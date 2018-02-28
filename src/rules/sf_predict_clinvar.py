"""Trained with panels,
   evaluate on clinvar
"""

rule eval_by_gene_clinvar:
    input:  i = WORK + 'roc_df_{eval_source}/{features}'
    output: o = DATA + 'interim/pred_clinvar_eval/{eval_source}.{features}'
    run:
        keys = ['Disease', 'y']
        df_pre = pd.read_csv(input.i, sep='\t')
        crit = df_pre.apply(lambda row: not 'uc' in row['Disease'] and not 'issue' in row['Disease'] and not 'earing' in row['Disease'], axis=1)
        df = df_pre[crit]
        wrong_df= df.groupby(keys).apply(calc_wrong).reset_index().rename(columns={0:'wrongFrac'})
        tot_wrong_df = df.groupby(['Disease']).apply(calc_wrong).reset_index().rename(columns={0:'predictorWrongFracTot'})
        size_df = df.groupby(keys).size().reset_index().rename(columns={0:'size'})
        m = pd.merge(wrong_df, size_df, on=keys)
        m.loc[:, 'var_class'] = m.apply(lambda row: 'pathogenic' if row['y'] == 1 else 'benign', axis=1)
        m.loc[:, 'clinvar_type'] = m.apply(lambda row: row['Disease'].split(':')[1], axis=1)
        m.loc[:, 'dd'] = m.apply(lambda row: row['Disease'].split(':')[0], axis=1)
        pd.merge(m, tot_wrong_df, on='Disease', how='left')[['Disease', 'dd', 'var_class', 'clinvar_type', 'size', 'predictorWrongFracTot', 'wrongFrac']].to_csv(output.o, index=False, sep='\t')

rule combine_features_by_gene_clinvar_plot:
    input:  expand(DATA + 'interim/pred_clinvar_eval/{{eval_source}}.{feature}', feature=COMBO_FEATS)
    output: o=DATA + 'interim/{eval_source}.by_gene_feat_combo.predictFullClinvar'
    run:
        pd.concat([read_gene_df(afile) for afile in list(input)]).to_csv(output.o, index=False, sep='\t')

rule plot_clinvar_eval:
    input:  DATA + 'interim/{eval_source}.by_gene_feat_combo.predictFullClinvar'
    output: DOCS + 'plot/eval_clinvar/{eval_source}.{disease}.predictFullClinvar.byVarClass{byVarClass}.png'
    run:
        dd = wildcards.disease.split(':')[0]
        if wildcards.byVarClass == 'True':
            plot_cmd = 'geom_col(aes(y=wrongFrac, x=reorder(combo, predictorWrongFracTot), fill=var_class), position="dodge")'
        else:
            plot_cmd = 'geom_col(aes(y=wrongFrac, x=reorder(combo, predictorWrongFracTot)), position="dodge")'
        R("""
          require(ggplot2)
          d = read.delim("{input}", sep='\t', header=TRUE)
          p = ggplot(data=d[d$dd=="{dd}",]) + {plot_cmd} +
              ylab('Wrong prediction fraction') + xlab('') + theme_bw() + facet_grid(clinvar_type~.) +
              labs(fill="Variant class") + coord_flip() +
              theme(axis.text.y = element_text(size=6))
          ggsave("{output}", p, height=20)
          """)

rule tmp_c:
    input: DOCS + 'plot/eval_clinvar/clinvar.genedx-epi:tot.predictFullClinvar.byVarClassTrue.png',
           DOCS + 'plot/eval_clinvar/clinvar.genedx-epi:tot.predictFullClinvar.byVarClassFalse.png'

rule all_clinvar_eval:
    input:
           expand(DOCS + 'plot/eval_clinvar/{eval_source}.{disease}:{d2}.predictFullClinvar.png', eval_source=('clinvar',), d2=('tot', ), disease=DD), \



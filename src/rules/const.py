import os, sys
from itertools import combinations, chain
from p_change import *

# SECRETS = '/home/evansj/me/.secrets/'
# sys.path.append(SECRETS)
# from pass_wd import *

# DONE = TWILIO_PRE + "--data-urlencode 'Body=DONE' " + TWILIO_POST
# FAIL = TWILIO_PRE + "--data-urlencode 'Body=FAIL' " + TWILIO_POST

p = os.getcwd()
if 'src' in p:
    PWD = p.split('src/')[0]
else:
    PWD = p + '/'

TMP = PWD + 'tmp/'
WORK = PWD + 'work/'
WORK2 = '/mnt/isilon/cbmi/variome/perry/projects/sarmadi/mahdi_epi/work/'
DOCS = PWD + 'docs/'
FILES = PWD + 'docs/'
SCRIPTS = PWD + 'src/scripts/'
SCRIPTS2 = '/mnt/isilon/cbmi/variome/perry/projects/sarmadi/mahdi_epi/src/scripts/'
DATA = PWD + 'data/'
LOG = PWD + 'log/'
CONFIG = PWD + 'configs/'
PLOTS = PWD + 'docs/plots/'

EXAC_DIR = '/home/evansj/me/projects/diskin/target_exac_setup/data/'
EXAC_PED = '/home/evansj/me/projects/diskin/target_exac_setup/files/JUNK_PED.ped'
VCFANNO_LUA_FILE = '/home/evansj/me/projects/me/vcfanno_lua/scripts/target.lua'

ISILON = '/mnt/isilon/cbmi/variome/perry/'
TABIX = ISILON + 'bin/tabix'
BGZ = '/nas/is1/bin/bgzip'
VT = ISILON + 'condas/miniconda3/envs/target_capture/bin/vt'
PY27_T = '~/me/condas/miniconda3/envs/testPy27/bin/python'
PY27 = '~/me/condas/miniconda3/envs/py27/bin/python'
JAVA = '/nas/is1/bin/java'
EFF = '/home/evansj/me/tools/snpEff/snpEff.jar'
SIFT = '/home/evansj/me/tools/snpEff/SnpSift.jar'
SIFT_DBNSFP = '/home/evansj/me/tools/snpEff/data/dbNSFP/dbNSFP2.4.txt.gz'
EFF_CONFIG = '/home/evansj/me/tools/snpEff/snpEff.config'
CLINVAR = '/mnt/isilon/cbmi/variome/bin/gemini/data/gemini_data/clinvar_20160203_noUnicode.tidy.vcf.gz'
HEADER_HCKR =  '/nas/is1/perry/projects/me/vcfHeaderHckr/vcfHeadrHckr.py'
VCFANNO = '/mnt/isilon/cbmi/variome/bin/vcfanno/0.0.11/bin/vcfanno'
GEMINI_ANNO = '/mnt/isilon/cbmi/variome/bin/gemini/data/gemini_data'

HG19_FA = DATA + 'raw/hg19.fa'

FOCUS_GENES = ('SCN1A','SCN2A','KCNQ2', 'KCNQ3', 'CDKL5',
               'PCDH19', 'SCN1B', 'SCN8A', 'SLC2A1',
               'SPTAN1', 'STXBP1', 'TSC1')

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

feats = ('mpc', 'revel', 'ccr', 'is_domain')
COMBO_FEATS = ['-'.join(x) for x in powerset(feats) if x]

DBNSFP_FIELDS = 'Interpro_domain,SIFT_score,Polyphen2_HVAR_pred,RadialSVM_pred,LR_pred,Reliability_index,FATHMM_pred,MutationAssessor_pred,MutationTaster_pred,phyloP100way_vertebrate,phastCons100way_vertebrate'

HEADER_FIX = 'eff_indel_splice,1,Flag AC,1,Integer AF,1,Float dbNSFP_FATHMM_pred,.,String dbNSFP_Interpro_domain,.,String dbNSFP_LR_pred,.,String dbNSFP_phyloP100way_vertebrate,.,String dbNSFP_phastCons100way_vertebrate,.,String dbNSFP_SIFT_score,.,String dbNSFP_Reliability_index,.,String dbNSFP_RadialSVM_pred,.,String dbNSFP_RadialSVM_pred,.,String dbNSFP_Polyphen2_HVAR_pred,.,String dbNSFP_MutationTaster_pred,.,String dbNSFP_MutationAssessor_pred,.,String'

CRUZ_PY = '/home/evansj/me/franklin_condas/envs/cruzdb/bin/python'

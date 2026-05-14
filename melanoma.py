import pandas as pd
gene_exp_inmune = pd.read_csv('https://drive.google.com/uc?id=1PYzEIdmnfjOnBpPDIFBE9hL1Lkj_OBCk',index_col=0)
clinical_info_inmune = pd.read_csv('https://drive.google.com/uc?id=1hHQfcvrFa5Jds-9tW_X4sHjKpYKdii9s',index_col=0)
X, y = gene_exp_inmune, clinical_info_inmune
print("Número de instancias y número de variables:", X.shape)
print("Valores de clase:", pd.unique(y['RNASEQ-CLUSTER_CONSENHIER']))
print("Número de instancias por clase:\n", y.value_counts())

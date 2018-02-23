# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 08:15:06 2018

@author: 593419
"""

#%% Package Imports
import pandas as pd
from pandas import read_csv
import statsmodels.formula.api as smf
import sklearn as sk
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import seaborn as sns
from scipy import stats
import scipy

file=r'C:/Users/593419/Documents/PythonScripts/Data Visualization/clean_data_lung.csv'
healthdata=pd.read_csv(file)

healthdata=healthdata.replace(-1111.1, np.NaN)
healthdata=healthdata.replace(-2222, np.NaN)

#%% Functions unused
def minmaxnormalize (columnname, combined):
    maxx = combined[columname].max()
    minx = combined[columname].min()

    x = combined[columname]
    xprime =  (x-minx)/(maxx-minx)

    return (xprime)

#%% scale certain values
c=['Recent_Drug_Use', 'Ecol_Rpt', 'Salm_Rpt', 'Shig_Rpt']

for i in c:
   healthdata[i]=healthdata[i]/healthdata['Population_Size']
   
c=['a_cl_ln',
   'a_cn_ln',
   'a_diesel_ln',
   'a_eox_ln',
   'a_pb_ln',
   'a_so2_mean_ln',
   'a_no2_mean_ln',
   'a_co_mean_ln',
   'a_o3_mean_ln',
   'a_teca_ln',
   'w_112tca_ln',
   'a_dbcp_ln',
   'a_tdi_ln',
   'a_2clacephen_ln',
   'a_2np_ln',
   'a_pnp_ln',
   'a_ch3cn_ln',
   'a_acetophenone_ln',
   'a_acrolein_ln',
   'a_acrylic_acid_ln',
   'a_c3h3n_ln',
   'a_sb_ln',
   'a_benzidine_ln',
   'a_benzyl_cl_ln',
   'a_be_ln',
   'a_biphenyl_ln',
   'a_dehp_ln',
   'a_bromoform_ln',
   'a_cd_ln',
   'a_cs2_ln',
   'a_cs_ln',
   'a_c6h5cl_ln',
   'a_chloroform_ln',
   'a_chloroprene_ln',
   'a_cr_ln',
   'a_cresol_ln',
   'a_cumene_ln',
   'a_dbp_ln',
   'a_dmf_ln',
   'a_me2_phthalate_ln',
   'a_me2so4_ln',
   'a_ech_ln',
   'a_etacrylate_ln',
   'a_etcl_ln',
   'a_edb_ln',
   'a_edc_ln',
   'a_egly_ln',
   'a_edcl2_ln',
   'a_glycol_ethers_ln',
   'a_hcb_ln',
   'a_hcbd_ln',
   'a_hccpd_ln',
   'a_hexane_ln',
   'a_n2h2_ln',
   'a_hcl_ln',
   'a_isophorone_ln',
   'a_mn_ln',
   'a_hg_ln',
   'a_meoh_ln',
   'a_mibk_ln',
   'a_mma_ln',
   'a_mecl_ln',
   'a_mehydrazine_ln',
   'a_mtbe_ln',
   'a_nitrobenzene_ln',
   'a_dma_ln',
   'a_otoluidine_ln',
   'a_pahpom_ln',
   'a_pcp_ln',
   'a_ph3_ln',
   'a_p_ln',
   'a_pcbs_ln',
   'a_procl2_ln',
   'a_proo_ln',
   'a_quinoline_ln',
   'a_se_ln',
   'a_cl4c2_ln',
   'a_toluene_ln',
   'a_c2hcl3_ln',
   'a_etn_ln',
   'a_vyac_ln',
   'a_vycl_ln',
   'a_11dce_ln']

for i in c:
    healthdata[i]=np.exp(healthdata[i])
   
 
c=['Population_Size',
   'Population_Density',
   'Poverty',
   'White',
   'Black',
   'Hispanic',
   'Native_American',
   'Asian',
   'No_Exercise',
   'Few_Fruit_Veg',
   'Obesity',
   'Smoker',
   'Diabetes',
   'Uninsured',
   'Prim_Care_Phys_Rate',
   'Dentist_Rate',
   'Unemployed',
   'Major_Depression',
   'Recent_Drug_Use',
   'Ecol_Rpt',
   'Salm_Rpt',
   'Shig_Rpt',
   'a_ccl4',
   'a_cl_ln',
   'a_cn_ln',
   'a_diesel_ln',
   'a_eox_ln',
   'a_pb_ln',
   'a_pm10_mean_ln',
   'a_pm25_mean',
   'a_so2_mean_ln',
   'a_no2_mean_ln',
   'a_co_mean_ln',
   'a_o3_mean_ln',
   'a_teca_ln',
   'w_112tca_ln',
   'a_dbcp_ln',
   'a_tdi_ln',
   'a_2clacephen_ln',
   'a_2np_ln',
   'a_pnp_ln',
   'a_ch3cn_ln',
   'a_acetophenone_ln',
   'a_acrolein_ln',
   'a_acrylic_acid_ln',
   'a_c3h3n_ln',
   'a_sb_ln',
   'a_benzidine_ln',
   'a_benzyl_cl_ln',
   'a_be_ln',
   'a_biphenyl_ln',
   'a_dehp_ln',
   'a_bromoform_ln',
   'a_cd_ln',
   'a_cs2_ln',
   'a_cs_ln',
   'a_c6h5cl_ln',
   'a_chloroform_ln',
   'a_chloroprene_ln',
   'a_cr_ln',
   'a_cresol_ln',
   'a_cumene_ln',
   'a_dbp_ln',
   'a_dmf_ln',
   'a_me2_phthalate_ln',
   'a_me2so4_ln',
   'a_ech_ln',
   'a_etacrylate_ln',
   'a_etcl_ln',
   'a_edb_ln',
   'a_edc_ln',
   'a_egly_ln',
   'a_edcl2_ln',
   'a_glycol_ethers_ln',
   'a_hcb_ln',
   'a_hcbd_ln',
   'a_hccpd_ln',
   'a_hexane_ln',
   'a_n2h2_ln',
   'a_hcl_ln',
   'a_isophorone_ln',
   'a_mn_ln',
   'a_hg_ln',
   'a_meoh_ln',
   'a_mibk_ln',
   'High_Blood_Pres',
   'a_mma_ln',
   'a_mecl_ln',
   'a_mehydrazine_ln',
   'a_mtbe_ln',
   'a_nitrobenzene_ln',
   'a_dma_ln',
   'a_otoluidine_ln',
   'a_pahpom_ln',
   'a_pcp_ln',
   'a_ph3_ln',
   'a_p_ln',
   'a_pcbs_ln',
   'a_procl2_ln',
   'a_proo_ln',
   'a_quinoline_ln',
   'a_se_ln',
   'a_cl4c2_ln',
   'a_toluene_ln',
   'a_c2hcl3_ln',
   'a_etn_ln',
   'a_vyac_ln',
   'a_vycl_ln',
   'a_11dce_ln']

#%% Remove Na values
combined=healthdata
combined=combined.rename(columns={'Cancer_Incidence':'Cancer'})
combined=combined.drop(['FIPS','Sulfur_Dioxide_Ind', 'Toxic_Chem', 'Lead_Ind', 'Ozone_Ind', 'Particulate_Matter_Ind'], axis=1)
combined=combined.dropna()

#%% categorical scaling
normalized=pd.DataFrame(columns=[combined.columns[0:]])
normalized['Cancer']=combined['Cancer']
normalized=combined
normalized['Cancer']=normalized.Cancer.astype(int)
normalized['Cancer']=pd.qcut(normalized['Cancer'],5, labels=False, duplicates='drop')
normalized['Cancer']=normalized['Cancer']+1
normalized=normalized.convert_objects(convert_numeric=True)

for i in c:
    normalized[i]=pd.qcut(normalized[i],500, labels=False, duplicates='drop')
    normalized[i]=normalized[i].astype(int)
    normalized[i]=normalized[i]+1


#%% min max normalization
#for i in range (1,combined.shape[1]):
 #   columname=combined.columns[i]
 #   xprime=minmaxnormalize(columname,combined)
  #  normalized[columname]=xprime
    
#%% Split Test and Train
testdata=normalized
train=testdata.sample(frac=0.75, random_state=50)
test=testdata.drop(train.index) 

#%% manual random forest
rf=RandomForestClassifier(n_jobs=1, n_estimators=80, oob_score=True, max_features=0.3, max_depth=6)
rf1=rf.fit(train[train.columns[1:]], train["Cancer"])
predictcancer=rf1.predict(test[test.columns[1:]])
traincancer=rf1.predict(train[train.columns[1:]])

#%% Cross-Validated Random Forest
param_grid={'n_estimators': [50,60,70,80,90,100,120],
           'max_depth': [2, 4, 6, 8, 10, 12, 14]
           }
from sklearn.grid_search import GridSearchCV
grid_clf=GridSearchCV(rf, param_grid, cv=3)

#%% Training cross-validated random forest
rf2=grid_clf.fit(train[train.columns[1:]], train["Cancer"])

#%% Using the Best Forest Model
predictcancer=rf2.best_estimator_.predict(test[test.columns[1:]])
traincancer=rf2.best_estimator_.predict(train[train.columns[1:]])
alltest=rf2.best_estimator_.predict(testdata[testdata.columns[1:]])

#%% error metrics
confusion=sk.metrics.confusion_matrix(test["Cancer"],predictcancer)
print "Confusion matrix ", sk.metrics.confusion_matrix(test["Cancer"],predictcancer)
print 'Out-of-bag score estimate: ', rf.oob_score_
print "Train Accuracy:: ", sk.metrics.accuracy_score(train["Cancer"], traincancer)
print "Test Accuracy:: ", sk.metrics.accuracy_score(test["Cancer"], predictcancer)
print "All Accuracy:: ", sk.metrics.accuracy_score(testdata["Cancer"],alltest)                 

#%% feature importance                
importances = rf2.best_estimator_.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf2.best_estimator_.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

for i in range (0,test.shape[1]-1):
    print("feature:  " + test.columns[indices[i] +1] + " (%f)" % (importances[indices[i]]))

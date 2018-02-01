library(dplyr)
healthData <- read.csv('clean_data.csv',
                       na.strings = c('-2222', '-1111.1'),
                       header = TRUE)

# scale Uninsured, Unemployed, Major_Depression, Recent_Drug_Use,
# *_Rpt, Toxic_Chem by population size
for (i in c('Uninsured', 'Unemployed', 'Major_Depression',
            'Recent_Drug_Use', 'Ecol_Rpt', 'Salm_Rpt', 'Shig_Rpt')) {
    healthData[[i]] <- healthData[[i]]/healthData['Population_Size']
}
    

# factorize the columns that are not indicators and bin using ntiles
# with 5 levels for continuously varying columns
for (i in c('Cancer_Incidence',
            'Population_Density',
            'Poverty
healthData$Poverty <- as.factor(ntile(healthData$Poverty, 5))

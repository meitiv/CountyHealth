#!/usr/bin/env python3

# read the cancer incidence
import csv
cancerIncidence = {}
with open('incd.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        cancerIncidence[row[1].strip()] = row[3].strip()

# read the demographic data
popSize = {}
popDens = {}
poverty = {}
fracCAU = {}
fracAA = {}
fracHIS = {}
fracNA = {}
fracASI = {}
with open('chsi_dataset/DEMOGRAPHIC.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = row['State_FIPS_Code'] + row['County_FIPS_Code']
        popSize[key] = row['Population_Size']
        popDens[key] = row['Population_Density']
        poverty[key] = row['Poverty']
        fracCAU[key] = row['White']
        fracAA[key] = row['Black']
        fracHIS[key] = row['Hispanic']
        fracNA[key] = row['Native_American']
        fracASI[key] = row['Asian']

def padZero(text,lenght):
    l = len(text)
    if l < length:
        return '0'*(length - l) + text
    else:
        return text
    
# read in the health factors
sedentary = {}
poor_diet = {}
obesity = {}
hypertension = {}
smoker = {}
diabetic = {}
uninsured = {}
primary_care = {}
dentist = {}
with open('chsi_dataset/RISKFACTORSANDACCESSTOCARE.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fipsState = padZero(row['State_FIPS_Code'],2)
        fipsCounty = padZero(row['County_FIPS_Code'],3)
        key = fipsState + fipsCounty
        sedentary[key] = row['No_Exercise']
        poor_diet[key] = row['Few_Fruit_Veg']
        obesity[key] = row['Obesity']
        hypertension[key] = 
        smoker[key] = row['Smoker']
        diabetic[key] = row['Diabetes']
        uninsured[key] = row['Uninsured']
        primary_care[key] = row['Prim_Care_Phys_Rate']
        dentist[key] = row['Dentist_Rate']

# read in exposure
with open('chsi_dataset/VUNERABLEPOPSANDENVHEALTH.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fipsState = padZero(row['State_FIPS_Code'],2)
        fipsCounty = padZero(row['County_FIPS_Code'],3)
        key = fipsState + fipsCounty
        

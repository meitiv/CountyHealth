#!/usr/bin/env python3

# make the dataframe
import pandas as pd
cols = ['Cancer_Incidence',
        'Population_Size',
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
        'High_Blood_Pres',
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
        'Toxic_Chem',
        'Sulfur_Dioxide_Ind',
        'Ozone_Ind',
        'Particulate_Matter_Ind',
        'Lead_Ind']

data = pd.DataFrame(columns = cols)
# read the cancer incidence
import csv
with open('incd.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        key = row[1].strip()
        incidence = row[3].strip()
        data.set_value(key,'Cancer_Incidence', incidence)

# read the demographic data
with open('chsi_dataset/DEMOGRAPHICS.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = row['State_FIPS_Code'] + row['County_FIPS_Code']
        for col in cols:
            if col in row:
                data.set_value(key, col, row[col])

def padZero(text,length):
    l = len(text)
    if l < length:
        return '0'*(length - l) + text
    else:
        return text
    
# read in the health factors
with open('chsi_dataset/RISKFACTORSANDACCESSTOCARE.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fipsState = padZero(row['State_FIPS_Code'],2)
        fipsCounty = padZero(row['County_FIPS_Code'],3)
        key = fipsState + fipsCounty
        for col in cols:
            if col in row:
                data.set_value(key, col, row[col])

# read in exposure
with open('chsi_dataset/VUNERABLEPOPSANDENVHEALTH.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fipsState = padZero(row['State_FIPS_Code'],2)
        fipsCounty = padZero(row['County_FIPS_Code'],3)
        key = fipsState + fipsCounty
        for col in cols:
            if col in row:
                data.set_value(key, col, row[col])

data.to_csv('clean_data.csv')        

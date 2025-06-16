import pandas as pd

def transform_data(demographics, nutrients, body):
    df = demographics.merge(nutrients, on='SEQN').merge(body, on='SEQN')
    df = df[(df['RIAGENDR'] == 2) & (df['RIDAGEYR'].between(20, 40))]

    df['BMI_Group'] = pd.cut(df['BMXBMI'], bins=[0,18.5,25,30,100],
                             labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

    df['Income_Group'] = pd.cut(df['INDFMPIR'], bins=[0,1.3,3,5],
                                labels=['Low', 'Middle', 'High'])

    df = df[['SEQN', 'RIDAGEYR', 'BMI_Group', 'Income_Group',
             'DR1TCALC', 'DR1TIRON', 'DR1TPOTA', 'DR1TMAGN']]

    df.columns = ['SEQN', 'Age', 'BMI_Group', 'Income_Group',
                  'Calcium', 'Iron', 'Potassium', 'Magnesium']

    RDA = {'Iron': 18, 'Calcium': 1000, 'Magnesium': 310}
    df['Iron_RDA'] = df['Iron'] / RDA['Iron']
    df['Calcium_RDA'] = df['Calcium'] / RDA['Calcium']
    df['Magnesium_RDA'] = df['Magnesium'] / RDA['Magnesium']

    df['Low_Iron'] = df['Iron'] < 18
    df['Low_Calcium'] = df['Calcium'] < 1000
    df['Low_Magnesium'] = df['Magnesium'] < 310
    df['Low_Potassium'] = df['Potassium'] < 2600
    
    df.to_csv("outputs/cleaned_data.csv", index=False)

    return df


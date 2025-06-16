import os

def save_grouped_rda(df, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    grouped_rda_bmi = df.groupby('BMI_Group', observed=True)[['Iron_RDA', 'Calcium_RDA', 'Magnesium_RDA']].mean()
    grouped_rda_income = df.groupby('Income_Group', observed=True)[['Iron_RDA', 'Calcium_RDA', 'Magnesium_RDA']].mean()

    bmi_path = os.path.join(output_dir, "bmi_grouped_rda.csv")
    income_path = os.path.join(output_dir, "income_grouped_rda.csv")

    grouped_rda_bmi.reset_index().to_csv(bmi_path, index=False)
    print("✅ Exported BMI grouped RDA data to CSV for Tableau.")

    grouped_rda_income.reset_index().to_csv(income_path, index=False)
    print("✅ Exported INCOME grouped RDA data to CSV for Tableau.")

    return grouped_rda_bmi, grouped_rda_income
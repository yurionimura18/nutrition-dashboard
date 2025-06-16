

from etl.extract import extract_datasets
from etl.transform import transform_data
from etl.load import save_grouped_rda

if __name__ == "__main__":
    demographics, nutrients, body = extract_datasets()
    df = transform_data(demographics, nutrients, body)
    grouped_rda_bmi, grouped_rda_income = save_grouped_rda(df)
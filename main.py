import pandas as pd

def get_earthquake_data():
	df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

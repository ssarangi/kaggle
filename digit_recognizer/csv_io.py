import pandas as pd

def read_csv(csv_filename):
	print("Reading file: " % csv_filename)
	df = pd.read_csv(csv_filename, dtype=float,header=0)
	return df

def write_csv(csv_filename, df):
	df.to_csv(csv_filename)

if __name__ == "__main__":
	read_csv("input_data/train.csv")
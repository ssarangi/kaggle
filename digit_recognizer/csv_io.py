import pandas as pd

def read_csv(csv_filename):
	df = pd.read_csv(csv_filename, dtype=float,header=0)
	return df

if __name__ == "__main__":
	read_csv("input_data/train.csv")
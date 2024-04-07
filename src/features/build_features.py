import pandas as pd
import numpy as np
import pathlib

from feature_definitions import feature_build
from sklearn.model_selection import train_test_split



def load_data(data_path):
    # Load your dataset from a given path
    df = pd.read_csv(data_path)
    return df

def split_data(df, test_split, seed):
    # Split the dataset into train and test sets
    train, test = train_test_split(df, test_size=test_split, random_state=seed)
    return train, test

def save_data(train, test, output_path):
    # Save the split datasets to the specified output path
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)
    train.to_csv(output_path + '/train.csv', index=False)
    test.to_csv(output_path + '/test.csv', index=False)




if __name__ == '__main__':
    curr_dir = pathlib.Path(__file__)
    home_dir = curr_dir.parent.parent.parent
    
    train_path = home_dir.as_posix() + '/data/raw/train.csv'
    test_path = home_dir.as_posix() + '/data/raw/test.csv'
    
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    output_path = home_dir.as_posix() + '/data/processed'

    train_data = feature_build(train_data, 'train-data')
    test_data = feature_build(test_data, 'test-data')

    save_data(train_data, test_data, output_path)

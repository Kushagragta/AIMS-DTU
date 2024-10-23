import pandas as pd
import numpy as np

def one_hot_encode(df, column):
    unique_values = df[column].unique()
    encoded_df = pd.DataFrame()
    
    for value in unique_values:
        encoded_df[column + '_' + str(value)] = np.where(df[column] == value, 1, 0)
    return encoded_df

if __name__ == "__main__":
   
    data = {
        'color': ['red', 'blue', 'green', 'blue', 'green', 'red'],
        'size': ['S', 'M', 'L', 'S', 'M', 'L']
    }
    
    df = pd.DataFrame(data)
    encoded_color_df = one_hot_encode(df, 'color')
    encoded_size_df = one_hot_encode(df, 'size')
    df_encoded = pd.concat([df, encoded_color_df, encoded_size_df], axis=1)
    df_encoded = df_encoded.drop(['color', 'size'], axis=1)
    print("One-Hot Encoded DataFrame:")
    print(df_encoded)

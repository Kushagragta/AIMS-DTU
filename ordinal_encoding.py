import pandas as pd
import numpy as np

def ordinal_encode(df, column):
    unique_values = df[column].unique()
    value_map = {val: i for i, val in enumerate(unique_values)}
    encoded_column = df[column].map(value_map)
    return encoded_column, value_map


if __name__ == "__main__":
    data = {
        'color': ['red', 'blue', 'green', 'blue', 'green', 'red'],
        'size': ['S', 'M', 'L', 'S', 'M', 'L']
    }
    df = pd.DataFrame(data)
    encoded_color, color_mapping = ordinal_encode(df, 'color')
    df['encoded_color'] = encoded_color
    encoded_size, size_mapping = ordinal_encode(df, 'size')
    df['encoded_size'] = encoded_size
    
    
    print("Encoded DataFrame:")
    print(df)
    
    print("\nColor Mapping:")
    print(color_mapping)
    
    print("\nSize Mapping:")
    print(size_mapping)

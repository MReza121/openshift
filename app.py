import pandas as pd

def save_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df.to_csv('/path/to/your/file.csv', index=False)

if __name__ == '__main__':
    save_dataframe()

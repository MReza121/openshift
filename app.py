import pandas as pd

def save_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df.to_csv('/etc/mymodel', index=False)

if __name__ == '__main__':
    save_dataframe()

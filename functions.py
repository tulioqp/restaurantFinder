import pandas as pd

# load data
def load(path):
    '''
    function to read csv data. input: string path, return: pandas dataframe
    '''

    df = pd.read_csv(path)

    return df

# ----------------------

def test(dataframe: pd.DataFrame):
    
    return dataframe.head()

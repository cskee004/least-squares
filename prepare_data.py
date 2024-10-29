import pandas as pd
import re

def build_table(path, time_step):
    """
    Builds a DataFrame for the given file and time step.  

    Args:
        path      (str): Text file with space-separated values.
        time_step (int): Value for each time interval.
    
    Returns:
        df (DataFrame): DataFrame with time steps as the index and CPU temperature values.
    """
    
    time_index = []
    cleaned_lines = []
    
    with open(path) as fp:
        for line in fp:
            cleaned_line = re.sub(r'[+°C]', '', line).strip()
            cleaned_lines.append(cleaned_line)
    
    for i in range(len(cleaned_lines)):
        time_index.append(i * time_step)
    
    df = pd.DataFrame([line.split() for line in cleaned_lines], dtype=float)
    df.columns = ["0", "1", "2", "3"]
    df.index = time_index
    
    return df

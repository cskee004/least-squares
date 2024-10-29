import sys
import os
from prepare_data import build_table
from interpolation import piecewise_interpolation

def main(input_file, output_dir, time_step):
    """
    Main driver that performs piecewise interpolation and least squares regression on a DataFrame column.
    A single column is processed, then results are written to a text document in the output directory.
    
    Args:
        input_file  (str): Input file path.
        outout_dir  (str): Output file path.
        time_step   (int): Time interval value.
    """
    
    df = build_table(input_file, time_step)
    
    for column_name in df.columns:
        results = piecewise_interpolation(df[column_name])
        
        output_file = os.path.join(output_dir, f"CPU_{column_name}.txt")
        
        with open(output_file, 'w') as f:
            for i in range(len(results) - 1):
                slope, intercept = results[i]
                x0, x1 = df.index[i], df.index[i + 1]
                f.write(f"{x0:8} <= x <= {x1:8} ; y = {float(intercept):10.4f} + {float(slope):10.4f} x ; interpolation\n")
            
            slope, intercept = results[-1]
            f.write(f"{df.index[0]:8} <= x <= {df.index[-1]:8} ; y = {float(intercept):10.4f} + {float(slope):10.4f} x ; least-squares\n")

def parse_arguments():
    """
    Parses command-line arguments for input file, output directory, and time step.  
    
    Returns:
        input_file (str): Input file path.
        output_dir (str): Output file path.
        time_step  (int): Time interval value.
    """
    
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_file> <output_directory> <time_step>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    time_step = int(sys.argv[3])

    os.makedirs(output_dir, exist_ok=True)

    return input_file, output_dir, time_step

if __name__ == "__main__":
    input_file, output_dir, time_step = parse_arguments()
    main(input_file, output_dir, time_step)

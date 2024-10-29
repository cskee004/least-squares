# Piecewise Interpolation and Least Squares Program

This program performs piecewise interpolation and least-squares regression on data provided in a space-separated text file. For each column of data, it calculates interpolation slopes and y-intercepts for defined intervals, as well as a least-squares regression for the entire column. The results are saved to a specified output directory.

## Requirements

- Python 3.x
- `pandas` library

## File Structure

- **`input.py`**: Main script to run the program.
- **`interpolation.py`**: Contains the functions for calculating slopes, intercepts, and performing piecewise interpolation.
- **`/tests/test_interpolation.py`**: Unit tests for building a dataframe with the given input file and time step, calculating slopes, intercepts, 
and performing piecewise interpolation.

## Usage

### Command

To run the program, use the following command(s):

```bash
python input.py <input_file> <output_directory> <time_step>
```

- `<input_file>`: Path to the input text file containing the data.
- `<output_directory>`: Directory where output files will be saved.
- `<time_step>`: Integer value specifying the time step between indices.

```bash
python input.py ./data/test-input-labels.txt ./output 30
```

```bash
python input.py ./data/test-input-no-labels.txt ./output 30
```

To run the programs unit tests, use the following command:

```bash
pytest
```

## Input File Format

The input file should be a space-separated `.txt` file without column labels. Each line should represent values at a specific time index.

Example:

```
61.0 63.0 50.0 58.0
80.0 81.0 68.0 77.0
62.0 63.0 52.0 60.0
83.0 82.0 70.0 79.0
68.0 69.0 58.0 65.0
```

```
+61.0°C +63.0°C +50.0°C +58.0°C
+80.0°C +81.0°C +68.0°C +77.0°C
+62.0°C +63.0°C +52.0°C +60.0°C
+83.0°C +82.0°C +70.0°C +79.0°C
+68.0°C +69.0°C +58.0°C +65.0°C
```

## Output

The output will contain one text file per column of data in the input file, saved in the specified output directory. Each file follows this format:

```
       0 <= x <=       30 ; y =      61.0000 +       0.6333 x ; interpolation
      30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
      60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
      90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation
       0 <= x <=      120 ; y =      67.4000 +       0.0567 x ; least-squares
```

- Each line represents an interval with a slope (`m`) and y-intercept (`b`) for that segment.
- The final line displays the least-squares regression for the entire range.

## Functionality

1. **build_table**: Constructs a DataFrame with a specified time step based on the input file.
2. **piecewise_interpolation**: Calculates slopes and intercepts for each interval and performs least-squares regression.
3. **calc_slope and calc_intercept**: Helper functions to compute slope and y-intercept.
4. **least_squares**: Calculates least-squares regression parameters.
from prepare_data import build_table
from interpolation import *

test_file = "./data/test-input-no-labels.txt"
time_step = 30
temperature_table = build_table(test_file, time_step)

df0 = temperature_table['0'] # cpu_0
df1 = temperature_table['1']
df2 = temperature_table['2']
df3 = temperature_table['3']
    
expected_cpu0 = [   ('0.6333', '61.0000'), 
                    ('-0.6000', '98.0000'), 
                    ('0.7000', '20.0000'), 
                    ('-0.5000', '128.0000'),
                    ('0.0567', '67.4000')] # least-squares result

expected_cpu1 = [   ('0.6000', '63.0000'), 
                    ('-0.6000', '99.0000'), 
                    ('0.6333', '25.0000'), 
                    ('-0.4333', '121.0000'),
                    ('0.0433', '69.0000')]

expected_cpu2 = [   ('0.6000', '50.0000'), 
                    ('-0.5333', '84.0000'), 
                    ('0.6000', '16.0000'), 
                    ('-0.4000', '106.0000'),
                    ('0.0600', '56.0000')]

expected_cpu3 = [   ('0.6333', '58.0000'), 
                    ('-0.5667', '94.0000'), 
                    ('0.6333', '22.0000'), 
                    ('-0.4667', '121.0000'),
                    ('0.0533', '64.6000')]

def test_build_table():
    """ Unit test for building the given text file and time-step value into a DataFrame. """
    
    assert temperature_table.shape == (5, 4)
    assert temperature_table.iat[3, 2] == 70
    assert temperature_table.iat[0,0] == 61

def test_calc():
    """ Unit test for calculating slope and y-intercept. """
    
    assert calc_slope(30, 60, 80, 62) == '-0.6000'
    m = -0.6000
    
    assert calc_intercept(m, 30, 80) == '98.0000'
    
def test_least_squares():
    """ Unit test for the least-squares regression line. """
    
    x = df0.index.tolist()
    y = df0.iloc[0:].tolist()
    expected_slope = '0.0567'
    expected_intercept = '67.4000'
    m, b = least_squares(x, y)
    
    assert expected_slope == m
    assert expected_intercept == b

def test_df_ops():
    """ Unit tests for pieceswise interpolation for each cpu core. """
    
    results = piecewise_interpolation(df0)
    assert results == expected_cpu0
    
    results = piecewise_interpolation(df1)
    assert results == expected_cpu1
    
    results = piecewise_interpolation(df2)
    assert results == expected_cpu2
    
    results = piecewise_interpolation(df3)
    assert results == expected_cpu3
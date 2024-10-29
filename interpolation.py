def calc_slope(x0, x1, y0, y1):
    """
    Calculates the slope of a line given two points.

    Args:
        x0 (int): The x-coordinate of the first position.
        x1 (int): The x-coordinate of the second poisition.
        y0 (int): The y-coordinate of the first position.
        y1 (int): the y-coordinate of the second posiition.

    Returns:
        str: The slope as a string, formatted to four decimal places.
    """
    
    m = (y1 - y0) / (x1 - x0)
    return '{:.4f}'.format(m)

def calc_intercept(m, x0, y0):
    """
    Calculates the y-intercept of a line given a point and a slope.

    Args:
        m (float) : The slope of a line.
        x0 (float): The x-coordinate of the point.
        y0 (float): The y-coordinate of the point.
    
    Returns:
        str: The y-intercept as a string, rounded and formatted to four decimal places. 
    """
    
    b = y0 - (m * x0)
    return '{:.4f}'.format(round(b))

def piecewise_interpolation(df):
    """
    Performs piecewise interpolation and least squares regression on a DataFrame column.

    Args:
        df (pd.DataFrame): DataFrame with time steps as the index and CPU temperature values. 
    
    Returns:
        list of tuple: A list of tuples, each containing slope and y-intercept as strings formatted to four decimal places.
                       Example:
                        [
                            ('0.6333', '61.0000'), 
                            ('-0.6000', '98.0000'), 
                            ('0.7000', '20.0000'), 
                            ('-0.5000', '128.0000'),
                            ('0.0567', '67.4000') # least-squares result
                        ]
    """
    
    slopes = list()
    intercepts = list()
    x = df.index.tolist()
    y = df.iloc[0:].tolist()
    
    for i in range(4):
        x0 = df.index[i+1]
        x1 = df.index[i]
        y0 = df.iat[i+1]
        y1 = df.iat[i]
        m = calc_slope(x0, x1, y0, y1)
        slopes.append(m)
        intercepts.append(calc_intercept(float(m), float(x0), float(y0)))
    
    m, b = least_squares(x, y)
    slopes.append(m)
    intercepts.append(b)
    
    return list(zip(slopes, intercepts))
        
def least_squares(x_values, y_values):
    """
    Calculates the slope and intercept of a least-squares regression line.  

    Args:
        x_values (list of float): List of x values representing time steps.
        y_values (list of float): List of y values representing temperatures at each time step.
    
    Returns:
        list: A list containing the slope (str) and y-intercept (str) for the least-squares regression line,
              with the y-intercept formatted to four decimal places. 
    """
    
    sum_x = 0
    sum_y = 0
    sum_x_sqrd = 0
    sum_products = 0
    
    for x, y in zip(x_values, y_values):
        sum_x += x
        sum_y += y
        sum_x_sqrd += pow(x, 2)
        sum_products += x * y

    n = len(x_values)
    y1 = n * sum_products 
    y0 = sum_x * sum_y 
    x1 = n * sum_x_sqrd 
    x0 = sum_x * sum_x 
    
    m = calc_slope(x0, x1, y0, y1)
    temp = calc_intercept(float(m), sum_x, sum_y) 
    b = float(temp) / n

    return [m, '{:.4f}'.format(b)]
import math

# r_t = (P_t − P_{t-1}) / P_{t-1}

def simple_return(p_t, p_prev):


    """
    
    Compute the simple (arithmetic) return between two prices.

    Formula:
        r_t = (p_t - p_prev) / p_prev

    Parameters
    ----------
    p_t : float
        The price at time t (the later price).
    p_prev : float
        The price at time t-1 (the earlier price). Must not be zero.

    Returns
    -------
    float
        The simple return, e.g. 0.10 for a 10% gain.

    Raises
    ------
    ValueError
        If p_prev is zero (division by zero is undefined).
    
    """


    if p_prev == 0:
        raise ValueError("division by zero is undefined")
    return (p_t-p_prev)/p_prev




def log_return(p_t, p_prev):
    """
    Compute the natural-log return between two prices.

    Formula:
        r_log = ln(p_t / p_prev)

    Domain:
        p_t > 0 and p_prev > 0 (ln is only defined for positive inputs).

    Raises:
        ValueError: if p_t <= 0 or p_prev <= 0.
    """

    if p_t <= 0 or p_prev <= 0:
        raise ValueError("Only accepts positive inputs")
    return math.log(p_t / p_prev)






def log_return(price, prev_price):
    """Calculate logarithmic return."""
    if price <= 0 or prev_price <= 0:
        raise ValueError("Prices must be positive")

    return math.log(price / prev_price)




    
        
            
import math
#from quant_math.compounding import compound_value

# P_T = P_0 × (1 + r)^T


def compound_value(p0, r, T):


    """
    Future value of p0 compounded at rate r for T periods.

    Formula:
        P_T = p0 * (1 + r)**T

    Parameters
    ----------
    p0 : float
        The initial value (principal).
    r : float
        The per-period growth rate as a decimal, e.g. 0.05 for 5%.
    T : int
        Number of periods. Must be a non-negative integer.

    Returns
    -------
    float
        The value after T periods.

    Raises
    ------
    ValueError
        If T is negative.
    """


    if T < 0:
        raise ValueError("T must be non-negative")
    
    return p0 * (1 + r) ** T
    
    




def cagr(p0, p_t, periods):
    """Calculate compound annual growth rate."""
    if p0 <= 0 or p_t <= 0 or periods <= 0:
        raise ValueError("Inputs must be positive")

    return (p_t / p0) ** (1 / periods) - 1


def periods_to_target(p0, target, r):
    """Calculate periods needed to reach a target."""
    import math

    if p0 <= 0 or target <= 0 or r <= 0:
        raise ValueError("Inputs must be positive")

    return math.log(target / p0) / math.log(1 + r)

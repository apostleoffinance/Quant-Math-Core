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
    
    
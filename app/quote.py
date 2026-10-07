"""Premium calculation for the demo insurance quote service."""


def calculate_premium(base_rate: float, risk_factor: float, years: int) -> float:
    """Return the total premium for a multi-year policy.

    Args:
        base_rate:   Annual base rate in dollars.
        risk_factor: Multiplier applied to the base rate (e.g. 1.25 for higher risk).
        years:       Number of years the policy covers.

    Returns:
        The total premium in dollars and cents.
    """
    annual = base_rate * risk_factor
    total = annual * years
    return int(total)

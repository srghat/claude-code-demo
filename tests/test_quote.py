from app.quote import calculate_premium


def test_whole_dollar_premium():
    # A clean rate produces a whole-dollar premium.
    assert calculate_premium(base_rate=1000.0, risk_factor=1.0, years=1) == 1000.0


def test_multi_year_total():
    # Three years at a flat rate.
    assert calculate_premium(base_rate=500.0, risk_factor=1.0, years=3) == 1500.0


def test_risk_factor_preserves_cents():
    # Reproduces the customer bug report: a risk factor that introduces cents
    # must not have those cents dropped from the premium.
    assert calculate_premium(base_rate=1000.0, risk_factor=1.2345, years=1) == 1234.5

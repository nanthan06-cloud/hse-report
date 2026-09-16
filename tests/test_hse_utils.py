from hse_utils import incident_rate


def test_incident_rate_basic():
    assert incident_rate(1, 200_000) == 1.0


def test_incident_rate_zero_hours():
    assert incident_rate(5, 0) == 0.0

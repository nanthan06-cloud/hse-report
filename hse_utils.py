def incident_rate(incident_count: int, hours_worked: int) -> float:
    """Incidents per 200,000 hours worked (OSHA standard)."""
    if hours_worked == 0:
        return 0.0
    return (incident_count * 200_000) / hours_worked

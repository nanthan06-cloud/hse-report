# HSE Report

A small toolkit for tracking workplace Health, Safety, and Environment (HSE) incidents.

## Features

- Calculate incident rates from raw incident logs (OSHA-style, per 200,000 hours worked)

## Usage

```python
from hse_utils import incident_rate

rate = incident_rate(incident_count=3, hours_worked=100_000)
print(rate)  # 6.0
```

## Running tests

```bash
python -m pytest
```

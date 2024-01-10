# API Endpoints



### Endpoints
- `/api/nifty-50/`
- `/api/nifty-midcap50/`
- `/api/nifty-midcap150/`
- `/api/nifty-next50/`
- `/api/nifty-smallcap50/`


### Description
Retrieve filtered data for given index.

### Parameters
- `start_date` (Date): Start date for the data range.
- `end_date` (Date): End date for the data range.
- `open_above` (Float): Filter by open price greater than the specified value.
- `closed_above` (Float): Filter by close price greater than the specified value.
- `open_below` (Float): Filter by open price less than the specified value.
- `closed_below` (Float): Filter by close price less than the specified value.
- `high_above` (Float): Filter by high price greater than the specified value.
- `high_below` (Float): Filter by high price less than the specified value.
- `low_above` (Float): Filter by low price greater than the specified value.
- `low_below` (Float): Filter by low price less than the specified value.
- `turnover_greater_than` (Float): Filter by turnover greater than the specified value.
- `turnover_less_than` (Float): Filter by turnover less than the specified value.
- `shares_traded_greater_than` (Integer): Filter by shares traded greater than the specified value.
- `shares_traded_less_than` (Integer): Filter by shares traded less than the specified value.

### Response
```json
{
  "start-date": "2024-01-01",
  "end-date": "2024-01-10",
  "data": [
    {"field1": "value1", "field2": "value2", ...},
    {"field1": "value1", "field2": "value2", ...},
    ...
  ],
  "ranges": {
    "open": {"lowest": 100.0, "highest": 200.0},
    "close": {"lowest": 90.0, "highest": 210.0},
    "shares_traded": {"lowest": 50000, "highest": 100000}

  }
}


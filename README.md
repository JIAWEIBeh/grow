# Cost Accounting Prototype

A minimal FastAPI prototype for cost centers, cost elements, cost objects, transactions, allocation rules, and simple allocation engine.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit Swagger UI at http://localhost:8000/docs

## Seed demo data

```bash
python -c "from app.database import init_db; init_db(); from app.seed import seed; seed()"
```

## Key endpoints

- Cost Centers: `GET/POST/PUT/DELETE /api/cost-centers`
- Cost Elements: `GET/POST/PUT/DELETE /api/cost-elements`
- Cost Objects: `GET/POST/PUT/DELETE /api/cost-objects`
- Transactions: `GET/POST/PUT/DELETE /api/transactions`
- Reporting:
  - `GET /api/reporting/totals/by-center?period=YYYY-MM`
  - `GET /api/reporting/totals/by-object?period=YYYY-MM`
  - `POST /api/reporting/allocate/{period}`

## Notes

- SQLite default DB at `./costing.db`, override with `DATABASE_URL`.
- Allocation supports percentage and driver-based methods for demo purposes.
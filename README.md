# Insurance Quote Service

A tiny FastAPI service that calculates insurance premiums. Used to demo an
end-to-end bug-fix workflow with Claude Code.

## Run it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then:

```bash
curl -X POST localhost:8000/quote \
  -H 'content-type: application/json' \
  -d '{"base_rate": 1000, "risk_factor": 1.2345, "years": 1}'
```

## Test it

```bash
pytest -q
```

## The demo scenario

> **Bug report from a customer:** "Our quotes are coming back a few dollars
> short. A policy that should be **\$1,234.50** is quoted as **\$1,234**. The
> cents are disappearing."

Starting point: the suite is green, but it only covers whole-dollar cases, so
the bug is hidden. The task is to reproduce the report with a failing test,
fix `app/quote.py`, get the suite green, and open a PR.

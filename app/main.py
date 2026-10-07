"""FastAPI insurance quote service."""

from fastapi import FastAPI
from pydantic import BaseModel

from app.quote import calculate_premium

app = FastAPI(title="Insurance Quote Service")


class QuoteRequest(BaseModel):
    base_rate: float
    risk_factor: float
    years: int


class QuoteResponse(BaseModel):
    premium: float


@app.post("/quote", response_model=QuoteResponse)
def quote(req: QuoteRequest) -> QuoteResponse:
    """Calculate the total premium for a policy."""
    premium = calculate_premium(req.base_rate, req.risk_factor, req.years)
    return QuoteResponse(premium=premium)

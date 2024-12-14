import numpy as np

ANNUAL_RETURN = 0.05
WITHDRAWAL_RATE = 0.04

def calculate_fire(current_portfolio: float, fire_goal: float, monthly_savings: float) -> int:
    yearly_savings = monthly_savings * 12
    years = 0
    portfolio = current_portfolio

    while portfolio < fire_goal:
        portfolio += yearly_savings
        portfolio *= (1 + ANNUAL_RETURN)
        years += 1

    return years

def savings_needed(current_portfolio, fire_goal, years):
    if not years or years <= 0:
        return None

    annual_contribution = (fire_goal - current_portfolio * (1 + ANNUAL_RETURN)**years) / sum(
        [(1 + ANNUAL_RETURN)**i for i in range(1, years + 1)]
    )
    return annual_contribution / 12

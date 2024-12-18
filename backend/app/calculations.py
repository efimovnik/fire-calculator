import numpy as np

# Constants for returns based on asset allocation
STOCKS_RETURN = 0.07
BONDS_RETURN = 0.03
WITHDRAWAL_RATE = 0.04

def calculate_fire(current_age: int, current_portfolio: float, fire_goal: float, monthly_savings: float, stocks_allocation: float) -> (int, int):
    # Calculate weighted annual return
    annual_return = (stocks_allocation / 100) * STOCKS_RETURN + ((100 - stocks_allocation) / 100) * BONDS_RETURN
    
    yearly_savings = monthly_savings * 12
    years = 0
    portfolio = current_portfolio

    while portfolio < fire_goal:
        portfolio += yearly_savings
        portfolio *= (1 + annual_return)
        years += 1

    retirement_age = current_age + years
    return years, retirement_age

def savings_needed(current_age: int, current_portfolio: float, fire_goal: float, years: int, stocks_allocation: float):
    if not years or years <= 0:
        return None

    # Calculate weighted annual return
    annual_return = (stocks_allocation / 100) * STOCKS_RETURN + ((100 - stocks_allocation) / 100) * BONDS_RETURN

    annual_contribution = (fire_goal - current_portfolio * (1 + annual_return)**years) / sum(
        [(1 + annual_return)**i for i in range(1, years + 1)]
    )
    return annual_contribution / 12

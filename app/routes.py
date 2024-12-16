from flask import Blueprint, jsonify, request, render_template
from app.calculations import calculate_fire, savings_needed

routes = Blueprint('routes', __name__)

def parse_number(value):
    """
    Parses a user input string into a float.
    Handles commas, shorthand (e.g., 1M -> 1000000), and standard numeric strings.
    """
    if not value:
        return 0
    # Remove commas and convert shorthand notation (e.g., 1M -> 1000000)
    value = value.upper().replace(',', '').replace('M', '000000').replace('K','000').replace('k','000')
    return float(value)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/calculate', methods=['POST'])
def calculate():
    # Fetch and process input
    data = request.form
    current_age = int(data['current_age'])
    current_portfolio = parse_number(data['current_portfolio'])
    monthly_savings = parse_number(data['monthly_savings'])
    fire_goal = parse_number(data['fire_goal'])
    stocks_allocation = float(data['stocks_allocation'])
    years = data.get('years', None)
    years = int(years) if years else None  # Convert to int if provided, else keep as None

    # Calculate results
    if years:
        # If the user provides a target number of years, calculate savings needed
        required_savings = savings_needed(
            current_age, current_portfolio, fire_goal, years, stocks_allocation
        )
        results = {
            "required_monthly_savings": round(required_savings, 2),
            "years_provided": years
        }
    else:
        # If the user does not provide years, calculate time to FIRE and retirement age
        years_needed, retirement_age = calculate_fire(
            current_age, current_portfolio, fire_goal, monthly_savings, stocks_allocation
        )
        results = {
            "years_needed": years_needed,
            "retirement_age": retirement_age
        }

    # Render the results on a separate HTML page
    return render_template('results.html', results=results)

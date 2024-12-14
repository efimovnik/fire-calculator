import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.calculations import calculate_fire, savings_needed

def test_calculate_fire():
    assert calculate_fire(100000, 1500000, 2000) > 0

def test_savings_needed():
    assert savings_needed(100000, 1500000, 10) > 0

test_calculate_fire()
test_savings_needed()
print("All tests passed!")

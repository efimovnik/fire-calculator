import React, { useState } from 'react';
import InputField from './components/InputField';
import Results from './components/Results';

const App = () => {
  const [inputs, setInputs] = useState({
    currentAge: '',
    currentPortfolio: '',
    monthlySavings: '',
    fireGoal: '',
    stocksAllocation: '',
  });

  const [results, setResults] = useState({
    yearsToFire: null,
    retirementAge: null,
  });

  const parseNumber = (value) => {
    if (!value) return 0;
    return parseFloat(value.toUpperCase().replace(/,/g, '').replace(/M/, '000000').replace(/K/, '000')) || 0;
  };

  const calculateResults = () => {
    const { currentAge, currentPortfolio, monthlySavings, fireGoal } = inputs;
    const age = parseNumber(currentAge);
    const portfolio = parseNumber(currentPortfolio);
    const savings = parseNumber(monthlySavings);
    const goal = parseNumber(fireGoal);

    if (!age || !portfolio || !savings || !goal) return;

    let portfolioValue = portfolio;
    const yearlySavings = savings * 12;
    let years = 0;

    while (portfolioValue < goal) {
      portfolioValue += yearlySavings;
      portfolioValue *= 1.05; // Assume 5% annual return
      years++;
    }

    setResults({
      yearsToFire: years,
      retirementAge: age + years,
    });
  };

  const handleInputChange = (key, value) => {
    setInputs((prev) => ({ ...prev, [key]: value }));
    calculateResults();
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-center text-2xl font-bold text-gray-800 mb-6">FIRE Calculator</h1>
      <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        {Object.entries({
          currentAge: 'Current Age:',
          currentPortfolio: 'Current Portfolio:',
          monthlySavings: 'Monthly Savings:',
          fireGoal: 'FIRE Goal:',
          stocksAllocation: 'Asset Allocation (% Stocks):',
        }).map(([key, label]) => (
          <InputField
            key={key}
            label={label}
            type={key === 'stocksAllocation' ? 'number' : 'text'}
            placeholder={`Enter ${label.toLowerCase()}`}
            value={inputs[key]}
            onChange={(value) => handleInputChange(key, value)}
          />
        ))}
      </form>
      <Results {...results} />
    </div>
  );
};

export default App;

import React from 'react';

const Results = ({ yearsToFire, retirementAge }) => {
  return (
    <div className="bg-gray-200 p-4 rounded shadow-md">
      <h2 className="text-lg font-bold mb-2">Results:</h2>
      <p>Years to FIRE: <span className="font-semibold">{yearsToFire || 'N/A'}</span></p>
      <p>Projected Retirement Age: <span className="font-semibold">{retirementAge || 'N/A'}</span></p>
    </div>
  );
};

export default Results;

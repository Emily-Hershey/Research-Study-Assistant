import React from 'react';
import './index.css';

function Graph({ num_columns }) {
  const columns = Array.from({ length: num_columns }, (_, index) => (
    <div key={index} className="column">
      Column {index + 1}
    </div>
  ));

  return (
    <div className="graph">
      <h2>Graph with {num_columns} columns</h2>
      <div className="columns">
        {columns}
      </div>
    </div>
  );
}

export default Graph;
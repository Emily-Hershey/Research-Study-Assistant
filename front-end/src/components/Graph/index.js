import React from 'react';
import './index.css';

const sourceGraph = ({sources}) => {
  return (
    <div className="graph">
      <table>
        <thead>
          <tr>
            <th className={'col-topic'}>Topic</th>
            <th className={'col-link'}>Link</th>
            <th className={'col-summary'}>Summary</th>
          </tr>
        </thead>    
        <tbody>
          {sources.map((source) => (
            <tr key = {source.id}>
              <td className={'col-topic'}>{source.topic}</td>
              <td className={'col-link'}>{source.link}</td>
              <td className={'col-summary'}>{source.summary}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default sourceGraph;
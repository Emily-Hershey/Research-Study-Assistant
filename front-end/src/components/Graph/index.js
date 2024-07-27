import React from 'react';
import './index.css';
import { useQuery } from 'react-query';


const fetchData = async () => {
  try {

    console.log("gi")
    const response = await fetch("http://127.0.0.1:9000/");
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    console.log("SUCCESSly fetch")
    console.log("Data fetched:", data, "YAY");  // Check if data is fetched correctly
    return data.database
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}


function SourceGraph() {  
  /// Polling to fetch data repeatedly at regular intervals. 
  const { data, isLoading, error } = useQuery('dataKey', fetchData, {
    refetchInterval: 2000, // Poll every 2000ms
    enabled: true,
    refetchOnWindowFocus: true,
    onSuccess: (data) => {
      console.log('Data fetched successfully:', data);
    },
    
  });
  
  if (isLoading) {
    return (
      <tr>
        <td colSpan="3">Loading...</td>
      </tr>
    );
  }

  if (error) {
    return (
      <tr>
        <td colSpan="3">Error: {error.message}</td>
      </tr>
    );
  }

  return (
    <div className="graph">
      {data && data.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th className={'col-topic'}>Topic</th>
              <th className={'col-link'}>Link</th>
              <th className={'col-summary'}>Summary</th>
            </tr>
          </thead>    
          <tbody>
            {data.map((source) => (
              <tr key = {source.id}>
                <td className={'col-topic'}>{source.topic}</td>
                <td className={'col-link'}>{source.link}</td>
                <td className={'col-summary'}>
                  <textarea 
                    value={source.summary}
                    style={{ height: '100%' }}
                    readOnly
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No data available</p>
      )}
    </div>
  );
};

export default SourceGraph;
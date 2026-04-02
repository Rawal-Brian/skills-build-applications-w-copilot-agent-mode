import React, { useEffect, useState } from 'react';

const component = 'activities';

function normalizeResult(payload) {
  const result = payload?.results ?? payload;
  if (Array.isArray(result)) return result;
  if (result == null) return [];
  return [result];
}

function allKeys(items) {
  return Array.from(new Set(items.flatMap(item => Object.keys(item ?? {}))));
}

function DataTable({ items, onSelect }) {
  const columns = allKeys(items);

  if (!items.length) {
    return <div className="alert alert-secondary">No data available.</div>;
  }

  return (
    <div className="table-responsive">
      <table className="table table-striped table-hover table-bordered align-middle mb-0">
        <thead className="table-dark">
          <tr>
            <th>#</th>
            {columns.map((col) => (
              <th key={col}>{col}</th>
            ))}
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={item.id ?? item.pk ?? index}>
              <td>{index + 1}</td>
              {columns.map((col) => (
                <td key={col}>{String(item?.[col] ?? '')}</td>
              ))}
              <td>
                <button className="btn btn-sm btn-outline-primary" onClick={() => onSelect(item)}>
                  View
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function ItemModal({ item, onClose }) {
  if (!item) return null;

  return (
    <div className="modal d-block" tabIndex="-1" role="dialog" style={{ backgroundColor: 'rgba(0,0,0,0.4)' }}>
      <div className="modal-dialog modal-lg" role="document">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Item details</h5>
            <button type="button" className="btn-close" aria-label="Close" onClick={onClose}></button>
          </div>
          <div className="modal-body">
            <pre>{JSON.stringify(item, null, 2)}</pre>
          </div>
          <div className="modal-footer">
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selected, setSelected] = useState(null);

  const codespaceName = process.env.REACT_APP_CODESPACES_NAME;
  const baseURL = codespaceName ? `https://${codespaceName}-8000.app.github.dev` : (process.env.REACT_APP_API_URL || 'http://localhost:8000');
  // Codespace API URL: https://codespace-8000.app.github.dev/api/activities/
  const endpoint = `${baseURL}/api/${component}/`;

  async function fetchData() {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(endpoint);
      const json = await response.json();
      const normalized = normalizeResult(json);
      setActivities(normalized);
    } catch (err) {
      setError(err.message || 'Unknown error');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    console.log('[Activities] REST API endpoint:', endpoint);
    fetchData();
  }, [endpoint]);

  return (
    <div className="card shadow-sm mb-4">
      <div className="card-header d-flex align-items-center justify-content-between">
        <h2 className="h4 mb-0">Activities</h2>
        <button className="btn btn-sm btn-success" onClick={fetchData}>
          Refresh
        </button>
      </div>
      <div className="card-body">
        <p className="text-muted mb-1">
          Endpoint: <a href={endpoint} className="link-primary" target="_blank" rel="noreferrer">{endpoint}</a>
        </p>
        <p className="mb-3">Loaded: <strong>{activities.length}</strong> records</p>

        {error && <div className="alert alert-danger">Error: {error}</div>}

        {loading ? (
          <div className="alert alert-info">Loading data...</div>
        ) : (
          <DataTable items={activities} onSelect={setSelected} />
        )}

        <ItemModal item={selected} onClose={() => setSelected(null)} />
      </div>
    </div>
  );
}

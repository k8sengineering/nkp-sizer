import React, { useState } from 'react';

function App() {
    const [response, setResponse] = useState(null);
    const [config, setConfig] = useState({
        workload_clusters: 1,
        p2v_ratio: 1.5,
        platform_apps: [
            { name: "App 1", enabled: false, cpu: 2, memory: 4, storage: 10 },
            { name: "App 2", enabled: false, cpu: 1, memory: 2, storage: 5 }
        ]
    });

    const calculateSizing = async () => {
        const res = await fetch('/api/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(config)
        });
        const data = await res.json();
        setResponse(data);
    };

    return (
        <div>
            <h1>Nutanix NKP Sizer</h1>
            <button onClick={calculateSizing}>Calculate</button>
            {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
        </div>
    );
}

export default App;


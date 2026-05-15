import React, { useEffect, useState } from "react";

export default function App() {
  const [packets, setPackets] = useState([]);
  const [selected, setSelected] = useState(null);
  const [running, setRunning] = useState(false);

  useEffect(() => {
    const ws = new WebSocket("ws://127.0.0.1:8000/ws");

    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setPackets(prev => [data, ...prev].slice(0, 3000));
    };

    return () => ws.close();
  }, []);

  const start = async () => {
    await fetch("http://127.0.0.1:8000/start");
    setRunning(true);
  };

  const stop = async () => {
    await fetch("http://127.0.0.1:8000/stop");
    setRunning(false);
  };

  return (
    <div className="app">

      {/* HEADER */}
      <div className="header">
        <h2>NetPulse Sniffer</h2>

        <div>
          <button onClick={start} className="start">Start</button>
          <button onClick={stop} className="stop">Stop</button>
          <span className={running ? "status on" : "status off"}>
            {running ? "RUNNING" : "STOPPED"}
          </span>
        </div>
      </div>

      {/* STATS */}
      <div className="stats">
        <div>Packets: {packets.length}</div>
        <div>TCP: {packets.filter(p=>p.protocol==="TCP").length}</div>
        <div>UDP: {packets.filter(p=>p.protocol==="UDP").length}</div>
        <div>ICMP: {packets.filter(p=>p.protocol==="ICMP").length}</div>
      </div>

      {/* MAIN */}
      <div className="main">

        {/* TABLE */}
        <div className="table">
          <table>
            <thead>
              <tr>
                <th>Time</th>
                <th>Source</th>
                <th>Destination</th>
                <th>Protocol</th>
                <th>Length</th>
              </tr>
            </thead>

            <tbody>
              {packets.map((p,i)=>(
                <tr key={i} onClick={()=>setSelected(p)}>
                  <td>{p.time.slice(0,10)}</td>
                  <td>{p.src}</td>
                  <td>{p.dst}</td>
                  <td className={p.protocol}>{p.protocol}</td>
                  <td>{p.length}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* DETAILS */}
        <div className="details">
          {selected ? (
            <>
              <h3>Packet Details</h3>
              <pre>{JSON.stringify(selected,null,2)}</pre>
            </>
          ) : <h3>Select Packet</h3>}
        </div>

      </div>
    </div>
  );
}
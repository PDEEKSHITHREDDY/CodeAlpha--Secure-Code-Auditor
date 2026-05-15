import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, PieChart, Pie } from "recharts";

export default function Charts({ packets }) {
  const lineData = packets.slice(0, 20).map((p, i) => ({
    name: i,
    value: 1,
  }));

  const protocolData = Object.values(
    packets.reduce((acc, p) => {
      acc[p.protocol] = acc[p.protocol] || { name: p.protocol, value: 0 };
      acc[p.protocol].value++;
      return acc;
    }, {})
  );

  return (
    <div style={{ display: "flex", gap: 20, padding: 10 }}>
      
      <LineChart width={300} height={150} data={lineData}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Line dataKey="value" />
      </LineChart>

      <PieChart width={200} height={150}>
        <Pie data={protocolData} dataKey="value" nameKey="name" />
      </PieChart>

    </div>
  );
}
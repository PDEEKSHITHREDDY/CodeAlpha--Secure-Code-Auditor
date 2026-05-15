import React from "react";

export default function PacketTable({ packets, onSelect }) {
  return (
    <div style={{ flex: 2, overflow: "auto" }}>
      <table style={{ width: "100%", fontSize: "12px" }}>
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
          {packets.map((p, i) => (
            <tr
              key={i}
              onClick={() => onSelect(p)}
              style={{ cursor: "pointer", borderBottom: "1px solid #333" }}
            >
              <td>{p.time}</td>
              <td>{p.src}</td>
              <td>{p.dst}</td>
              <td style={{ color: getColor(p.protocol) }}>
                {p.protocol}
              </td>
              <td>{p.length}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function getColor(proto) {
  if (proto === "TCP") return "#4ade80";
  if (proto === "UDP") return "#60a5fa";
  if (proto === "ICMP") return "#facc15";
  return "white";
}
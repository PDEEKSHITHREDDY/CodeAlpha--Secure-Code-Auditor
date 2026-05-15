import React from "react";

export default function PacketDetails({ packet }) {
  if (!packet) {
    return (
      <div style={{ flex: 1, padding: 10, borderLeft: "1px solid #444" }}>
        <h3>No Packet Selected</h3>
      </div>
    );
  }

  return (
    <div style={{ flex: 1, padding: 10, borderLeft: "1px solid #444", overflow: "auto" }}>
      <h3>Packet Details</h3>

      <h4>Layers</h4>
      <pre>{JSON.stringify(packet.layers, null, 2)}</pre>

      <h4>Payload</h4>
      <pre>{packet.payload}</pre>
    </div>
  );
}
from scapy.all import AsyncSniffer, IP, TCP, UDP, ICMP, Raw

sniffer = None

def parse_packet(packet):
    if not packet.haslayer(IP):
        return None

    proto = "OTHER"
    if packet.haslayer(TCP): proto = "TCP"
    elif packet.haslayer(UDP): proto = "UDP"
    elif packet.haslayer(ICMP): proto = "ICMP"

    payload = ""
    if packet.haslayer(Raw):
        payload = str(packet[Raw].load[:100])

    return {
        "time": str(packet.time),
        "src": packet[IP].src,
        "dst": packet[IP].dst,
        "protocol": proto,
        "length": len(packet),
        "payload": payload
    }


def start_sniff(callback):
    global sniffer
    sniffer = AsyncSniffer(
        prn=lambda p: callback(parse_packet(p)) if parse_packet(p) else None,
        store=False
    )
    sniffer.start()


def stop_sniff():
    global sniffer
    if sniffer:
        sniffer.stop()
        sniffer = None
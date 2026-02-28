from scapy.all import sniff, IP, TCP

packet_limit = 10
packet_count = 0

def packet_callback(packet):
    global packet_count

    if IP in packet and TCP in packet:
        packet_count += 1
        print("=================================")
        print(f"Packet No       : {packet_count}")
        print(f"Source IP       : {packet[IP].src}")
        print(f"Destination IP  : {packet[IP].dst}")
        print(f"Protocol        : TCP")

    if packet_count >= packet_limit:
        print("\nPacket limit reached. Stopping sniffer.")
        return True   # <-- THIS STOPS sniffing

print("Sniffing 10 TCP packets only...")
sniff(filter="tcp", prn=packet_callback, store=False, stop_filter=lambda x: packet_count >= packet_limit)

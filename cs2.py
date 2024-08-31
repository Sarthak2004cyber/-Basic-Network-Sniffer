def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        # Check for TCP
        if TCP in packet:
            protocol = "TCP"
        # Check for UDP
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "Other"

        print(f"Protocol: {protocol} | Source: {ip_src} -> Destination: {ip_dst}")
def start_sniffing():
    print("Starting the sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffing()

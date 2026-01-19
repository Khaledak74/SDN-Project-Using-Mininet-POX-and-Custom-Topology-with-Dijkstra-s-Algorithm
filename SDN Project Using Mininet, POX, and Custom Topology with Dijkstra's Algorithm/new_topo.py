from mininet.topo import Topo

class CustomTopo(Topo):
    def __init__(self, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add links between hosts and switches
        self.addLink(s1, h1, **linkopts)
        self.addLink(s5, h2, **linkopts)

        # Add links between switches with different delays and bandwidths
        self.addLink(s1, s2, **linkopts_g)
        self.addLink(s1, s3, **linkopts_h)
        self.addLink(s2, s4, **linkopts_i)
        self.addLink(s4, s5, **linkopts_j)
        self.addLink(s3, s5, **linkopts_k)

# Link options with different parameters
linkopts_g = dict(delay='10ms', loss=0)
linkopts_h = dict(delay='20ms', loss=0)
linkopts_i = dict(delay='30ms', loss=0)
linkopts_j = dict(delay='40ms', loss=0)
linkopts_k = dict(delay='50ms', loss=0)
linkopts = dict(delay='0ms', loss=0)

topos = {'custom': (lambda: CustomTopo())}
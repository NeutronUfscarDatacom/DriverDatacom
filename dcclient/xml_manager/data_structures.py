""" Data structures used to build the XML
"""


class Pbits(object):
    """ Class pbits represents bitmasks (usually from ports)
    """

    _bits = 0

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, bits):
        assert type(bits) is int or type(bits) is list
        if type(bits) is int:
            self._bits = bits
        else:
            self._bits = sum([1 << (i-1) for i in set(bits)])

    @bits.deleter
    def bits(self):
        self._bits = 0

    def __init__(self, bits):
        self.bits = bits

    def as_xml(self):
        """ Method that returns the xml form of the object
        """
        return '<pbits id0="0">'+str(self.bits)+'</pbits>'


class Vlan_global(object):
    """ Class vlanglobal represents a VLan.
    """
    # TODO: adicionar checagens de limites nas properties

    _name = ''
    _vid = 0
    _ports = Pbits(0)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        assert type(name) is str
        self._name = name

    @name.deleter
    def name(self):
        self._name = ''

    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, vid):
        assert type(vid) is int
        self._vid = vid

    @vid.deleter
    def vid(self):
        self._vid = 0

    @property
    def ports(self):
        return self._ports

    @ports.setter
    def ports(self, ports):
        assert isinstance(ports, Pbits)
        self._ports = ports

    @ports.deleter
    def ports(self):
        self.ports = Pbits(0)

    def as_xml(self):
        """ Method that returns the xml form of the object
        """
        return '''
<vlan_global id0="%d">
   <vid> %d </vid>
   <active> 1 </active>
   <pbmp_untagged id="0">
      %s
   </pbmp_untagged>
</vlan_global>
''' % (self.vid,  # the vid that goes in the vlan_global array
       self.vid,  # the vid that goes in the <vid> field
       self.ports.as_xml())  # the bitmask that associate the ports


class Cfg_data(object):
    """ One class to contain them all
    """
    pass


class Interface(object):
    """ Class interface represents a switch interface
    """
    pass

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
    pass


class Cfg_data(object):
    """ One class to contain them all
    """
    pass


class Interface(object):
    """ Class interface represents a switch interface
    """
    pass

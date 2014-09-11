""" Data structures used to build the XML
"""

import xml.etree.ElementTree as ET


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
        xml = ET.Element("pbits")
        xml.attrib["id0"] = "0"
        xml.text = str(self.bits)
        return xml


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
        xml = ET.Element("vlan_global")
        xml.attrib["id0"] = str(self.vid)
        ET.SubElement(xml, "vid").text = str(self.vid)
        ET.SubElement(xml, "active").text = "1"
        pmbp_untagged = ET.SubElement(xml, "pmbp_untagged", {"id0": "0"})
        pmbp_untagged.append(self.ports.as_xml())
        return xml


class Cfg_data(object):
    """ One class to contain them all
    """
    pass


class Interface(object):
    """ Class interface represents a switch interface
    """
    pass


if __name__ == '__main__':
    vlan = Vlan_global()
    ports = Pbits([2, 3, 6])

    vlan.ports = ports

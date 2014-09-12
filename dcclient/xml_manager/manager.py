""" Methos to create and manipulate the XML
"""
import data_structures


class ManagedXml:
    def __init__(self):
        self.xml = data_structures.Cfg_data()

    def addVlan(self, vid, name='', ports=[]):
        """ This method adds a vlan to the XML an returns it's instance.
        """

        vlan = data_structures.Vlan_global(vid)

        if name:
            vlan.name = name

        if ports:
            vlan.ports = data_structures.Pbits(ports)

        self.xml.vlans.append(vlan)

        return vlan


if __name__ == '__main__':
    xml = ManagedXml()
    vlan = xml.addVlan(42, name='aaa', ports=[1, 3, 4])

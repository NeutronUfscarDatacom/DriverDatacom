""" Main class from dcclient. Manages XML interaction, as well as switch and
creates the actual networks
"""

import rpc
from xml_manager.manager import ManagedXml


from oslo.config import cfg


class Manager:
    def __init__(self):
         self.rpc = rpc.RPC(cfg.CONF.ml2_datacom.dm_username,
                         cfg.CONF.ml2_datacom.dm_password,
                         cfg.CONF.ml2_datacom.dm_host,
                         cfg.CONF.ml2_datacom.dm_method)

         self.xml = ManagedXml()

    def _update(self):
        self.rpc.send_xml(self.xml.xml.as_xml_text())

    def create_network(self, vlan):
        """ Creates a new network on the switch, if it does not exist already.
        """
        self.xml.addVlan(vlan)
        self._update()

from neutron.plugins.ml2 import driver_api as api


class DatacomMechanismDriver(api.MechanismDriver):
    """    """
    def __init__(self, rpc=None):
        pass

    def initialize(self):
        pass

    def create_network_precommit(self, context):
        """Within transaction."""

        pass

    def create_network_postcommit(self, context):
        """After transaction is done."""

        pass

    def update_network_precommit(self, context):
        """Within transaction."""

        pass

    def update_network_postcommit(self, context):
        """After transaction is done."""

        pass

    def delete_network_precommit(self, context):
        """Within transaction."""

        pass

    def delete_network_postcommit(self, context):
        """After transaction is done."""

        pass

    def create_port_precommit(self, context):
        """Within transaction."""

        pass

    def create_port_postcommit(self, context):
        """After transaction is done."""

        pass

    def update_port_precommit(self, context):
        """Within transaction."""

        pass

    def update_port_postcommit(self, context):
        """After transaction is done."""

        pass

    def delete_port_precommit(self, context):
        """Within transaction."""

        pass

    def delete_port_postcommit(self, context):
         """After transaction is done."""

       pass

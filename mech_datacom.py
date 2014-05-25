from neutron.plugins.ml2 import driver_api as api


class DatacomMechanismDriver(driver_api.MechanismDriver):
    """    """
    def __init__(self, rpc=None):
        pass
 
    def initialize(self):
        pass

    def create_network_precommit(self, context):
        """Remember the tenant, and network information."""

        pass

    def create_network_postcommit(self, context):
        """Provision the network on the Arista Hardware."""

        pass 

    def update_network_precommit(self, context):
        """At the moment we only support network name change

        Any other change in network is not supported at this time.
        We do not store the network names, therefore, no DB store
        action is performed here.
        """
        pass 

    def update_network_postcommit(self, context):
        """At the moment we only support network name change

        If network name is changed, a new network create request is
        sent to the Arista Hardware.
        """
        pass 

    def delete_network_precommit(self, context):
        """Delete the network infromation from the DB."""
        pass 

    def delete_network_postcommit(self, context):
        """Send network delete request to Arista HW."""
        pass 

    def create_port_precommit(self, context):
        """Remember the infromation about a VM and its ports

        A VM information, along with the physical host information
        is saved.
        """
        pass 

    def create_port_postcommit(self, context):
        """Plug a physical host into a network.

        Send provisioning request to Arista Hardware to plug a host
        into appropriate network.
        """
        pass 

    def update_port_precommit(self, context):
        """Update the name of a given port.

        At the moment we only support port name change.
        Any other change to port is not supported at this time.
        We do not store the port names, therefore, no DB store
        action is performed here.
        """
        pass 

    def update_port_postcommit(self, context):
        """Update the name of a given port in EOS.

        At the moment we only support port name change
        Any other change to port is not supported at this time.
        """
        pass
 
    def delete_port_precommit(self, context):
        """Delete information about a VM and host from the DB."""
        pass
 
    def delete_port_postcommit(self, context):
        pass 

    def delete_tenant(self, tenant_id):
        """delete a tenant from DB.

        A tenant is deleted only if there is no network or VM configured
        configured for this tenant.
        """
        pass 

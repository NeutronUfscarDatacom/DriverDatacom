import requests
from oslo.config import cfg
import gzip
import collections
import StringIO
import re


class RPC:
    """ RPC class. Used to connect to the client and pass the XML files.
    """
    def __init__(self):
        self.auth = (cfg.CONF.dm_username, cfg.CONF.dm_password)
        self.host = cfg.CONF.dm_host
        self.port = 80  # will be changed on production, might be added to conf

        # Create the base payload, with the common attributes
        self.base_payload = collections.OrderedDict()

        # File upload, as opposed to firmware
        self.base_payload['page'] = (
            '',
            StringIO.StringIO('file_upload'),
            'text/plain',
            {'Content-Transfer-Encoding': '8bit'}
            )

        # Flash that the startup will use
        self.base_payload['startup_upload'] = (
            '',
            StringIO.StringIO('4'),
            'text/plain',
            {'Content-Transfer-Encoding': '8bit'}
            )

        # Apply without shutting down the ports
        self.base_payload['apply_ports_up'] = (
            '',
            StringIO.StringIO('1'),
            'text/plain',
            {'Content-Transfer-Encoding': '8bit'}
            )

        # Flash in which the configuration will be saved
        self.base_payload['saving'] = (
            '',
            StringIO.StringIO('4'),
            'text/plain',
            {'Content-Transfer-Encoding': '8bit'}
            )

        # Add this configuration to the current, as opposed to overriding it
        self.base_payload['running_part'] = (
            '',
            StringIO.StringIO('1'),
            'text/plain',
            {'Content-Transfer-Encoding': '8bit'}
            )

        # Set the bounday that the switch will be expecting
        self.expected_boundary = '-oundaryboundaryboundaryboundaryBug13141'

    def send_xml(self, xml):
        """Send the XML to the switch.
        The xml has to be in plain text format
        """

        # Zipping the XML file.
        xml_gz = StringIO.StringIO()
        with gzip.GzipFile(fileobj=xml_gz, mode="w") as f:
            f.write(xml)

        # Creating the payload.
        payload = self.base_payload.copy()

        payload['file_to_upload'] = (
            'nms_config',
            xml_gz.getvalue(),
            'application/octet-stream',
            {'Content-Transfer-Encoding': 'binary'}
            )

        # Creating the request
        request = requests.Request(
            "POST",
            'https://192.168.0.13/System/File/file_config.html',
            files=payload,
            auth=('admin', 'admin')
            )

        prepared_request = request.prepare()

        # Fixing the boundary
        self.update_boundary(prepared_request, self.expected_boundary)

        # Sending the HTTP request
        session = requests.Session()
        session.send(prepared_request,  # THIS IS A SNAKEOIL WORKAROUND
                     cert=('certs/ssl-cert-snakeoil.pem',
                           'certs/ssl-cert-snakeoil.key'),
                     verify=False
                     )

    def _update_boundary(self, req, bound):
        """ Update the request with the expected boundary
        """
        current_boundary = self._get_boundary(req.headers)

        req.headers['Content-Type'] = req.headers['Content-Type'].\
            replace(current_boundary, self.expected_boundary)

        req.body = req.body.replace(current_boundary, self.expected_boundary)

    def _get_boundary(self, header):
        """ Returns the current boundary of the header
        """
        return re.findall('boundary=(.*)', header)[0]

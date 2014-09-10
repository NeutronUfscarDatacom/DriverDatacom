""" RPC class used to communicate with the hardware
"""
import pycurl
import gzip
from StringIO import StringIO as sio
from oslo.config import cfg

class RPC:
    """ RPC class. Used to connect to the client and pass the XML files.
    """
    def __init__(self):
        self.auth = self.CONF.dm_username+':'+self.CONF.dm_password
        self.host = cfg.CONF.dm_host
        self.method = cfg.CONF.method

    def _create_url(self):
        """ Internal method that returns the switches' URLs given the cfg
        attributes.
        """
        return self.method+'://'+self.auth+'@'+self.host+\
               '/System/File/file_config.html'


    def send_xml(self):
        """ Method used to send a given xml file to the switches
        """
        req = pycurl.Curl()

        #ignore ssl certificate verification
        if self.method is 'https':
            req.setopt(req.SSL_VERIFYPEER, 0)
            req.setopt(req.SSL_VERIFYHOST, 0)

        #set url being used
        req.setopt(req.URL, self._create_url())

        #oppening and zipping the xml file
        with open('teste.xml', 'r') as xml_file:
            xml_content = xml_file.read()

        ziped = sio()
        with gzip.GzipFile(fileobj=ziped, mode='w') as gzip_file:
            gzip_file.write(xml_content)

        run_data = ziped.getvalue()

        #sets necessary multipart fields and adds the zip from buffer
        data = [('page', 'file_upload'),
               ('running_part', '1'),
               ('file_to_upload', (req.FORM_BUFFER, 'upate_config',
                                  req.FORM_BUFFERPTR, run_data))]

        #sets POST method and the multipart packet
        req.setopt(req.HTTPPOST, data)

        #executes curl and exits
        req.perform()
        req.close()

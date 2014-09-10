import pycurl
import gzip
from StringIO import StringIO as sio
from urllib import urlencode
from oslo.config import cfg

class RPC:
    """ RPC class. Used to connect to the client and pass the XML files.
    """
    def __init__(self):
        self.auth = self.CONF.dm_username+':'+self.CONF.dm_password
        self.host = cfg.CONF.dm_host
        self.method = cfg.CONF.method

    def _create_url(self):
        return self.method+'://'+self.auth+'@'+self.host+\
               '/System/File/file_config.html'


    def send_xml(self, xml):
        c = pycurl.Curl()

        #ignore ssl certificate verification
        if self.method is 'https'
            c.setopt(c.SSL_VERIFYPEER, 0)
            c.setopt(c.SSL_VERIFYHOST, 0)

        #set url being used
        c.setopt(c.URL, self._create_url())

        #oppening and zipping the xml file
        with open('teste.xml', 'r') as xml_file:
            xml_content = xml_file.read()

        ziped = sio()
        with gzip.GzipFile(fileobj=ziped, mode='w') as f:
            f.write(xml_content)

        run_data = ziped.getvalue()

        #sets necessary multipart fields and adds the zip from buffer
        data = [('page', 'file_upload'),
               ('running_part', '1'),
               ('file_to_upload', (c.FORM_BUFFER, 'upate_config',
                                  c.FORM_BUFFERPTR, run_data))]

        #sets POST method and the multipart packet
        c.setopt(c.HTTPPOST, data)

        #executes curl and exits
        c.perform()
        c.close()

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

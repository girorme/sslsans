import ssl
import socket
import sys
import json
from optparse import OptionParser

def get_cert_domains(hostname, port=443):
    # Remove schema from http to prevent socket parsing error
    hostname = hostname.replace('https://', '').replace('http://', '')

    # Create a connection and fetch the certificate
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
            cert = ssl_sock.getpeercert()

    # Extract SANs from the certificate
    san_list = []
    for field in cert.get('subjectAltName', []):
        if field[0] == 'DNS':
            san_list.append(field[1])

    return san_list

parser = OptionParser(usage="usage: %prog --help")
parser.add_option("--hostname", dest="hostname",
                  help="hostname", metavar="HOSTNAME")
parser.add_option("--port", dest="port",
                  help="default: 443", metavar="PORT", type="int", default=443)
parser.add_option("--output", dest="output",
                  help="json|text", metavar="OUTPUT", default="text")

(options, args) = parser.parse_args()

if options.hostname is None:
    parser.error("Error: --hostname is required")

hostname = options.hostname
port = options.port

domains = get_cert_domains(hostname, port)

if options.output == "json":
    print(json.dumps(domains))
elif options.output == "text":
    print("\n".join(domains))
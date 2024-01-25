
import logging
import requests
from logdecorator import log_on_start, log_on_end, log_on_error, log_exception

@log_on_start(logging.DEBUG, "Start downloading {url:s}...")
@log_on_error(logging.ERROR, "Error on downloading {url:s}: {e!r}",
              on_exceptions=IOError,
              reraise=True)
@log_on_end(logging.DEBUG, "Downloading {url:s} finished successfully within {result.elapsed!s}")
def download(url):
    # some code
    response = requests.get(url)
    # some more code
    return response


logging.basicConfig(level=logging.DEBUG)

download("https://www.sighalt.de")
# DEBUG:__main__:Start downloading https://www.sighalt.de...
# DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.sighalt.de
# DEBUG:urllib3.connectionpool:https://www.sighalt.de:443 "GET / HTTP/1.1" 200 None
# DEBUG:__main__:Downloading https://www.sighalt.de finished successfully within 0:00:00.130960
#
# download("https://www.sighalt.der")
# # DEBUG:__main__:Start downloading https://www.sighalt.der...
# # DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.sighalt.der
# # ERROR:__main__:Error on downloading https://www.sighalt.der: ConnectionError(MaxRetryError("
# # HTTPSConnectionPool(host='www.sighalt.der', port=443): Max retries exceeded with url: /
# # (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7fe3fc4b5320>:
# # Failed to establish a new connection: [Errno -2] Name or service not known',))",),)
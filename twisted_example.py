import sys

from twisted.web import server
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor
from twisted.internet import endpoints


if __name__ == "__main__":
    root = Resource()
    root.putChild(b'', File('./templates/index.html'))
    root.putChild(b'static', File('./static'))
    site = server.Site(root)

    server = endpoints.serverFromString(
        reactor,
        "ssl:port=5000:privateKey=key.pem:certKey=cert.pem",
    )
    server.listen(site)
    reactor.run()

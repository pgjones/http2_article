How to serve HTTP/2 using Python
================================

This is the code to accompany an `article
<https://medium.com/@pgjones/how-to-serve-http-2-using-python-5e5bbd1e7ff1>`_,
it has simple examples for serving a simple website via HTTP/2. It
includes some bootstrap code.

Running
-------

Assuming you have at least Python 3.6, firstly to setup:

.. code-block::

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

then to run,

.. code-block::

    $ python quart_example.py
    $ python twisted_example.py

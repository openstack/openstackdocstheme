.. -*- rst -*-

This is a Test Service API Reference.

List the Servers
================

Testing API for Service 1.

**Passwords**

When you create a server, you can specify a password through the
optional adminPass attribute. The password must meet the complexity
requirements set by your OpenStack Compute provider. The server might
enter an ``ERROR`` state if the complexity requirements are not met. In
this case, a client might issue a change password action to reset the
server password.

If you do not specify a password, the API generates and assigns a random
password that it returns in the response object. This password meets the
security requirements set by the compute provider. For security reasons,
subsequent GET calls do not require this password.

**Server metadata**

You can specify custom server metadata at server launch time. The
maximum size for each metadata key-value pair is 255 bytes. The compute
provider determines the maximum number of key-value pairs for each
server. You can query this value through the ``maxServerMeta`` absolute
limit.

**Server networks**

You can specify one or more networks to which the server connects at
launch time. Users can also specify a specific port on the network or
the fixed IP address to assign to the server interface.

    **Note**

    You can use both IPv4 and IPv6 addresses as access addresses and you
    can assign both addresses simultaneously. You can update access
    addresses after you create a server.

**Server personality**

To customize the personality of a server instance, you can inject data
into its file system. For example, you might insert ssh keys, set
configuration files, or store data that you want to retrieve from inside
the instance. This customization method provides minimal launch-time
personalization. If you require significant customization, create a
custom image.

Follow these guidelines when you inject files:

-  The maximum size of the file path data is 255 bytes.

-  Encode the file contents as a Base64 string. The compute provider
   determines the maximum size of the file contents. The image that you
   use to create the server determines this value.

   .. note::

       The maximum limit refers to the number of bytes in the decoded
       data and not to the number of characters in the encoded data.

-  The ``maxPersonality`` absolute limit defines the maximum number of
   file path and content pairs that you can supply. The compute provider
   determines this value.

-  The ``maxPersonalitySize`` absolute limit is a byte limit that
   applies to all images in the deployment. Providers can set additional
   per-image personality limits.

The file injection might not occur until after the server builds and
boots.

After file injection, only system administrators can access personality
files. For example, on Linux, all files have root as the owner and the
root group as the group owner, and allow only user and group read access
(``chmod 440``).

**Server access addresses**

In a hybrid environment, the underlying implementation might not control
the IP address of a server. Instead, the access IP address might be part
of the dedicated hardware; for example, a router/NAT device. In this
case, you cannot use the addresses that the implementation provides to
access the server from outside the local LAN. Instead, the API might
assign a separate access address at creation time to provide access to
the server. This address might not be directly bound to a network
interface on the server and might not necessarily appear when you query
the server addresses. However, clients should use an access address to
access the server directly.

.. rest_method:: GET /v3/servers/{role_id}/role/{another_id}/role/{some_id}

Response
--------

.. rest_parameters:: parameters.yaml

   - host: host
   - name: name


Copy the Server
===============

Testing display of copy API.

.. rest_method:: COPY /v3/servers/{role_id}

Response
--------

.. rest_parameters:: parameters.yaml

   - host: host
   - name: name


Change or Update the Servers
============================

.. rest_method:: PUT /servers

Request
-------

.. rest_parameters:: parameters.yaml

   - name: name

Response
--------

.. rest_parameters:: parameters.yaml

   - server: server.obj
   - name: name

**Example List Servers:**

.. literalinclude:: update-server-resp.json
   :language: javascript


Delete a Server
===============

Delete some server content.

.. rest_method:: DELETE /servers/{id}

Request
-------

.. rest_parameters:: parameters.yaml

   - id: id

Response
--------

No content in body of response.

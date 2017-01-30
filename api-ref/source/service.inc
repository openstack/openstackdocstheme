.. -*- rst -*-

=========
 Service
=========

**Introductory Concepts**

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


List the Servers
================

.. rest_method:: GET /v3/servers/{role_id}/role

Short explanation about this GET method.

HTTP Status codes
-----------------

.. rest_status_code:: success status.yaml

   - 200
   - 201

.. rest_status_code:: error status.yaml

   - 400
   - 500

Response
--------

.. rest_parameters:: parameters.yaml

   - host: host
   - name: name
   - role_id: role_id


Copy the Server
===============

.. rest_method:: COPY /v3/servers/{role_id}

Short explanation about this COPY method.


Response
--------

.. rest_parameters:: parameters.yaml

   - host: host
   - name: name
   - role_id: role_id


Change or Update the Servers
============================

.. rest_method:: PUT /servers

Explantory text about this PUT method.

List of information:

- Item 1
- Item 2
- Item 3


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

.. rest_method:: DELETE /servers/{id}

Explain what the DELETE method does here.


Request
-------

.. rest_parameters:: parameters.yaml

   - id: id

Response
--------

No content in body of response.

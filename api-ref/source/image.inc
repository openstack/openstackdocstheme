.. -*- rst -*-

=======
 Image
=======

**Introductory Concepts**

When you create a server, you can specify a password through the
optional adminPass attribute. The password must meet the complexity
requirements set by your OpenStack Compute provider. The server might
enter an ``ERROR`` state if the complexity requirements are not met. In
this case, a client might issue a change password action to reset the
server password.

List the Images
===============

.. rest_method:: GET /v3/images/{role_id}/role/{another_id}/role/{some_id}<br>/b/a/x/{image_id.x}

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

Create an Image
===============

.. rest_method:: POST /images

Explantory text about this POST method.

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


Change or Update the Images
===========================

.. rest_method:: PATCH /servers

Explantory text about this PATCH method.

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


Change or Update the Images
===========================

.. rest_method:: PUT /images

Explantory text about this PUT method.

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


Delete an Image
===============

.. rest_method:: DELETE /image/{id}

Explain what the DELETE method does here.


Request
-------

.. rest_parameters:: parameters.yaml

   - id: id

Response
--------

No content in body of response.

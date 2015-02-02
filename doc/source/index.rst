==================
Demo documentation
==================

The demo documentation provides example markup for looking at the expected output.

The project aims for simple implementation, massive scalability, and a rich set
of features. Cloud computing experts from around the world contribute to the project.

Here's an example configuration::

  [DEFAULT]
  ...
  my_ip = 10.0.0.31
  vnc_enabled = True
  vncserver_listen = 0.0.0.0
  vncserver_proxyclient_address = 10.0.0.31
  novncproxy_base_url = http://controller:6080/vnc_auto.html

Here's the same example but with ..code: ini to test the pygments lexer:

.. code:: ini

  [DEFAULT]
  ...
  my_ip = 10.0.0.31
  vnc_enabled = True
  vncserver_listen = 0.0.0.0
  vncserver_proxyclient_address = 10.0.0.31
  novncproxy_base_url = http://controller:6080/vnc_auto.html

.. note:: Here's an example note.

.. toctree::
    :maxdepth: 1

    section_dashboard_access_and_security
    dashboard_demo
    configure_access_and_security_for_instances
    create_and_manage_databases

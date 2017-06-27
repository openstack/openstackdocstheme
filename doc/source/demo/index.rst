.. os-doc-demo documentation master file, created by
   sphinx-quickstart on Tue Jan 20 08:22:27 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. highlight: python
   :linenothreshold: 5

.. figure:: figures/doc-logo-fox.jpg
   :alt: Documentation Logo
   :scale: 30%
   :align: center

Demo documentation
==================

The demo documentation provides example markup for looking at the expected output.

The project aims for simple implementation, massive scalability, and a rich set
of features. Cloud computing experts from around the world contribute to the project.

Here's an example glossary:

Cactus
   An OpenStack grouped release of projects that came out in the spring of
   2011. It included Compute (nova), Object Storage (swift), and the Image
   service (glance). Cactus is a city in Texas, US and is the code name for
   the third release of OpenStack. When OpenStack releases went from three to
   six months long, the code name of the release changed to match a geography
   nearest the previous summit.

CADF
    Cloud Auditing Data Federation (CADF) is a specification for audit event
    data. CADF is supported by OpenStack Identity.

CALL
    One of the RPC primitives used by the OpenStack message queue software.
    Sends a message and waits for a response.

Here's an example configuration::

   [DEFAULT]
   ...
   my_ip = 10.0.0.31
   vnc_enabled = True
   vncserver_listen = 0.0.0.0
   vncserver_proxyclient_address = 10.0.0.31
   novncproxy_base_url = http://controller:6080/vnc_auto.html


Here's another example that's python code:

.. code-block:: python
    :linenos:

    def builder_inited(app):
        theme_dir = os.path.join(os.path.dirname(__file__), 'theme')
        app.info('Using openstack theme from %s' % theme_dir)
        # Insert our theme directory at the front of the search path and
        # force the theme setting to use the one in the package. This is
        # done here, instead of in setup(), because conf.py is read after
        # setup() runs, so if the conf contains these values the user
        # values overwrite these. That's not bad for the theme, but it
        # breaks the search path.
        app.config.html_theme_path.insert(0, theme_dir)
        # Set the theme name
        app.config.html_theme = 'openstack'
        # Re-initialize the builder, if it has the method for setting up
        # the templates and theme.
        if hasattr(app.builder, 'init_templates'):
            app.builder.init_templates()

Here's the same example but with ..code-block: ini to test the pygments lexer:

.. code-block:: ini

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
    create_and_manage_networks
    launch-instance

Search
~~~~~~

* :ref:`search`

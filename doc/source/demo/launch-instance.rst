==================
Launch an instance
==================


To access your instance remotely
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add rules to the ``default`` security group:

   a. Permit ``ICMP`` (ping):

      .. code-block:: console

         $ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
         +-------------+-----------+---------+-----------+--------------+
         | IP Protocol | From Port | To Port | IP Range  | Source Group |
         +-------------+-----------+---------+-----------+--------------+
         | icmp        | -1        | -1      | 0.0.0.0/0 |              |
         +-------------+-----------+---------+-----------+--------------+

   b. Permit secure shell (SSH) access:

      .. code-block:: console

         $ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
         +-------------+-----------+---------+-----------+--------------+
         | IP Protocol | From Port | To Port | IP Range  | Source Group |
         +-------------+-----------+---------+-----------+--------------+
         | tcp         | 22        | 22      | 0.0.0.0/0 |              |
         +-------------+-----------+---------+-----------+--------------+

2. Create a ``floating IP address`` on the ``ext-net`` external network:

   .. code-block:: console

      $ neutron floatingip-create ext-net
      Created a new floatingip:
      +---------------------+--------------------------------------+
      | Field               | Value                                |
      +---------------------+--------------------------------------+
      | fixed_ip_address    |                                      |
      | floating_ip_address | 203.0.113.102                        |
      | floating_network_id | 9bce64a3-a963-4c05-bfcd-161f708042d1 |
      | id                  | 05e36754-e7f3-46bb-9eaa-3521623b3722 |
      | port_id             |                                      |
      | router_id           |                                      |
      | status              | DOWN                                 |
      | tenant_id           | 7cf50047f8df4824bc76c2fdf66d11ec     |
      +---------------------+--------------------------------------+


Testing ordered lists and auto-numbering
----------------------------------------

#. Item 1

   #. Item 1, Item 1
   #. Item 2, Item 1

#. Item 2

   #. Item 2, Item 1

   #. Item 2, Item 2

      #. Item 2, Item 2, Item 1

      #. Item 2, Item 2, Item 2



Testing ordered lists and auto-numbering w/ note directive
----------------------------------------------------------

.. note::

   #. Item 1

      #. Item 1, nested under 1

         .. note::

            #. Item 1, nested in note under Item 1
            #. Item 2, nested in note under Item 1

      #. Item 2, nested under 1

   #. Item 2


=======================
Robotice Control Client
=======================

Python client for https://github.com/robotice/robotice-control and https://github.com/robotice/robotice

Requirements
------------

Usage as Robotice Client
------------------------

.. code-block:: python

	from roboticeclient import Client

	# listings

	client = Client(port=8004, host="127.0.0.1")

	print client.devices.list()
	print client.plans.list()
	print client.systems.list()
	print client.actions.list()

	client.actions.save(id, action)


Usage as Robotice Control Client !
----------------------------------

.. code-block:: python

	from roboticeclient import Client

	# listings

	client = Client(type="control", port=9753, host="127.0.0.1")

	print client.devices.list()
	print client.plans.list()
	print client.systems.list()
	print client.actions.list()

	client.actions.save(id, action)


Read more
---------

* http://docs.robotice.org
* http://docs.control.robotice.org
* https://github.com/robotice/robotice
* https://github.com/robotice/robotice-control
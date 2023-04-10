<h1> # Raspberry Pi: Full Cycle </h1>

**This repository contains the complete code and the steps to implements the Project Raspberry Pi:Full Cycle. **

In RPiFS an application was developed that take sensor data and make them available to the user via a web interface that is constructed based on jQuery and HTML5.

The objective of this project is to include new technologies to the Raspberry Pi:Full Stack with Raspbian(RPiFS) project, such as Django, Cloud, and to present new DevOps tools, such as Grafana and Terraform. As this project progresses, new tools may be included.

References

[1] Raspberry Pi:Full Stack with Raspbian, from Tech Explorations.
https://app.techexplorations.com/courses/raspberry-pi-full-stack-raspbian/


hire-me: https://www.linkedin.com/in/alexandre-lo-bianco-dos-santos-9541b6250/



structure:
Directory
Project: lab
App: sensors, controllers

lab_app/
├── lab/
├── sensors/
├── controllers/
└── manage.py

lab_app/
├── lab/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── sensors/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   │   ├── dht11_n1
│   │   ├── dht11_n2
│   │   ├── dht22_n1
│   │   ├── dht22_n3
│   │   ├── mq2_n1
│   │   ├── mq2_n2
│   │   ├── mq5_n1
│   │   ├── mq5_n2
│   │   ├── mq137_n1
│   │   └── mz-h19b_n1
│   ├── tests.py
│   └── views.py
├── controllers/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
<h1> Raspberry Pi Full Cycle with Django and AWS</h1>

<h2> Setup the System </h2>

<h5> Overview </h5>
<h5> Setup System </h5>
RPi base conf
Python
Python venv

<h5> Django </h5>
project:lab -> create project
lab/settings.py -> allow remote acess (ALLOWED_HOSTS = ['*'])

app:dht11 -> create app
lab/urls.py -> path to app  e import include
lab/setings.py -> include app
dht11/urls.py -> create urls.py
dht11/views.py -> create functions to render html files
dht11/templates/dht11/index.html -> html files

<h5> Django - Frontend: Basic </h5>
index.html


<h5> Django - Backend: Basic </h5>

To Do
<h6> Django - Frontend: Creating a beautifull Dashbord with AI </h6>
<h6> Django - Frontend:  </h6>
<h6> Django - Frontend:  </h6>
<h6> Django - Frontend:  </h6>
<h6> Django - Frontend:  </h6>
<h6> Django - Frontend:  </h6>
<h5> Django - Backend: RDS </h5>
<h5> Django - Backend: EC2 </h5>

This repository contains the complete code and the steps to implements the project Raspberry Pi Full Cycle(RPiFC).

In RPiFS an application was developed that take sensor data and make them available to the user via a web interface that is constructed based on Django.

The objective of this project is to include new technologies to the Raspberry Pi:Full Stack with Raspbian(RPiFS)[1] project, such as Django, Cloud, and to present new DevOps tools, such as Grafana and Terraform. As this project progresses, new tools may be included.

Raspberry Pi
Debian Buster
Python
Python venv
Adafruit
Django


References

[1] Raspberry Pi:Full Stack with Raspbian, from Tech Explorations.
https://app.techexplorations.com/courses/raspberry-pi-full-stack-raspbian/


<h2>Hire-me: https://www.linkedin.com/in/alexandre-lo-bianco-dos-santos-9541b6250/</h2>



structure:
Directory project: lab_app
Project: lab
App: sensors, controllers

lab_app
├── lab(project)
├── sensor_N(app)
├── controller_M(app)
└── manage.py

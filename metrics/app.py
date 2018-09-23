# -*- coding: utf-8 -*-

from flask import Flask
from flask_basicauth import BasicAuth
import json
import os
import psutil
psutil.PROCFS_PATH = "/proc_host"

from lib import cpu
from lib import disk
from lib import ram
from lib import service
from lib import network



application = Flask(__name__)

application.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
application.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(application)

application.config['BASIC_AUTH_FORCE'] = True


@application.route("/proc/")
def return_path():
    return psutil.PROCFS_PATH

@application.route("/hostname/")
def return_hostname():
    return "app served from {} to {}".format(socket.gethostname(), request.remote_addr)


@application.route("/")
def hello_world():
    return "Hello world"



@application.route("/hello/<string:name>")
def say_hello(name):
    return '<p>Hello <b>%s</b></p>' % name


@application.route("/metrics/cpu")
def metrics_cpu():
    return cpu.Cpu().json


@application.route("/metrics/ram")
def metrics_ram():
    return ram.Ram().json



@application.route("/metrics/disk")
def metrics_disk():
    return disk.Disk().json




@application.route("/metrics/network")
def metrics_network():
    return network.Network().json

@application.route("/metrics/services")
def metrics_services():
    return service.Service().json

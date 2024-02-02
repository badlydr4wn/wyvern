from textual import *
from environment import EnvironmentApp

APPS = [EnvironmentApp()]

def load(application_index):
    APPS[application_index].run()

def exit(application_index):
    APPS[application_index].exit()

load(0)
#!/usr/bin/python

import subprocess // subprocess is a module used for executing system commands

subprocess.call("ifconfig enp2s0 down",shell=True) // disabling interface and call is the function used
subprocess.call("ifconfig enp2s0 hw ether 00:11:22:33:44:55",shell=True)  // changing mac address
subprocess.call("ifconfig enp2s0 up",shell=True)   //enabling interface again

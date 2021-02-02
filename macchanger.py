#! /usr/bin/python

import subprocess
import optparse
import re
import pyfiglet 
  
result = pyfiglet.figlet_format("MacChanger") 
print(result + "\t\t\t\tMade by: Kirthik\n") 

class Mac_changer():
    def cmd_line(self):
        parser=optparse.OptionParser()
        parser.add_option("-i","--interface",dest="interface",help="Used to specify interface")
        parser.add_option("-m","--mac",dest="mac_address",help="Used to specify Mac Address")
        options=parser.parse_args()[0]
        if not options.interface:
            parser.error("You May Specify Your interface using -i flag......")
        elif not options.mac_address:
            parser.error("You May Specify Your New MAC using -m flag......")
        else:
            return options

    def execute(self,interface,mac):
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",mac])
        subprocess.call(["ifconfig",interface,"up"])

    def checking(self,interface,new_mac):
        check=subprocess.check_output(["ifconfig",interface])
        filtered=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",check)
        if filtered.group(0)==new_mac:
            print("MAC Address Changed To "+ new_mac)
        else:
            print("MAC Address not changed Retry Again")

mac=Mac_changer()
options=mac.cmd_line()
mac.execute(options.interface,options.mac_address)
mac.checking(options.interface,options.mac_address)


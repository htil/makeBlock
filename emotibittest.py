import argparse, time
from pythonosc import dispatcher
from pythonosc import osc_server
from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm
from typing import List, Any
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import numpy as np


dispatcherObj = dispatcher.Dispatcher()
ip = '127.0.0.1' #loopback address
port = 12345
""""
Channels from emotibit, make sure output is set OSC

			/EmotiBit/0/PPG:RED

			/EmotiBit/0/PPG:IR

			/EmotiBit/0/PPG:GRN

			/EmotiBit/0/EDA

			/EmotiBit/0/HUMIDITY

			/EmotiBit/0/ACC:X

			/EmotiBit/0/ACC:Y

			/EmotiBit/0/ACC:Z

			/EmotiBit/0/GYRO:X

			/EmotiBit/0/GYRO:Y

			/EmotiBit/0/GYRO:Z

			/EmotiBit/0/MAG:X

			/EmotiBit/0/MAG:Y

			/EmotiBit/0/MAG:Z

			/EmotiBit/0/THERM

			/EmotiBit/0/TEMP
"""
def filter_populate(address: str, *args: List[Any]) -> None:
    # Checking to make sure we get a full packet which has the channel val in it
	# then when select the val below and output it to the user
    if not len(args) == 3:
        return
           
    #PacketNUM = args[0] # packet num
    #Time_Stamp = args[1] # timestamp             
    #CHANNEL_VAL = args[2] # Channel value
    CHANNEL_VAL = args[2]
    
    

    if(address == "/EmotiBit/0/PPG:RED"):
        print("/EmotiBit/0/PPG:RED")
        print(CHANNEL_VAL)
        #print(f"RED::{len(CHANNEL_VAL)}")
        
        
    '''
    if(address == "/EmotiBit/0/PPG:IR"):
        print(CHANNEL_VAL)
        #print(f"IR::{len(CHANNEL_VAL)}")     

    if(address == "/EmotiBit/0/PPG:GRN"):
        print(CHANNEL_VAL)
        #print(f"GRN::{len(CHANNEL_VAL)}")  
    '''
    
    '''
    if(address == "/EmotiBit/0/EDA"):
        print("/EmotiBit/0/EDA")
        print(CHANNEL_VAL)
        #print(f"EDA::{len(CHANNEL_VAL)}")
    '''

def main():
    dispatcherObj.map("/EmotiBit/0/PPG:RED", filter_populate)
    dispatcherObj.map("/EmotiBit/0/PPG:IR", filter_populate)
    dispatcherObj.map("/EmotiBit/0/PPG:GRN", filter_populate)
    dispatcherObj.map("/EmotiBit/0/EDA",  filter_populate)

    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcherObj) #full block
    print("Starting server at {}".format(server.server_address))
    server.serve_forever()
    server.server_close()

if __name__=="__main__":
    main()







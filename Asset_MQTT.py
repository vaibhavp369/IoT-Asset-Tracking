import paho.mqtt.client as Asset_trackingClient
import time


IP = "broker.hivemq.com"
name = "Server_tx"
port = 1883
Subscribe_Topic = "Asset_tracking"

pre_present_asset = [] 
current_present_asset = []

Connected = False

class mqtt(object):
    def __init__(self,progress_callback,progress_msg):
        self.progress = progress_callback
        self.msg = progress_msg

    def on_connect(self,client, userdata, flags, rc):
        if rc == 0:
            #print("Connected to broker")
            self.msg.emit("Connected to broker")
            global Connected                #Use global variable
            Connected = True                #Signal connection
        else:
            self.msg.emit("Connection failed")
            #print("Connection failed",rc)

    def on_message(self,client, userdata, message):
        msgs1 = str(message.payload)
        #print(msgs1)
        self.msg.emit(msgs1)
        '''if(len(msg)>3):
            if(msg[3] == '1'):
                print("Asset_1 Present !!!")
            else:
                print("Asset_1 Absent !!!")
            if(msg[4] == '1'):
                print("Asset_2 Present !!!")
            else:
                print("Aseet_2 Absent !!!")
            if(msg[5] == '1'):
                print("Asset_3 Present !!!")
            else:
                print("Asset_3 Absent !!!")
    '''

    def initMqtt(self):
        Asset_tracking = Asset_trackingClient.Client(name)		#create a client name
        Asset_tracking.on_connect= self.on_connect                      #attach function to callback
        Asset_tracking.on_message= self.on_message                      #attach function to callback
        Asset_tracking.connect(IP,port)			#connect to broker
        Asset_tracking.loop_start()

        while Connected != True:
            time.sleep(0.1)

        Asset_tracking.subscribe(Subscribe_Topic)
        print("Subscribed...")


        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting")
            Asset_tracking.disconnect()
            Asset_tracking.loop_stop()
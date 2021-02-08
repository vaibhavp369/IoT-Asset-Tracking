
from Asset_ import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import traceback,sys
from Asset_MQTT import mqtt

Asset_1_available = False
Asset_2_available = False
Asset_3_available = False

class WorkerSignals(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
    process_msg = pyqtSignal(str)

class Worker(QThread):

    def __init__(self,fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress
        self.kwargs['progress_msg'] = self.signals.process_msg


    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class mainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		try:
			QMainWindow.__init__(self)
			self.setupUi(self)
			#self.setFixedSize(self.size())
			
			self.connectMe()
			self.startMqttThread()

		except Exception as e:
			print("init : " + str(e))

	def updateLabel1(self):
		if(Asset_1_available):
			print("Asset 1 Button Pressed")
			self.Output_lable.setText("Asset 1 available")
			#self.Asset1.setStyleSheet("background-color: lightgreen")
		else:
			self.Output_lable.setText("Asset 1 not_available")
			#self.Asset1.setStyleSheet("background-color: red")

	def updateLabel2(self):

		if(Asset_2_available):
			print("Asset 2 Button Pressed")
			self.Output_lable.setText("Asset 2 available")
			#self.Asset2.setStyleSheet("background-color: lightgreen")
		else:
			self.Output_lable.setText("Asset 2 not_available")
			#self.Asset2.setStyleSheet("background-color: red")

	def updateLabel3(self):
		if(Asset_3_available):
			print("Asset 3 Button Pressed")
			self.Output_lable.setText("Asset 3 available")
			#self.Asset3.setStyleSheet("background-color: lightgreen")
		else:
			self.Output_lable.setText("Asset 3 not_available")
			#self.Asset3.setStyleSheet("background-color: red")


	def connectMe(self):
		try:
			#print("HEllo")
			self.Asset1.clicked.connect(self.updateLabel1)
			self.Asset2.clicked.connect(self.updateLabel2)
			self.Asset3.clicked.connect(self.updateLabel3)
		except Exception as e:
			print("connectMe : "+ str(e))

	def startMqttThread(self):
		try:
			self.thread_1 = QThread()
			self.worker = Worker(fn=self.startMqtt)
			self.worker.moveToThread(self.thread_1)
			self.worker.signals.process_msg.connect(self.mqttMessage)
			self.worker.signals.result.connect(self.mqttResult)
			self.worker.signals.finished.connect(self.threadComplete)
			self.worker.start()
		except Exception as e:
			print("startMqttThread : " + str(e))


	def startMqtt(self,progress_callback,progress_msg):
		try:
			mqttObject = mqtt(progress_callback,progress_msg)
			mqttObject.initMqtt()
		except Exception as e:
			print("mqttMessage : " + str(e))


	def mqttMessage(self,data):
		global Asset_1_available,Asset_2_available,Asset_3_available
		try:
			print(data)
			print(data[3])
			if(data[3] == '1'):
				Asset_1_available = True
				self.Asset1.setStyleSheet("background-color: lightgreen")
			else:
				Asset_1_available = False
				self.Asset1.setStyleSheet("background-color: red")

			if(data[4] == '1'):
				Asset_2_available = True
				self.Asset2.setStyleSheet("background-color: lightgreen")
			else:
				Asset_2_available = False
				self.Asset2.setStyleSheet("background-color: red")

			if(data[5] == '1'):
				Asset_3_available = True
				self.Asset3.setStyleSheet("background-color: lightgreen")
			else:
				Asset_3_available = False
				self.Asset3.setStyleSheet("background-color: red")

		except Exception as e:
			print("mqttMessage : " + str(e))

	def mqttResult(self,data):
		try:
			print(data2)
		except Exception as e:
			print("mqttResult : " + str(e))

	def threadComplete(self):
		try:
			print("thread completed.")
		except Exception as e:
			print("threadComplete : " + str(e))





if (__name__ == "__main__"):
    try:
        app = QApplication(sys.argv)
        mw = mainWindow()
        mw.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)

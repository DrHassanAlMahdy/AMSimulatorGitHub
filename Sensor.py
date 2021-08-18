#!/usr/bin/python
# importing the random module

class Sensor:
	 'Class Structure for Sensor'
	 ' Constructor with zero or multiple parameter'
	 def __init__(self,arrivalTime=0,serviceTime=0,inService=0,vmID=-1):
			self.arrivalTime=arrivalTime
			self.serviceTime=serviceTime
			self.inService=inService
			self.vmID=vmID
			'Function to set sensor information'
	 def __str__(self):
		  return 'Sensor id {self.id} type{self.type} datatype {self.datatype} data {self.data} '.format(self=self)
	 def setArrivalTime(self,t):
			self.arrivalTime=t

	 def  setServiceTime(self,t):
			self.serviceTime=t

	 def setinServices(self,status):
			self.inService=status

	 def setVmID(self,ID):
			self.vmID=ID

	 def getArrivalTime(self):
			return self.arrivalTime

	 def getServiceTime(self):
			return self.serviceTime

	 def getinServices(self):
			return self.inService

	 def getVmID(self):
			return self.vmID

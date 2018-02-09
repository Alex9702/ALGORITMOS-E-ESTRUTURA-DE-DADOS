# incompleto
class LogicGate:
	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self, n, a, b):
		self.pinA = a
		self.pinB = b

	def getPinA(self):
		return int()
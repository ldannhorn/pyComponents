from gate_and import AndGate
from gate_or import OrGate
from gate_nand import NandGate
from gate_nor import NorGate
from gate_not import NotGate
from gate_xor import XorGate
from gate_xnor import XnorGate

gAnd = AndGate('gAnd')
gOr = OrGate('gOr')
gNand = NandGate('gNand')
gNor = NorGate('gNor')
gNot = NotGate('gNot')
gXor = XorGate('gXor')
gXnor = XnorGate('gXnor')

def setAllModes(mode:str):
    gAnd.setMode(mode)
    gOr.setMode(mode)
    gNand.setMode(mode)
    gNor.setMode(mode)
    gNot.setMode(mode)
    gXor.setMode(mode)
    gXnor.setMode(mode)

def printAllInfo():
    gAnd.printInfoColored()
    gOr.printInfoColored()
    gNand.printInfoColored()
    gNor.printInfoColored()
    gNot.printInfoColored()
    gXor.printInfoColored()
    gXnor.printInfoColored()

def setAllInputs(inX,inY):
    gAnd.setInput('inX', inX) ; gAnd.setInput('inY', inY)
    gOr.setInput('inX', inX) ; gOr.setInput('inY', inY)
    gNand.setInput('inX', inX) ; gNand.setInput('inY', inY)
    gNor.setInput('inX', inX) ; gNor.setInput('inY', inY)
    gNot.setInput('inX', inX) ; gNot.setInput('inY', inY)
    gXor.setInput('inX', inX) ; gXor.setInput('inY', inY)
    gXnor.setInput('inX', inX) ; gXnor.setInput('inY', inY)


print('-------------------NATIVE--------------------')

setAllModes('native')
setAllInputs(False,False)
printAllInfo()

print('---------------------------------------------')

setAllInputs(True,False)
printAllInfo()

print('---------------------------------------------')

setAllInputs(False,True)
printAllInfo()

print('---------------------------------------------')

setAllInputs(True,True)
printAllInfo()

print('-----------------TRANSISTOR------------------')

setAllModes('transistor')
setAllInputs(False,False)
printAllInfo()

print('---------------------------------------------')

setAllInputs(True,False)
printAllInfo()

print('---------------------------------------------')

setAllInputs(False,True)
printAllInfo()

print('---------------------------------------------')

setAllInputs(True,True)
printAllInfo()

print('---------------------END---------------------')
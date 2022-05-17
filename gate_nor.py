from gate_or import OrGate
from gate_not import NotGate
from gate import Gate
class NorGate(Gate):
    def __init__(self,id:str):
        self.type = 'NorGate'
        self.id = str(id)
        self.inX = False
        self.inY = False
        self.out = True
        self.mode = 'native'
        self.refresh()
    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        if self.mode == 'native':
            if self.inX or self.inY: self.out = False
            else: self.out = True
        elif self.mode == 'transistor':
            g1 = OrGate('g1'); g2 = NotGate('g2')
            g1.setMode('transistor'); g2.setMode('transistor')
            g1.setInput('inX',self.inX); g1.setInput('inY',self.inY)
            g2.setInput('inX',g1.get('out'))
            self.out = g2.get('out')
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID); state = bool(state)
        if inputID == 'inX': self.inX=state
        elif inputID == 'inY': self.inY=state
        self.refresh()
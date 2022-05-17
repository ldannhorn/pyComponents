from gate import Gate
class NotGate(Gate):
    def __init__(self,id:str):
        self.type = "NotGate"
        self.id = str(id)
        self.inX = False
        self.inY = None
        self.out = True
        self.mode = 'native'
        self.refresh()
    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        if self.mode == 'native' or self.mode == 'transistor':      ### transistor not possible at the moment
            self.mode = 'native'                                    ###
            if self.inX: self.out = False
            else: self.out = True
        elif self.mode == 'transistor':
            pass
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID); state = bool(state)
        if inputID == 'inX': self.inX=state
        elif inputID == 'inY': self.inY=state
        self.refresh()
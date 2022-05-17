class Transistor:
    def __init__(self,id:str):
        self.id = str(id)
        self.base = False
        self.collector = False
        self.emitter = False
        self.refresh()
    def refresh(self):
        if self.base and self.collector: self.emitter=True
        else: self.emitter=False
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID); state = bool(state)
        if inputID == 'base': self.base = state
        elif inputID == 'collector': self.collector = state
        self.refresh()
    def returnInfo(self):
        self.refresh()
        return ('Transistor',self.id,self.base,self.collector,self.emitter)
    def printInfo(self):
        self.refresh()
        print(f'Type: Transistor\nID: {self.id}\nBase: {self.base}\nCollector: {self.collector}\nEmitter: {self.emitter}\n')
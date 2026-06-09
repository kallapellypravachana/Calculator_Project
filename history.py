class Histroy:
    def __init__(self):
        self.records=[]
    def add(self,record):
        self.records.append(record)
    def show(self):
        for item in self.records:
           print(item) 
    def clear(self):
        self.records.clear()        

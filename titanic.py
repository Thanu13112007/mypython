class titanic:
  def __init__(self,girlfriend,boyfriend):
   self.girlfriend=girlfriend
   self.boyfriend=boyfriend 
  def love(self):
    print(self.girlfriend,self.boyfriend )
titanic1=titanic(girlfriend="rose",boyfriend ="jack")
titanic1.love()
rose jack

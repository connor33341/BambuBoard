import os
class WriteCache():
    def __init__(self,FileName,FileDir):
        self.FileName = FileName
        self.FileDir = FileDir
    def Write(self,Data):
        os.makedirs(self.FileDir,exist_ok=True)
        with open(os.path.join(os.getcwd()+self.FileDir,self.FileName),"w") as File:
            File.write(Data)
            File.close()
import threading
import http.client
from jsonRW import *
from log import log

class UpdateSystem:
    def __init__(self,AutoUpdate):
        self.AutoUpdate = AutoUpdate
        JsonClass = JsonReader("autoUpdateConfig.json")
        JsonData = JsonClass.Read()
        self.Host = JsonData["Host"]
        self.RepoPath = JsonData["RepoPath"]
        self.VersionFile = JsonData["VersionFile"]
        self.CacheName = JsonData["CacheName"]
        self.RawHost = JsonData["RawHost"]
        self.Branch = JsonData["Branch"]
    def CFU(self):
        Version = 0
        with open(self.VersionFile,"rw") as VersionFile:
            Version = int(VersionFile.read())
        RepoVersion = 0
        Connection = http.client.HTTPSConnection(self.Host)
        Connection.request("GET",self.RepoPath+self.Branch+self.VersionFile)
        Response = Connection.getresponse()
        ResponseData = Response.read().decode()
        print("[UPDATE-DBG]: Response Data: "+ResponseData)

c = UpdateSystem(True)
c.CFU()     
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
        with open(self.VersionFile,"r") as VersionFile:
            Version = int(VersionFile.read())
        RepoVersion = 0
        Connection = http.client.HTTPSConnection(self.RawHost)
        Connection.request("GET",self.RepoPath+self.Branch+self.VersionFile)
        Response = Connection.getresponse()
        ResponseData = Response.read().decode()
        RepoVersion = int(ResponseData)
        log("[UPDATE-DBG][https://"+self.RawHost+self.RepoPath+self.Branch+self.VersionFile+"]: Response Data: "+ResponseData)
        if (RepoVersion > Version):
            log("[REPO]: Outdated Version")
            if (self.AutoUpdate):
                log("[REPO]: Updating")
            else:
                log("[REPO]: Enable AutoUpdate in config.json to update")

c = UpdateSystem(True)
c.CFU()     
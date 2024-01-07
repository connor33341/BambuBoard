import threading
import http.client
from jsonRW import JsonReader,json
from log import log
from cache import WriteCache
import os
import shutil
import subprocess

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
        self.UpdateFile = JsonData["UpdateFile"]
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
                CacheControler = WriteCache("updateCache.json","/cache/")
                CacheControler.Write("")
                CurrentDir = os.getcwd()
                JsonControler1 = JsonReader("config.json")
                JsonControler2 = JsonReader(CurrentDir+"/cache/updateCache.json")
                JsonControler2.Write(JsonControler1.Read())
                ParentDir = os.path.dirname(CurrentDir)
                ActiveHeader = "ACTIVE_"
                shutil.copy(os.path.join(CurrentDir,self.UpdateFile),os.path.join(CurrentDir,ActiveHeader+self.UpdateFile))
                shutil.move(os.path.join(CurrentDir,ActiveHeader+self.UpdateFile),os.path.join(ParentDir,ActiveHeader+self.UpdateFile))
                os.chdir(ParentDir)
                subprocess.run(["python",ActiveHeader+self.UpdateFile])
            else:
                log("[REPO]: Enable AutoUpdate in config.json to update")
    def BWD(self):
        try:
            os.remove("web")
        except Exception as e:
            print("[WARN]: Dir /web does not exist")
        os.system("git clone https://github.com/t0nyz/BambuBoard.git")
        os.rename("BambuLab","web")
        JsonControler = JsonReader("config.json")
        JsonData = JsonControler.Read()
        with open("match.txt","r") as File:
            MatchLines = File.readlines()
        with open("/web/bambuConnection.js","r+") as File:
            Lines = File.readlines()
            for i in range(len(Lines)):
                for KeyWord in MatchLines:
                    if Lines[i].find(KeyWord):
                        ValueData = json.dumps(JsonData)
                        ValueData.lower()
                        ValueData = json.loads(ValueData)
                        Value = ValueData[KeyWord.lower()]
                        Lines[i] = "const "+KeyWord+" = "+Value+";"
            File.writelines(Lines)
                

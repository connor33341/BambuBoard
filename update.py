import threading
import http.client
from jsonRW import JsonReader
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
    
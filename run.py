#Copyright© 2019 By Fajar Firdaus
#Please don't Recode My Program Because i take a long time to complete this project :)

import urllib3 as url
import json as js
import os
import os.path
import time
import os.path

class Get:

    def banner():
         print("     .---. ")
         print("     |---| ")
         print("     |---| ")
         print("     |---| ")
         print(" .---^ - ^---. ")
         print(" :___________: ")
         print("    |  |//|  ")
         print("    |  |//|     ")
         print("    |  |//| ")
         print("    |  |//| [Take All Repo] ")
         print("    |  |//|      [By]")
         print("    |  |//| [Fajar Firdaus] ")
         print("    |  |.-|  ")
         print("    |.-'**|  ")
         print("     \***/  ")
         print("      \*/   ")
         print("       V    ")
    
    def page():
        account = str(input("[?] Input Account Name >_ "))
        user = str(input("[?] Input Page >_ "))
        agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
        u = url.PoolManager(headers=agent)
        data = u.request("GET", "https://api.github.com/users/" + account + "/repos?page=" + user)

        result = js.loads(data.data)
        
        for loop in range(30):
            os.system("git clone " + result[loop]['clone_url'])


run = Get.banner()
run = Get.page()
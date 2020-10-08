import requests
import os
import re

def loadFileContent(downloadUrl) :
    return requests.get(downloadUrl).text

def writeFile(content):
    file = './execute.py'
    with open(file, 'w', encoding='utf-8') as f: f.write(content.replace('\r\n','\n'))

print("\n同步文件中...")
webFileContent = loadFileContent(os.environ["SYNCURL"])
print("\n文件同步完毕, 处理中...")
xmly_speed_cookie = os.environ["XMLY_SPEED_COOKIE"]
agentPattern = re.compile(r'UserAgent = \"[\d\D]+\"')
for line in xmly_speed_cookie.split('\n'):
    executeContent = webFileContent.replace('xmly_speed_cookie = os.environ["XMLY_SPEED_COOKIE"]','xmly_speed_cookie = "' + line + '"',1)
    if line.find("_device=android")>0:#此时表示是获取的安卓的cookie,需要使用安卓的agent
        rewriteAgent = os.environ["XMLY_ANDROID_AGENT"]
        if len(rewriteAgent) ==0 or rewriteAgent.strip()=='':
            rewriteAgent='UserAgent = "ting_1.8.30(Redmi+7,Android28)"'
            executeContent = re.sub(agentPattern,rewriteAgent,executeContent)
    writeFile(executeContent)
    print("\n文件处理安卓Agent完毕，执行中...")
    os.system('python ./execute.py')
    print("\n文件执行完毕\n\n")
print("\n***************************\n文件全部执行完毕")
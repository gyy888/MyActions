import requests
import os

def loadFileContent(downloadUrl) :
    return requests.get(downloadUrl).text

def writeFile(content):
    file = './execute.py'
    # print(content)
    with open(file, 'w', encoding='utf-8') as f: f.write(content.replace('\r\n','\n'))

print("\n加载文件中...")
writeFile(loadFileContent(os.environ["SYNCURL"]))
print("\n文件加载完毕，执行中...")
os.system('python ./execute.py')

import re
agentPattern = re.compile('UserAgent = \"[\d\D]+\"',re.S)
content= 'UserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iting/1.0.12 kdtunion_iting/1.0 iting(main)/1.0.12/ios_1"\n# '
rewriteAgent='UserAgent = "ting_1.8.30(Redmi+7,Android28)"'
testContent = re.sub(agentPattern,rewriteAgent,content)
print(testContent)
import urllib.request
import math
from bs4 import BeautifulSoup

print('Enter github username: ')
username = str(input())

urle = 'https://github.com/'+str(username)+'?tab=stars'
page = urllib.request.urlopen(urle)
soup = BeautifulSoup(page, 'html.parser')
x = str(soup.encode_contents())
counterstars = str(soup.encode_contents())
counterstars = counterstars.strip().replace(' ','')
counterstars = counterstars.strip().replace('\\n','')
counterstars = counterstars.split('href="/'+str(username)+'?tab=stars"')[1].split('<span class="Counter">')[0].split('role="tab">Stars<spanclass="Counter">')[1].split('</span></a><aaria-selected="false"class="underline-nav-item"href="/'+str(username)+'?tab=followers')
countingstars = int(counterstars[0]) + 30
countingstars = math.ceil((countingstars - 30)/30)
ro= open('roro.txt','w')
ro.write('Number | Check | Repository | Description |\n')
ro.write('----- | ----- | ----- | -----|\n')
counterrr = 0
for j in range(0,int(countingstars)):
    urle = 'https://github.com/'+username+'?page='+str(j+1)+'&tab=stars'
    page = urllib.request.urlopen(urle)
    soup = BeautifulSoup(page, 'html.parser')
    x = str(soup.encode_contents())
    x= x.replace('\\n','')
    x = x.replace('ios-version="6.0">' ,' >')
    x = x.split('class=\"position-relative\"')
    x = x[1]
    listofblocks = x.split('<div class="col-12 d-block width-full py-4 border-bottom">')
    for i in range(0,len(listofblocks)):
        if i >= 1:
            ro.write('| ' + str(counterrr) +'. | <ul style="list-style-type:none"><li> [ ] </li></ul> | ')
            counterrr += 1
            a = listofblocks[i].split('<a href="')
            b = a[1].split('">')
            ro.write('['+ b[0] +']' + '(' + 'https://github.com' + b[0] + ') | ')
            n = b[8].split('</p>')
            if n[0].strip() is '<span class="repo-language-color ml-0" style="background-color:#3572A5;':
                ro.write('No Description | \n')
            else:
                res = n[0].strip()
                res = res.strip().replace('\\n','')
                res = res.strip().replace('  ','')
                ro.write( res + ' | \n' )

ro.close()

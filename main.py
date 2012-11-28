
import urllib2
import getpass
import cairoplot, math, random
import urllib2
from urlparse import urlparse, urlunparse
import ntlm
from ntlm import HTTPNtlmAuthHandler 
import os
import sys
import cairoplot
import ConfigParser
from plotter import *
import plotter

from BeautifulSoup import BeautifulSoup
def readConfig(task=None,domain=None,uname=None,pwd=None,url=None):

    Config = ConfigParser.ConfigParser()
    Config.read("test.conf")
    print Config.sections()
    dict =ConfigSectionMap(Config,ConfigSectionMap(Config,'Site')['usesite'])
    print "Using configuration:",ConfigSectionMap(Config,'Site')['usesite']
    for key in dict.keys():
        if key == 'task':
            task=dict[key]
        if key == 'domain':
            domain=dict[key]
        if key == 'username':
            uname=dict[key]
        if key == 'password':
            pwd=dict[key]
        if key == 'url':
            url=dict[key]            
    return readLoginData(task,domain,uname,pwd,url)
def ConfigSectionMap(Config,section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
def readLoginData(task=None,domain=None,uname=None,pwd=None,url=None):
    if task == None:
        task    = raw_input("Enter Task id  :")
    if domain==None:
        domain  = raw_input("Enter Domain   :")
    if uname == None:
        uname   = raw_input("Enter Username :")
    if pwd == None:
        pwd     = getpass.getpass('Enter password :')
    if url == None:
        url     = raw_input('Enter URL      :')
    return task,domain,uname,pwd,url
        
def login(url, username, password):
    parsed_url = urlparse(url)
    base_uri = urlunparse((parsed_url[0],parsed_url[1],"","","",""))
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, base_uri, username, password)
    auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
    auth_basic = urllib2.HTTPBasicAuthHandler(passman)
    auth_digest = urllib2.HTTPDigestAuthHandler(passman)
    proxy_handler = urllib2.ProxyHandler({})

    opener = urllib2.build_opener(proxy_handler, auth_NTLM, auth_digest, auth_basic)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url) 
    return response.read()

def main(task="3773"):

    if os.path.isfile('test.conf'):
        (task,domain,uname,pwd,url)=readConfig()
    else:
        (task,domain,uname,pwd,url)=readLoginData()
    url="https://"+url+"/activity/printactivity.aspx?id="+task
    uname = '%s\%s' % (domain,uname)
    data=login(url,uname,pwd)
    print "data got"
    soup = BeautifulSoup(data)
    print "soupified"
    sres=    [ [ col.renderContents() for col in row.findAll('td') ]
             for row in soup.find('table',id="tbl_all").findAll('tr') ]
    del sres[0]
    del sres[0]
    del sres[-1]
    res = []
    for row in sres:
        aY=0
        aN=0	
        aNA=0
        found=False
        name=row[1].replace('&nbsp','')
        answer=row[2]+row[3]
        answer=answer.replace('&nbsp;','')
        if answer=='Y':
            aY=1
        elif answer=='N':
            aN=1
        else:
            aNA=1
                
        for group in res:
          if name == group[0]:
            found=True
        if found == False:
          res.append([name,0,0,0,0])
        for group in res:
            if name == group[0]:
              group[1] += aY
              group[2] += aN
              group[3] += aNA
              group[4] += aY +aN +aNA
    totalPlot(res)      
    totalComming(res)
    groupPie(res)
            
        
if __name__ == "__main__":
    main()
 


        
        
    

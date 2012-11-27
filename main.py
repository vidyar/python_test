
import urllib2
import getpass
import cairo, math, random
import urllib2
from urlparse import urlparse, urlunparse
import ntlm
from ntlm import HTTPNtlmAuthHandler 
import os
import sys
import cairoplot

from BeautifulSoup import BeautifulSoup

        
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
    task    = getpass.getpass('Enter Task id  :')
    domain  = getpass.getpass('Enter Domain   :')
    uname   = getpass.getpass('Enter Username :')
    pwd     = getpass.getpass('Enter password :')
    url     = getpass.getpass('Enter URL :')
    url="https://"+url+"/activity/printactivity.aspx?id="+task
    uname = '%s\%s' % (domain,uname)
    data=login(url,uname,pwd)
    soup = BeautifulSoup(data)
    res=    [ [ col.renderContents() for col in row.findAll('td') ]
             for row in soup.find('table',id="tbl_all").findAll('tr') ]
    del res[0]
    del res[0]
    del res[-1]
    print res
    



def testPlot():
        #Stack horizontal
    #Stack vertical
    data = { 'teste00' : [27,13], 'teste01' : [10,20], 'teste02' : [18,12], 'teste03' : [5,25], 'teste04' : [1,29], 'teste05' : [22,8] }
    colorGreen = (0,1,0)
    colorRed = (1,0,0)
    colorYellow=(1,1,0.0)
    colors = [ colorGreen, colorRed,  colorYellow]
    cairoplot.vertical_bar_plot ( 'vbar_0_dictionary.svg', data, 400, 300, border = 20, display_values = True, grid = True, rounded_corners = True, stack=True,colors = colors )
    
    
    
        
        
if __name__ == "__main__":
    main()
 


        
        
    
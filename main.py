
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
import htmldata
from login import login



def main(task="3773"):
    task    = getpass.getpass('Enter Task id  :')
    domain  = getpass.getpass('Enter Domain   :')
    uname   = getpass.getpass('Enter Username :')
    pwd     = getpass.getpass('Enter password :')
    url     = getpass.getpass('Enter URL :')
    url="https://intranet.hiq.se/activity/printactivity.aspx?id="+task
    uname = '%s\%s' % (domain,uname)
    data=login(url,uname,pwd)
    data=data.split("table")
    print data[1]

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
 


        
        
    
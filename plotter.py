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
colorGreen = (0,1,0)
colorRed = (1,0,0)
colorYellow=(1,1,0.0)  
def totalPlot(res,plotFileName='PercentCommingAllGroups.svg'):


    data = []
    plotName = []
    for rec in res:
      data.append([100*rec[1]/rec[4],100*rec[2]/rec[4],100*rec[3]/rec[4]])
      plotName.append(rec[0])
    colors = [ colorGreen, colorRed,  colorYellow]
    cairoplot.vertical_bar_plot ( plotFileName, data, 1920, 1080, border = 20, grid = True, rounded_corners = True, stack=True,colors = colors, x_labels=plotName, three_dimension = True )
    print "wrote",plotFileName
    
def totalComming(res,plotFileName='TotalCommingAllGroups.svg'):
    data = dict()
    plotName = []
    for roc in res:
        data[roc[0]] = roc[1]
    cairoplot.pie_plot(plotFileName, data, 1920, 1080)
    print "wrote",plotFileName
    
def groupPieWorker(name,data,groupStats='Statistics.svg'):
    plotFileName = name + groupStats
  
    colors = [colorRed, colorYellow ,  colorGreen]
    cairoplot.pie_plot(plotFileName, data, 1920, 1080,colors = colors)
    print "wrote",plotFileName


def groupPie(res):
    for rec in res:
        d=dict()
        d['Yes'] = rec[1]
        d['No'] = rec[2]
        d['No reply'] = rec[3]       
        groupPieWorker(rec[0],d)


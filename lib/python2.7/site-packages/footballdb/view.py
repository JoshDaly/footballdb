#!/usr/bin/python
###############################################################################
#                                                                             #
#    view.py                                                                  #
#                                                                             #
#    suite of visualisations available for FootballDB                         #
#                                                                             #
#    Copyright (C) Josh Daly                                                  #
#                                                                             #
###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

__author__ = "Josh Daly"
__copyright__ = "Copyright 2015"
__credits__ = ["Josh Daly"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Josh Daly"
__email__ = "joshua.daly@uqconnect.edu.au"
__status__ = "Dev"

###############################################################################
###############################################################################
###############################################################################
###############################################################################

# system imports
import numpy as np
import matplotlib.pyplot as plt

# local imports

###############################################################################
###############################################################################
###############################################################################
###############################################################################

class View(object):
    def __init__(self):
        pass
    
    def visualisePlayerStats(self,
                             playerData,
                             sortedPlayerData):
        fig = plt.figure()
        ax  = plt.subplot(1,1,1)
        
        # calculate the number of data points
        ind, ys = self.numDataPoints(playerData,
                                    sortedPlayerData)
        
        ax.bar(ind, ys, 0.35)
        plt.show()
        
    def numDataPoints(self,
                      playerData,
                      sortedPlayerData):
        N  = 0
        ys = []
        for data in sortedPlayerData:
            season = data[0]
            N += len(playerData[season])
            for week in data[1].keys():
                stat = data[1][week]
                ys.append(stat)
        ind = np.arange(N)
        return ind, ys
    
    def visualiseTeamStats(self):
        pass
    
    def compareStats(self, type, ):
        pass
    
    
    def visualiseTable(self, orderedTable, tableData, season):
        """visualise table using blank scatter plot"""
        fig     = plt.figure(figsize=(8, 2),dpi=400)
        ax      = plt.subplot(1,1,1)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        tableHeaders = ['teams','wins', 'draws', 'losses',
                        'goalsFor','goalsAgainst',
                        'byes','forfeitWins',
                        'forfeitLosses','points',
                        'bonusPoints']
        
        data = []
        
        # print header
        header_to_print = "\t".join(tableHeaders)
        print "###########################################################"
        print "-----------Brisbane City Indoor Sports Season %d-----------" % season
        print "###########################################################"
        print header_to_print
        
        # print table
        for team in orderedTable:
            array = [team[0]]
            data_to_print = team[0]
            for header in tableHeaders[1:]:
                #array.append(tableData[team[0]][header])
                data_to_print += "\t%s" % str(tableData[team[0]][header])
            data.append(array)
            print data_to_print
        
        print "###########################################################"
        print "###########################################################"
        
        # Need to find better table out format
        #table = ax.table(cellText=data,
        #                 colLabels=tableHeaders,
        #                 loc='center'
        #                 )
        
        #plt.savefig('tmp', type='png')
        
        
        
        
    
    
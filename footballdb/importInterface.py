#!/usr/bin/python
###############################################################################
#                                                                             #
#    importInterface.py                                                       #
#                                                                             #
#    Interface for importing data stored in csv files into the FootballDB DB  #
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
import sys
#sys.path.insert(0, "/home/josh/working/sw/footballdb/footballdb")

# local imports
from dancingPeasant.exceptions import *
from dancingPeasant.interface import Interface
from dancingPeasant.interface import Condition
from db import FootballDB

###############################################################################
###############################################################################
###############################################################################
###############################################################################

class ImportInterface(Interface):
    """Use this interface for importing data stored in csv
    files into the FootballDB DB"""
    def __init__(self,
                 dbFileName,        # file name to connect to
                 verbosity=-1       # turn off all DP chatter
                 ):
        Interface.__init__(self, dbFileName, verbosity)
        self.db = FootballDB(verbosity=verbosity)            # <-- This line is important!
        self.dbFileName = dbFileName
    
    def importGameData(self,
                       gameDataCSV,     # file containing data 
                       opposition,      # string of opposition team
                       season,          # int of season number
                       week):           # int of week in season
        """import new game data into the FootballDB
           Create new DB if it doesn't exist!"""
         
        if not self.connect(createDB=True):
            # database exists
            pass
        else:
            # if True, database has been created!
            print "Database %s created" % self.dbFileName
        
        to_db = {}
        
        # add game data to DB
        self.convertFileIntoArray(gameDataCSV,
                                  opposition,
                                  season,
                                  week,
                                  to_db)
        
        to_db = [(0,8,5,0,1,0,7,1,4,0,47,40,1,11,5,6,0)]
        
        self.insert("ron",["goals","shots_attempted","shots_on_target","assists",
                          "tackles","intercepts","gk_saves","fouls_committed",
                          "fouls_suffered","blocked_shots","passes_attempted",
                          "passes_successful","subbed","attacking_passes_attempted",
                          "attacking_passes_successful","turnovers","deflected_passes"], to_db)
        
        #for player in to_db.keys():
        #    print player
        #    data_to_db = to_db[player]
        #    self.insert("%s" % player, ["goals","shots_attempted","shots_on_target","assists",
        #                                "tackles","intercepts","gk_saves","fouls_committed",
        #                                "fouls_suffered","blocked_shots","passes_attempted",
        #                                "passes_successful","subbed","attacking_passes_attempted",
        #                                "attacking_passes_successful","turnovers","deflected_passes"],data_to_db)
        
        self.disconnect()
    
    def convertFileIntoArray(self,
                             gameDataCSV,
                             opposition,
                             season,
                             week,
                             to_db):
        
        with open(gameDataCSV) as fh:
            for l in fh:
                tabs = l.rstrip().split("\t")
                
                # skip header
                if tabs[0].lower() != 'player':
                    player                      = tabs[0]
                    goals                       = tabs[1]
                    shots_attempted             = tabs[2]
                    shots_on_target             = tabs[3]
                    assists                     = tabs[4]
                    tackles                     = tabs[5]
                    intercepts                  = tabs[6]
                    gk_saves                    = tabs[7]
                    fouls_committed             = tabs[8]
                    fouls_suffered              = tabs[9]
                    blocked_shots               = tabs[10]
                    passes_attempted            = tabs[11]
                    passes_successful           = tabs[12]
                    subbed                      = tabs[13]
                    attacking_passes_attempted  = tabs[14]
                    attacking_passes_successful = tabs[15]
                    turnovers                   = tabs[16]
                    deflected_passes            = tabs[17]

                    to_db[player] = [(goals,shots_attempted,shots_on_target,assists,tackles,
                                    intercepts,gk_saves,fouls_committed,fouls_suffered,
                                    blocked_shots,passes_attempted,passes_successful,subbed,
                                    attacking_passes_attempted,attacking_passes_successful,turnovers,deflected_passes)]
                    
    def addBars(self):
        """Add bars to the database"""
        if not self.connect(createDB=True):
            # database exists
            pass
        else:
            # if True, database has been created!
            print "Database %s created" % self.dbFileName
        
        # connect to the database
        #self.connect()
    
        # bars is an array of tuples. All ordered in the same way
        # EX:
        bars =  [(10, 1, "iron"), (20, 15, "wax")]
        #
        self.insert("bam",
                    ["length",
                     "diameter",
                     "material"],
                     bars)
    
        # disconnect once done
        self.disconnect()
    
    def getBars(self, length):
        """Get bars longer than a set length"""
    
        # connect to the database
        self.connect()
    
        # set the select condition
        C = Condition("length", ">", length)
    
        # access the database and get rows
        rows = self.select('bars', ["material", "diameter"], C)
    
        # disconnect once done
        self.disconnect()
    
        # do something with the results
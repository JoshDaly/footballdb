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
from footballdb.db import FootballDB

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
        self.db = FooDB(verbosity=verbosity)            # <-- This line is important!
        self.dbFileName = dbFileName
    
    def importGameData(self,
                       gameDataCSV,     # file containing data 
                       opposition,      # string of opposition team
                       season,          # int of season number
                       week):           # int of week in season
        """import new game data into the FootballDB"""
        if not self.connect(createDB=True):
            # database exists
            print 'Database already exists!'
        else:
            # if True = database has been created!
            print "Database %s created" % self.dbFileName
        
        self.disconnect()
    
    def addBars(self, bars):
        """Add bars to the database"""
        # connect to the database
        self.connect()
    
        # bars is an array of tuples. All ordered in the same way
        # EX:
        # [(10, 1, "iron"), (20, 15, "wax"), ... ]
        #
        self.insert("bars",
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
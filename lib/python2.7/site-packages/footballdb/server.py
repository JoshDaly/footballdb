#!/usr/bin/python
###############################################################################
#                                                                             #
#    server.py                                                                #
#                                                                             #
#    Main entry point for the footballdb software                             #
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
from footballdb.importInterface import ImportInterface

###############################################################################
###############################################################################
###############################################################################
###############################################################################

class Server(object):
    def __init__(self,
                 dbfilename         # path to db file to work with
                 ):
        self.dbfilename = dbfilename
        
    def importGameStats(self,
                        gameStatsFile,  # csv containing game statistics
                        opposition,     # opposition team name
                        season,         # season number
                        week            # week number
                        ):
        print "Importing new game data for Week %d of Season %d against %s" % (week,
                                                                               season,
                                                                               opposition)
        # get an interface to the file
        II = ImportInterface(self.dbFileName)
        
        # import game stats as csv file
        II.importGameData(gameStatsFile,
                          opposition,
                          season,
                          week)
    
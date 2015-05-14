#!/usr/bin/python
###############################################################################
#                                                                             #
#    db.py                                                                    #
#                                                                             #
#    Controls interactions with database file                                 #
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

__FOOTBALLDB_DB_VERSION__ = "0.1.0"

###############################################################################
###############################################################################
###############################################################################
###############################################################################

# system imports
import sys
#sys.path.insert(0, "/home/josh/working/sw/footballdb/footballdb")

# local imports
from dancingPeasant.baseFile import BaseFile
from dancingPeasant.exceptions import *

###############################################################################
###############################################################################
###############################################################################
###############################################################################



class FootballDB(BaseFile):
    def __init__(self, verbosity=0):
        BaseFile.__init__(self, verbosity)

    def createNewFile(self,
                      fileName,             # name of the new file
                      force=False,          # should we check to see if this is a wise move?
                      ):
        """Create a new FootballDB database file"""
        
        # make a basic file
        BaseFile.createNewFile(self,
                               fileName,
                               type="FootballDB_DB",
                               version=__FOOTBALLDB_DB_VERSION__,
                               force=force)
        
        self._addTable('results',
                       {
                        "season" : "INT",
                        "week" : "INT",
                        "team_a" : "TEXT",
                        "team_b" : "TEXT",
                        "score_a" : "INT",
                        "score_b" : "INT",
                       },
                       force=True)
        
    def addNewPlayer(self, player):
        """Add new player table to present Database"""
        # check if table already exists for player
        
        self._addTable(player,
                       {
                        "season" : "INT",
                        "week" : "INT",
                        "opposition" : "TEXT",
                        "goals" : "INT",
                        "shots_attempted" : "INT",
                        "shots_on_target" : "INT",
                        "assists" : "INT",
                        "tackles" : "INT",
                        "intercepts" : "INT",
                        "gk_saves" : "INT",
                        "fouls_committed" : "INT",
                        "fouls_suffered" : "INT",
                        "blocked_shots" : "INT",
                        "passes_attempted" : "INT",
                        "passes_successful" : "INT",
                        "subbed" : "INT",
                        "attacking_passes_attempted" : "INT",
                        "attacking_passes_successful" : "INT",
                        "turnovers" : "INT",
                        "deflected_passes" : "INT"
                       },
                       force=True)
        
    
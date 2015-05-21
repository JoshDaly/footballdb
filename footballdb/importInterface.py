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
import sqlite3 as lite
import operator

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
    
    def importGameStats(self,
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
        
        # add game data to DB
        self.convertFileIntoArray(gameDataCSV,
                                opposition,
                                season,
                                week
                                )
        
        self.disconnect()
    
    def convertFileIntoArray(self,
                             gameDataCSV,
                             opposition,
                             season,
                             week
                             ):
        
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

                    to_db = [(season, week, opposition, goals,shots_attempted,shots_on_target,assists,tackles,
                            intercepts,gk_saves,fouls_committed,fouls_suffered,
                            blocked_shots,passes_attempted,passes_successful,subbed,
                            attacking_passes_attempted,attacking_passes_successful,turnovers,deflected_passes)]
                    
                    # check to see if table exists, if not, create it!
                    #self.db.addNewPlayer(player)
                    if self.doesPlayerTableExist(player):
                        # insert data into table
                        self.insert(player,
                                    [
                                    "season","week","opposition","goals","shots_attempted",
                                    "shots_on_target","assists","tackles","intercepts",
                                    "gk_saves","fouls_committed","fouls_suffered",
                                    "blocked_shots","passes_attempted","passes_successful",
                                    "subbed","attacking_passes_attempted","attacking_passes_successful",
                                    "turnovers","deflected_passes"
                                    ],
                                    to_db)
                    else:
                        print "Adding new player (%s) table to %s" % (player, self.dbFileName)
                         # create table
                        self.db.addNewPlayer(player)
                        
                        # then add data
                        self.insert(player,
                                    [
                                    "season","week","opposition","goals","shots_attempted",
                                    "shots_on_target","assists","tackles","intercepts",
                                    "gk_saves","fouls_committed","fouls_suffered",
                                    "blocked_shots","passes_attempted","passes_successful",
                                    "subbed","attacking_passes_attempted","attacking_passes_successful",
                                    "turnovers","deflected_passes"
                                    ],
                                    to_db)
                    
    def doesPlayerTableExist(self, player):
        try:
            table_data = self.select(player, "*")
            return True
        except(lite.OperationalError):
            return False

    def insertData(self, ):
        pass
    
    
    def importResults(self,
                      resultsDataFile,
                      season,
                      week
                      ):
        """Import the results for the round into the ladder DB.
           Create new database if it doesn't already exist!"""
        
        if not self.connect(createDB=True):
            # database exists
            pass
        else:
            # if True, database has been created!
            print "Database %s created" % self.dbFileName
    
        # add round results to DB
        self.addRoundResults(resultsDataFile,
                             season,
                             week)
        
        self.disconnect()
    
    
    def addRoundResults(self,
                        resultsDataFile,
                        season,
                        week):
        # table already exists, created with the database!
        with open(resultsDataFile) as fh:
            for l in fh:
                tabs        = l.rstrip().split("\t")
                team_a      = tabs[0]
                team_b      = tabs[1]
                score_a     = tabs[2]
                score_b     = tabs[3]
                
                to_db = [(season, week, team_a, team_b, score_a, score_b)]
        
                self.insert('results',
                            [
                             "season",
                             "week",
                             "team_a",
                             "team_b",
                             "score_a",
                             "score_b"
                             ],
                            to_db)
                
    def viewTable(self,
                  season):
        # view table for specified season
        tableData = {}
        # connect to database
        self.connect()
        
        # set the select condition
        C = Condition("season", "=", season)
        
        # access the database and get rows
        rows = self.select('results', ["week","team_a","team_b","score_a","score_b"], C)
        
        # disconnect once done
        self.disconnect()
        
        for row in rows:
            week    = int(row[0])
            team_a  = row[1]
            team_b  = row[2]
            score_a = row[3]
            score_b = row[4]
            
            # initialise team
            self.initialiseTeam(tableData,team_a)
            self.initialiseTeam(tableData,team_b)
            
            # add data to dictionary
            self.prepareData(tableData, team_a, team_b, score_a, score_b)
            
        sorted_table = sorted(tableData.items(), key=lambda x:x[1]['points'],reverse=True)
        
        for teamData in sorted_table:
            team = teamData[0]
            print team, tableData[team]
        
            
    def initialiseTeam(self, tableData, team):
        if team not in tableData and team!= 'bye':
            tableData[team] = {}
            tableData[team]['goalsFor']         = 0
            tableData[team]['goalsAgainst']     = 0
            tableData[team]['wins']             = 0
            tableData[team]['losses']           = 0
            tableData[team]['draws']            = 0
            tableData[team]['byes']             = 0
            tableData[team]['forfeitWins']      = 0
            tableData[team]['forfeitLosses']    = 0
            tableData[team]['points']           = 0
            tableData[team]['bonusPoints']      = 0
    
    def prepareData(self, tableData, team_a, team_b, score_a, score_b):
        # check if bye
        if self.isBye(team_a,team_b):
            if team_a == 'bye':
                self.addDataToTable(tableData,
                                    team_b,
                                    goalsFor=0,
                                    goalsAgainst=0,
                                    wins=0,
                                    losses=0,
                                    draws=0,
                                    byes=1,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=0,
                                    bonusPoints=0)
            elif team_b == 'bye':
                self.addDataToTable(tableData,
                                    team_a,
                                    goalsFor=0,
                                    goalsAgainst=0,
                                    wins=0,
                                    losses=0,
                                    draws=0,
                                    byes=1,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=0,
                                    bonusPoints=0)
        
        # check if forfeit
        elif self.isForfeit(score_a, score_b):
            if score_a == 'FW':
                self.addDataToTable(tableData,
                                    team_a,
                                    goalsFor=0,
                                    goalsAgainst=0,
                                    wins=0,
                                    losses=0,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=1,
                                    forfeitLosses=0,
                                    points=4,
                                    bonusPoints=0)
                self.addDataToTable(tableData,
                                    team_b,
                                    goalsFor=0,
                                    goalsAgainst=0,
                                    wins=0,
                                    losses=0,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=1,
                                    points=0,
                                    bonusPoints=0)
            elif score_b == 'FW':
                self.addDataToTable(tableData,
                                    team_b,
                                    goalsFor=0,
                                    goalsAgainst=0,
                                    wins=0,
                                    losses=0,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=1,
                                    forfeitLosses=0,
                                    points=4,
                                    bonusPoints=0)
                self.addDataToTable(tableData,
                                    team_a,
                                    goalsFor=0,
                                    goalsAgainst=0,
                                    wins=0,
                                    losses=0,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=1,
                                    points=0,
                                    bonusPoints=0)
        
        # check if result
        else:
            result  = self.gameResult(score_a,score_b)
            bonus   = self.gameBonus(score_a,score_b)
            score_a = int(score_a)
            score_b = int(score_b)
            
            if result == 'draw':
                self.addDataToTable(tableData,
                                    team_a,
                                    goalsFor=score_a,
                                    goalsAgainst=score_b,
                                    wins=0,
                                    losses=0,
                                    draws=1,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=2+bonus[0],
                                    bonusPoints=bonus[0])
                self.addDataToTable(tableData,
                                    team_b,
                                    goalsFor=score_b,
                                    goalsAgainst=score_a,
                                    wins=0,
                                    losses=0,
                                    draws=1,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=2+bonus[1],
                                    bonusPoints=bonus[1])
            elif result == 'awin':
                self.addDataToTable(tableData,
                                    team_a,
                                    goalsFor=score_a,
                                    goalsAgainst=score_b,
                                    wins=1,
                                    losses=0,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=4+bonus[0],
                                    bonusPoints=bonus[0])
                self.addDataToTable(tableData,
                                    team_b,
                                    goalsFor=score_b,
                                    goalsAgainst=score_a,
                                    wins=0,
                                    losses=1,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=0+bonus[1],
                                    bonusPoints=bonus[1])
            elif result == 'bwin':
                self.addDataToTable(tableData,
                                    team_a,
                                    goalsFor=score_a,
                                    goalsAgainst=score_b,
                                    wins=0,
                                    losses=1,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=0+bonus[0],
                                    bonusPoints=bonus[0])
                self.addDataToTable(tableData,
                                    team_b,
                                    goalsFor=score_b,
                                    goalsAgainst=score_a,
                                    wins=1,
                                    losses=0,
                                    draws=0,
                                    byes=0,
                                    forfeitWins=0,
                                    forfeitLosses=0,
                                    points=4+bonus[1],
                                    bonusPoints=bonus[1])
            
    
    def addDataToTable(self, tableData, team, goalsFor, goalsAgainst,
                       wins, losses, draws, byes, forfeitWins,
                       forfeitLosses, points, bonusPoints):
        tableData[team]['goalsFor']         += goalsFor
        tableData[team]['goalsAgainst']     += goalsAgainst
        tableData[team]['wins']             += wins
        tableData[team]['losses']           += losses
        tableData[team]['draws']            += draws
        tableData[team]['byes']             += byes
        tableData[team]['forfeitWins']      += forfeitWins
        tableData[team]['forfeitLosses']    += forfeitLosses
        tableData[team]['points']           += points
        tableData[team]['bonusPoints']      += bonusPoints
    
    
    def isBye(self,
              team_a,
              team_b
              ):
        if team_a == 'bye' or team_b == 'bye':
            return True
    
    def isForfeit(self,
                  score_a,
                  score_b
                  ):
        if score_a == 'FW' or score_a == 'FL' or score_b == 'FW' or score_b == 'FL':
            return True
        
    def gameBonus(self,
                  score_a,
                  score_b):
        bonus_a = score_a / 3
        bonus_b = score_b / 3
        return [bonus_a, bonus_b]
    
    def gameResult(self,
                   score_a,
                   score_b):
        if score_a == score_b:
            return 'draw'
        elif score_a > score_b:
            return 'awin'
        elif score_a < score_b:
            return 'bwin'
    
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
        #bars =  [(1, 15, "gold"), (2, 15, "asphalt")]
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
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
    
    def visualiseTable(self, orderedTable, tableData):
        """visualise table using blank scatter plot"""
        fig     = plt.figure(figsize=(30,15),dpi=300)
        ax      = plt.subplot(1,1,1,axisbg='white',autoscale_on=True, aspect='equal')
        xs      = []
        ys      = []
        
        tableHeaders = ['wins', 'losses', 'draws',
                        'goalsFor','goalsAgainst',
                        'byes','forfeitWins',
                        'forfeitLosses','points',
                        'bonusPoints']
        
        
        
        
        
    
    
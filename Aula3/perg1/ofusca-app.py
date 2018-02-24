# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateBlindData-app.py
#
# Cripto-7.1.1 - Commmad line app to exemplify the usage of blindData
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that receives Data and pRDashComponents from STDIN and writes
blindMessage and blindComponents and pRComponents to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind


def printUsage():
	print("Usage: python ofusca-app.py -msg <mensagem a assinar> -RDash <pRDashComponents>")

def parseArgs():
	if (sys.argv[1] != "-msg"):
		printUsage()
	else:
		i = 2
		msg = ""
		rdash = ""
		while(sys.argv[i] != "-RDash" and i < len(sys.argv)):
			msg+=sys.argv[i]
			i+=1
		if(i != len(sys.argv)):
			if(sys.argv[i] == "-RDash" ):
				i+=1
				while(i < len(sys.argv)):
					rdash+=sys.argv[i]
					i+=1
			else:
				printUsage()
		else:
			printUsage()
		main(msg, rdash)

def showResults(errorCode, result):
	if (errorCode is None):
		blindComponents, pRComponents, blindM = result
		print("%s" % blindM)
		out = open("message.components", "w")
		out.write(blindComponents)
		out.write("\n")
		out.write(pRComponents)
		out.close()
		
	elif (errorCode == 1):
		print("Error: pRDash components are invalid")

def main(data, pRDashComponents):
	errorCode, result = eccblind.blindData(pRDashComponents, data)
	showResults(errorCode, result)

if __name__ == "__main__":
	parseArgs()

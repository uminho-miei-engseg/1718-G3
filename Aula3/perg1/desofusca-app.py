# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# unblindSignature-app.py
#
# Cripto-7.3.1 - Commmad line app to exemplify the usage of unblindSignature
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
Command line app that receives Blind signature, Blind components and prDashComponents
from STDIN and writes the unblinded signature to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind


def printUsage():
	print("Usage: python desofusca-app.py -s <Blind Signature> -RDash <pRDashComponents>" )

def parseArgs():
	if (len(sys.argv) < 2 or sys.argv[1] != "-s"):
		printUsage()
	else:
		i = 2
		s = ""
		rdash = ""
		while(sys.argv[i] != "-RDash" and i < len(sys.argv)):
			s+=sys.argv[i]
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
		main(s, rdash)

def showResults(errorCode, signature):
	if (errorCode is None):
		print("%s" % signature)
	elif (errorCode == 1):
		print("Error: pRDash components are invalid")
	elif (errorCode == 2):
		print("Error: blind components are invalid")
	elif (errorCode == 3):
		print("Error: invalid blind signature format")

def main(blindSignature, pRDashComponents):
	inpu = open("message.components", "r")
	blindComponents = inpu.readline()
	errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
	showResults(errorCode, signature)

if __name__ == "__main__":
	parseArgs()

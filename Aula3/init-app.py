import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python initSigner-app.py")

def parseArgs():
    if (len(sys.argv) != 2):
        printUsage()
    elif (len(sys.argv) == 2):
		if (argv[1] == "-init"):
        	init()
		else:
			try:
				initted = open(argv[1], "r")
				
			except IOError:  			
				print("Error: command unknown")
		
	elif (len(sys.argv) == 1):
		normal()

def init():
	initComponents, pRDashComponents = eccblind.initSigner()
	

def normal():
    initComponents, pRDashComponents = eccblind.initSigner()
    print("Output")
    print("pRDashComponents: %s" % pRDashComponents)

if __name__ == "__main__":
    parseArgs()

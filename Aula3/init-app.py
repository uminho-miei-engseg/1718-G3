import sys
from eVotUM.Cripto import eccblind

def printUsage():
	print("Usage: python initSigner-app.py" )

def parseArgs():
	if (len(sys.argv) != 2 and len(sys.argv) != 1 ):
		printUsage()
	elif (len(sys.argv) == 2):
		if (sys.argv[1] == "-init"):
			init()
		else:
			print("Unknown Parameter")
	elif (len(sys.argv) == 1):
		normal()


def init():
	initComponents, pRDashComponents = eccblind.initSigner()
	componentesF = open('xcomponents.data', 'w')
	componentesF.write(initComponents + "\n")
	componentesF.write(pRDashComponents)
	componentesF.close()

def normal():
	#initComponents, pRDashComponents = eccblind.initSigner()
	try:
		componentes = open('xcomponents.data', 'r')
		componentes.readline()
		pR = componentes.readline()
		print("pRDashComponents:\n"+pR)
	except:
		print("Not initialized")

if __name__ == "__main__":
	parseArgs()

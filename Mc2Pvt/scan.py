from src.scanner import Scanner
import sys

min = ((int)(sys.argv[2]), (int)(sys.argv[3]), (int)(sys.argv[4]))
max = ((int)(sys.argv[5]), (int)(sys.argv[6]), (int)(sys.argv[7]))

scanner = Scanner(min, max, sys.argv[1])
scanner.scan()

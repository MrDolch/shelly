#! /usr/bin/python

import subprocess
import sys

def extractAllCommands(filename):
  with open(filename) as f:
    lines = f.readlines()
  yield '0', "vi %s" % lines[0].strip(), "bash", "vi %s" % filename
  h = s = e = n = 0
  c = ''
  for i, line in enumerate(lines):
    if line.startswith('#'):
      h = i
    elif line.strip() == '```bash':
        s = i
        c = "bash"
    elif line.strip() == '```javascript':
        s = i
        c = "javascript"
    elif line.strip() == '```':
        e = i
    if h>0 and s>0 and e>0:
      n += 1
      yield '%d'%n, lines[h].strip(), c, ''.join(lines[s+1:e])
      h = s = e = 0

## Hauptprogramm
filename = sys.argv[1] #"Shelly.md"

while True:

  print "-----------------------------------------------"

  for nr, title, shell, command in extractAllCommands(filename):
    print "%s) %s" % (nr, title)

  auswahl = raw_input("Auswahl: ")

  print "-----------------------------------------------"

  for nr, title, shell, command in extractAllCommands(filename):
    if auswahl == nr:
      print command
      if shell == "bash":
        print subprocess.Popen(['bash', '-c', command]).communicate()
      elif shell == "javascript":
        print subprocess.Popen(['js', '-e', command]).communicate()

  if auswahl == "q":
    break

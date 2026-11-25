#!/usr/bin/env python3
"""Installs the 5 check agents into .claude/agents of the folder you run it from.
Works on Windows, macOS and Linux. Needs Python 3 and nothing else.
If this file sits next to the agents/ folder (the ZIP), it copies from there, otherwise it downloads."""
import os, shutil, urllib.request

NAMES = ["quota-check", "instructions-check", "switch-check", "verify-check", "ownership-check"]
BASE = "https://raw.githubusercontent.com/guycoful/claude-dependency-test/main/agents/"
here = os.path.dirname(os.path.abspath(__file__))
dest = os.path.join(os.getcwd(), ".claude", "agents")
os.makedirs(dest, exist_ok=True)

for n in NAMES:
    local = os.path.join(here, "agents", n + ".md")
    target = os.path.join(dest, n + ".md")
    if os.path.exists(local):
        shutil.copyfile(local, target)
    else:
        urllib.request.urlretrieve(BASE + n + ".md", target)
    print("installed:", target)

print("Done. Open this folder in Claude Code and write: run quota-check on this project")

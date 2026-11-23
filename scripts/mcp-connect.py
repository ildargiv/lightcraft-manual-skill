#!/usr/bin/env python3
r"""OpenCode MCP launcher for LightCraft (connect mode, self-healing).

Before handing stdio to lightcraft-cli, make sure the desktop app is running
with --control 7980.  When it is not, start it on the same library and wait
for the control channel.  os.execv keeps the MCP stdio stream byte-exact.

Configured in ~/.config/opencode/opencode.json as:
    python.exe  ...\skills\lightcraft\scripts\mcp-connect.py
"""
import os
import socket
import subprocess
import sys
import time

CLI = os.path.join(os.environ.get("LOCALAPPDATA", r"%USERPROFILE%\AppData\Local"),
                   "Programs", "ArtCraft", "LightCraft", "lightcraft-cli.exe")
APP = os.path.join(os.path.dirname(CLI), "lightcraft.exe")
LIB = os.path.join(os.environ.get("USERPROFILE", r"C:\Users\User"),
                   "Pictures", "LightCraft Library")
HOST, PORT = "127.0.0.1", 7980


def port_open():
    s = socket.socket()
    s.settimeout(0.3)
    try:
        return s.connect_ex((HOST, PORT)) == 0
    finally:
        s.close()


def main():
    if not port_open():
        if os.path.isfile(APP):
            try:
                subprocess.Popen([APP, "--library", LIB, "--control", str(PORT)],
                                 close_fds=True)
            except OSError as e:
                print("lightcraft launcher: cannot start app:", e, file=sys.stderr)
        deadline = time.time() + 45
        while time.time() < deadline and not port_open():
            time.sleep(0.4)
        if not port_open():
            print("lightcraft launcher: control port not ready on %s:%d" % (HOST, PORT),
                  file=sys.stderr)

    # Inherit the parent's stdio verbatim: subprocess keeps the pipes that
    # OpenCode gave us, so the CLI's JSON-RPC stream is byte-exact.
    rc = subprocess.call([CLI, "mcp", "--compact", "--connect", "%s:%d" % (HOST, PORT)])
    sys.exit(rc)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

import names

def init():
    appContext = startApplication("addressbook fr")
    test.log("Application started with command \"%s\" at time %f in directory %s" % (appContext.commandLine, appContext.startTime, appContext.cwd))

def cleanup():
    ctx = currentApplicationContext()
    test.log("STDOUT", ctx.readStdout())
    test.warning("STDERR", ctx.readStderr())
    ctx.detach()
    
def main():
    ctx = currentApplicationContext()
    test.log("%s is current application context with id %d on port %d and host %s" % (ctx.name, ctx.pid, ctx.port, ctx.host))
    test.log("Memory: %d" % ctx.usedMemory)
    snooze(5)
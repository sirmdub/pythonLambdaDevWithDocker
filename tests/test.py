#!/bin/python
from pythonLambdaDevWithDocker import *

main(None, None)

setval("somevalue", redis_set)
if not r.sismember(redis_set, "somevalue"):
    raise Exception("FAILED: setval did not set val in db")

replaceval("somevalue", "somevalueelse", redis_set)
if r.sismember(redis_set, "somevalue"):
    raise Exception("FAILED: replaceval did not remove original val from db")
if not r.sismember(redis_set, "somevalueelse"):
    raise Exception("FAILED: replaceval did not set new val in db")

delval("somevalueelse", redis_set)
if r.sismember(redis_set, "somevalueelse"):
    raise Exception("FAILED: delval did not remove val from db")

#!/bin/python
import logging
import ConfigParser
import redis
import boto3

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

config = ConfigParser.ConfigParser()
config.read('config.ini')
redis_host = config.get("access", "redis_host")
redis_set = config.get("access", "redis_set")

r = redis.StrictRedis(host=redis_host)

def main(event, context):
    print("doing stuff")

def setval(val, redis_set):
    print("posting ", val, " to the Redis db", redis_set)
    r.sadd(redis_set, val)

def delval(val, redis_set):
    print("deleting ", val, " from the Redis db", redis_set)
    r.srem(redis_set, val)

def replaceval(val, val2, redis_set):
    print("replace ", val, " with ", val2, redis_set)
    delval(val,redis_set)
    setval(val2,redis_set)

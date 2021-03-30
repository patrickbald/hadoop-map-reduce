#!/bin/sh

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files nDegreesMap.py,nDegreesReduce.py -input /users/pbald/finalCleanData/host-link -output /users/pbald/finalOutputs/nhops -mapper nDegreesMap.py -reducer nDegreesReduce.py -numReduceTasks 1

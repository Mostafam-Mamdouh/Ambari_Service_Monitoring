####################################################################################################################
#
# File:        ambari_config.py
# Description: A config file, for Ambari REST API.
#              Note: tested on ambari version 2.6.2.0, used in HDP 2.6.5
# Author:      Mostafa Mamdouh
# Created:     Wed May 05 22:17:24 PDT 2021
#
####################################################################################################################


AMBARI_DOMAIN = 'localhost'
AMBARI_PORT = '8080'
AMBARI_USER_ID = 'raj_ops'
AMBARI_USER_PW = 'raj_ops'
RM_DOMAIN = '127.0.0.1'
RM_PORT = '8088'
REST_API = '/api/v1/clusters/'
# add services that you want to monitor
SERVICES = ["KAFKA", "SPARK2", "HDFS", "HIVE", "YARN", "RANGER", "FLUME", "HBASE"]
# time to check services
CHECK_EVERY = 5


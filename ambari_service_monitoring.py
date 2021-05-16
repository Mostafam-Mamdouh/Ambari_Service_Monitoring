####################################################################################################################
#
# File:        ambari_service_monitoring.py
# Description: A simple script to monitor services like (Kafka, Spark, HDFS, Hive, Yarn, Ranger, Flume, Hbase, ...)
#              using Ambari REST API. It needs Crontab or  any other scheduling tool.
#              If you do not want any scheduling tool, use ambari_service_monitoring_standalone.py
#              Note: Tested on Ambari version 2.6.2.0, used in HDP 2.6.5
# Author:      Mostafa Mamdouh
# Created:     Wed May 05 22:17:24 PDT 2021
#
####################################################################################################################


import ambari_config
import json
import requests


# Connect to the API
def ambari_rest(rest_api):
    url = "http://" + ambari_config.AMBARI_DOMAIN + ":" + ambari_config.AMBARI_PORT + rest_api
    r = requests.get(url, auth=(ambari_config.AMBARI_USER_ID, ambari_config.AMBARI_USER_PW))
    return(json.loads(r.text))

# Get desired service info
def get_service(service, cluster_name):
    rest_api = ambari_config.REST_API + cluster_name + "/services/" + service
    json_data =  ambari_rest(rest_api)
    return(json_data)

# Get ckuster name
def get_cluser_name() :
    json_data = ambari_rest(ambari_config.REST_API)
    cluster_name = json_data["items"][0]["Clusters"]["cluster_name"]
    return cluster_name


# Handle error by just print it, you can handle
# You can the desired action here (send email, excute script, ...) instead of just printing messages
# Also you can do one for error, and another for alert
def handle_error(components):  
    for component in components:
        component_rest_api = component["href"].split("8080")[1]
        component_dict = ambari_rest(component_rest_api)
        component_info = component_dict["ServiceComponentInfo"]
        component_keys = ['started_count', 'state', 'total_count', 'unknown_count']
        component_needed_info = {x:component_info[x] for x in component_keys}
        print("==" * 20)
        print(component["ServiceComponentInfo"]["component_name"] + " status:")
        print(component_needed_info)


def main():
    for service in ambari_config.SERVICES:
        cluster_name = get_cluser_name()
        service_dict = get_service(service, cluster_name) # dict
        service_info = service_dict["ServiceInfo"]
        service_key = ['maintenance_state', 'repository_state', 'service_name', 'state']
        service_needed_info = {x:service_info[x] for x in service_key}
        service_alerts = service_dict["alerts_summary"]
        print('=' * 50 + service + '=' * 50)
        if(service_needed_info["state"] != "STARTED"):
            # Do the desired action here (send email, excute script, ...) instead of just printing messages
            print("There is an Error, Actions will be set here")
            print(service + " status:")
            print(service_needed_info)
            print("Alerts Summary status:")
            print(service_alerts)
            components = service_dict["components"]    
            handle_error(components) # here we just print, you can do anything
        elif(service_alerts["CRITICAL"] > 0 or service_alerts["WARNING"] > 0 or service_alerts["UNKNOWN"] > 0):
            # Do the desired action here (send email, excute script, ...) instead of just printing messages
            print("There is an Alert, Actions will be set here")
            print(service + " status:")
            print(service_needed_info)
            print("Alerts Summary status:")
            print(service_alerts)
            components = service_dict["components"]    
            handle_error(components) # here we just print, you can do anything
        else:
            print("Everything is ok with " + service)

if __name__ == "__main__":
    main()


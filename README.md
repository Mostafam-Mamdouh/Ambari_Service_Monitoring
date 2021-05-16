# Ambari_Service_Monitoring

Ambari_Service_Monitoring is a simple Python script to monitor services like (Kafka, Spark, HDFS, Hive, Yarn, Ranger, Flume, Hbase, ...) using Ambari REST API.  
  
Note: Tested on Ambari version 2.6.2.0, used in HDP 2.6.5.


## Installation

Any Python version will work, no external libraries is needed.

## Usage

```bash
python ambari_service_monitoring_standalone.py
python ambari_service_monitoring.py
```

- Run ambari_service_monitoring_standalone.py, in case you want a standalone script that is always up and running.
- Run ambari_service_monitoring.py, in case you want your script to be scheduled by Crontab or any Scheduling tool.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
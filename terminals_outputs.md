# Q1 — Le dataDir de ZooKeeper :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ grep -E '^dataDir' ~/kafka/config/zookeeper.properties
dataDir=/home/raslan/kafka-data/zookeeper
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ ls -R ~/kafka-data/zookeeper
/home/raslan/kafka-data/zookeeper:
version-2

/home/raslan/kafka-data/zookeeper/version-2:
log.1  log.43  log.c2  snapshot.0  snapshot.42  snapshot.c1
```
---

# Q2 + Q3 + Q4 — Le shell ZooKeeper :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ zookeeper-shell.sh localhost:2181
Connecting to localhost:2181
Welcome to ZooKeeper!
JLine support is disabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
help
ZooKeeper -server host:port [-zk-tls-config-file <file>] cmd args
        addWatch [-m mode] path # optional mode is one of [PERSISTENT, PERSISTENT_RECURSIVE] - default is PERSISTENT_RECURSIVE
        addauth scheme auth
        close
        config [-c] [-w] [-s]
        connect host:port
        create [-s] [-e] [-c] [-t ttl] path [data] [acl]
        delete [-v version] path
        deleteall path [-b batch size]
        delquota [-n|-b|-N|-B] path
        get [-s] [-w] path
        getAcl [-s] path
        getAllChildrenNumber path
        getEphemerals path
        history
        listquota path
        ls [-s] [-w] [-R] path
        printwatches on|off
        quit
        reconfig [-s] [-v version] [[-file path] | [-members serverID=host:port1:port2;port3[,...]*]] | [-add serverId=host:port1:port2;port3[,...]]* [-remove serverId[,...]*]
        redo cmdno
        removewatches path [-c|-d|-a] [-l]
        set [-s] [-v version] path data
        setAcl [-s] [-v version] [-R] path acl
        setquota -n|-b|-N|-B val path
        stat [-w] path
        sync path
        version
        whoami
Command not found: Command not found help
ls /
[admin, brokers, cluster, config, consumers, controller, controller_epoch, feature, isr_change_notification, latest_producer_id_block, log_dir_event_notification, zookeeper]
ls /brokers/ids
[0]
get /brokers/ids/0
{"features":{},"listener_security_protocol_map":{"PLAINTEXT":"PLAINTEXT"},"endpoints":["PLAINTEXT://DESKTOP-L584EQM.localdomain:9092"],"jmx_port":-1,"port":9092,"host":"DESKTOP-L584EQM.localdomain","version":5,"timestamp":"1781706151709"}
get /brokers/topics/premier-topic
{"partitions":{"0":[0],"1":[0]},"topic_id":"WV18z8nWQ8yekl_6282UEQ","adding_replicas":{},"removing_replicas":{},"version":3}
get /controller
{"version":2,"brokerid":0,"timestamp":"1781706151854","kraftControllerEpoch":-1}
```

---

# 
## Shell ZK : 
###  ls /brokers/topics avant : 
```
ls /brokers/topics
[__consumer_offsets, premier-topic]
```
### la confirmation de création dans un autre terminal :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic zk-demo --partitions 1 --replication-factor 1
Created topic zk-demo.
```
### le ls après + le get :
```
ls /brokers/topics
[__consumer_offsets, premier-topic, zk-demo]
get /brokers/topics/zk-demo
{"partitions":{"0":[0]},"topic_id":"i5lmFi0tS0GZAAA0trfk7g","adding_replicas":{},"removing_replicas":{},"version":3}
```

---
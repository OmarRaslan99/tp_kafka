# terminal 1 :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ zookeeper-server-start.sh ~/kafka/config/zookeeper.properties
[2026-06-17 09:10:51,038] INFO Reading configuration from: /home/raslan/kafka/config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,043] INFO clientPortAddress is 0.0.0.0:2181 (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,043] INFO secureClientPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,043] INFO observerMasterPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,044] INFO metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,046] INFO autopurge.snapRetainCount set to 3 (org.apache.zookeeper.server.DatadirCleanupManager)
[2026-06-17 09:10:51,046] INFO autopurge.purgeInterval set to 0 (org.apache.zookeeper.server.DatadirCleanupManager)
[2026-06-17 09:10:51,046] INFO Purge task is not scheduled. (org.apache.zookeeper.server.DatadirCleanupManager)
[2026-06-17 09:10:51,046] WARN Either no config or no quorum defined in config, running in standalone mode (org.apache.zookeeper.server.quorum.QuorumPeerMain)
[2026-06-17 09:10:51,048] INFO Log4j 1.2 jmx support not found; jmx disabled. (org.apache.zookeeper.jmx.ManagedUtil)
[2026-06-17 09:10:51,049] INFO Reading configuration from: /home/raslan/kafka/config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,050] INFO clientPortAddress is 0.0.0.0:2181 (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,050] INFO secureClientPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,050] INFO observerMasterPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,050] INFO metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2026-06-17 09:10:51,051] INFO Starting server (org.apache.zookeeper.server.ZooKeeperServerMain)
[2026-06-17 09:10:51,070] INFO ServerMetrics initialized with provider org.apache.zookeeper.metrics.impl.DefaultMetricsProvider@4b168fa9 (org.apache.zookeeper.server.ServerMetrics)
[2026-06-17 09:10:51,076] INFO ACL digest algorithm is: SHA1 (org.apache.zookeeper.server.auth.DigestAuthenticationProvider)
[2026-06-17 09:10:51,076] INFO zookeeper.DigestAuthenticationProvider.enabled = true (org.apache.zookeeper.server.auth.DigestAuthenticationProvider)
[2026-06-17 09:10:51,080] INFO zookeeper.snapshot.trust.empty : false (org.apache.zookeeper.server.persistence.FileTxnSnapLog)
[2026-06-17 09:10:51,097] INFO  (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO   ______                  _                                           (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO  |___  /                 | |                                          (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO     / /    ___     ___   | | __   ___    ___   _ __     ___   _ __    (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO    / /    / _ \   / _ \  | |/ /  / _ \  / _ \ | '_ \   / _ \ | '__| (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO   / /__  | (_) | | (_) | |   <  |  __/ |  __/ | |_) | |  __/ | |     (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO  /_____|  \___/   \___/  |_|\_\  \___|  \___| | .__/   \___| |_| (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,098] INFO                                               | |                      (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,099] INFO                                               |_|                      (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,099] INFO  (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,103] INFO Server environment:zookeeper.version=3.8.4-9316c2a7a97e1666d8f4593f34dd6fc36ecc436c, built on 2024-02-12 22:16 UTC (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,103] INFO Server environment:host.name=DESKTOP-L584EQM.localdomain (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,104] INFO Server environment:java.version=17.0.19 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,104] INFO Server environment:java.vendor=Eclipse Adoptium (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,104] INFO Server environment:java.home=/home/raslan/jdk-17.0.19+10 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,104] INFO Server environment:java.class.path=/home/raslan/kafka/bin/../libs/activation-1.1.1.jar:/home/raslan/kafka/bin/../libs/aopalliance-repackaged-2.6.1.jar:/home/raslan/kafka/bin/../libs/argparse4j-0.7.0.jar:/home/raslan/kafka/bin/../libs/audience-annotations-0.12.0.jar:/home/raslan/kafka/bin/../libs/caffeine-2.9.3.jar:/home/raslan/kafka/bin/../libs/commons-beanutils-1.9.4.jar:/home/raslan/kafka/bin/../libs/commons-cli-1.4.jar:/home/raslan/kafka/bin/../libs/commons-collections-3.2.2.jar:/home/raslan/kafka/bin/../libs/commons-digester-2.1.jar:/home/raslan/kafka/bin/../libs/commons-io-2.14.0.jar:/home/raslan/kafka/bin/../libs/commons-lang3-3.12.0.jar:/home/raslan/kafka/bin/../libs/commons-logging-1.2.jar:/home/raslan/kafka/bin/../libs/commons-validator-1.7.jar:/home/raslan/kafka/bin/../libs/connect-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-basic-auth-extension-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-json-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-mirror-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-mirror-client-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-runtime-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-transforms-3.9.1.jar:/home/raslan/kafka/bin/../libs/error_prone_annotations-2.10.0.jar:/home/raslan/kafka/bin/../libs/hk2-api-2.6.1.jar:/home/raslan/kafka/bin/../libs/hk2-locator-2.6.1.jar:/home/raslan/kafka/bin/../libs/hk2-utils-2.6.1.jar:/home/raslan/kafka/bin/../libs/jackson-annotations-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-core-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-databind-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-dataformat-csv-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-datatype-jdk8-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-jaxrs-base-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-jaxrs-json-provider-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-module-afterburner-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-module-jaxb-annotations-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-module-scala_2.13-2.16.2.jar:/home/raslan/kafka/bin/../libs/jakarta.activation-api-1.2.2.jar:/home/raslan/kafka/bin/../libs/jakarta.annotation-api-1.3.5.jar:/home/raslan/kafka/bin/../libs/jakarta.inject-2.6.1.jar:/home/raslan/kafka/bin/../libs/jakarta.validation-api-2.0.2.jar:/home/raslan/kafka/bin/../libs/jakarta.ws.rs-api-2.1.6.jar:/home/raslan/kafka/bin/../libs/jakarta.xml.bind-api-2.3.3.jar:/home/raslan/kafka/bin/../libs/javassist-3.29.2-GA.jar:/home/raslan/kafka/bin/../libs/javax.activation-api-1.2.0.jar:/home/raslan/kafka/bin/../libs/javax.annotation-api-1.3.2.jar:/home/raslan/kafka/bin/../libs/javax.servlet-api-3.1.0.jar:/home/raslan/kafka/bin/../libs/javax.ws.rs-api-2.1.1.jar:/home/raslan/kafka/bin/../libs/jaxb-api-2.3.1.jar:/home/raslan/kafka/bin/../libs/jersey-client-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-common-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-container-servlet-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-container-servlet-core-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-hk2-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-server-2.39.1.jar:/home/raslan/kafka/bin/../libs/jetty-client-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-continuation-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-http-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-io-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-security-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-server-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-servlet-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-servlets-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-util-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-util-ajax-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jline-3.25.1.jar:/home/raslan/kafka/bin/../libs/jopt-simple-5.0.4.jar:/home/raslan/kafka/bin/../libs/jose4j-0.9.4.jar:/home/raslan/kafka/bin/../libs/jsr305-3.0.2.jar:/home/raslan/kafka/bin/../libs/kafka-clients-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-group-coordinator-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-group-coordinator-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-metadata-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-raft-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-server-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-server-common-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-shell-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-storage-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-storage-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-examples-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-scala_2.13-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-test-utils-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-tools-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-tools-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-transaction-coordinator-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka_2.13-3.9.1.jar:/home/raslan/kafka/bin/../libs/lz4-java-1.8.0.jar:/home/raslan/kafka/bin/../libs/maven-artifact-3.9.6.jar:/home/raslan/kafka/bin/../libs/metrics-core-2.2.0.jar:/home/raslan/kafka/bin/../libs/metrics-core-4.1.12.1.jar:/home/raslan/kafka/bin/../libs/netty-buffer-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-codec-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-common-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-handler-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-resolver-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-classes-epoll-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-native-epoll-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-native-unix-common-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/opentelemetry-proto-1.0.0-alpha.jar:/home/raslan/kafka/bin/../libs/osgi-resource-locator-1.0.3.jar:/home/raslan/kafka/bin/../libs/paranamer-2.8.jar:/home/raslan/kafka/bin/../libs/pcollections-4.0.1.jar:/home/raslan/kafka/bin/../libs/plexus-utils-3.5.1.jar:/home/raslan/kafka/bin/../libs/protobuf-java-3.25.5.jar:/home/raslan/kafka/bin/../libs/reflections-0.10.2.jar:/home/raslan/kafka/bin/../libs/reload4j-1.2.25.jar:/home/raslan/kafka/bin/../libs/rocksdbjni-7.9.2.jar:/home/raslan/kafka/bin/../libs/scala-collection-compat_2.13-2.10.0.jar:/home/raslan/kafka/bin/../libs/scala-java8-compat_2.13-1.0.2.jar:/home/raslan/kafka/bin/../libs/scala-library-2.13.15.jar:/home/raslan/kafka/bin/../libs/scala-logging_2.13-3.9.5.jar:/home/raslan/kafka/bin/../libs/scala-reflect-2.13.15.jar:/home/raslan/kafka/bin/../libs/slf4j-api-1.7.36.jar:/home/raslan/kafka/bin/../libs/slf4j-reload4j-1.7.36.jar:/home/raslan/kafka/bin/../libs/snappy-java-1.1.10.5.jar:/home/raslan/kafka/bin/../libs/swagger-annotations-2.2.8.jar:/home/raslan/kafka/bin/../libs/trogdor-3.9.1.jar:/home/raslan/kafka/bin/../libs/zookeeper-3.8.4.jar:/home/raslan/kafka/bin/../libs/zookeeper-jute-3.8.4.jar:/home/raslan/kafka/bin/../libs/zstd-jni-1.5.6-4.jar (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:java.library.path=/usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:java.io.tmpdir=/tmp (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:java.compiler=<NA> (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:os.name=Linux (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:os.arch=amd64 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:os.version=6.18.33.1-microsoft-standard-WSL2 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:user.name=raslan (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,107] INFO Server environment:user.home=/home/raslan (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,108] INFO Server environment:user.dir=/mnt/c/tp_kafka (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,108] INFO Server environment:os.memory.free=493MB (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,108] INFO Server environment:os.memory.max=512MB (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,108] INFO Server environment:os.memory.total=512MB (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,108] INFO zookeeper.enableEagerACLCheck = false (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,109] INFO zookeeper.digest.enabled = true (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,109] INFO zookeeper.closeSessionTxn.enabled = true (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,110] INFO zookeeper.flushDelay = 0 ms (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,110] INFO zookeeper.maxWriteQueuePollTime = 0 ms (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,110] INFO zookeeper.maxBatchSize=1000 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,110] INFO zookeeper.intBufferStartingSizeBytes = 1024 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,112] INFO Weighed connection throttling is disabled (org.apache.zookeeper.server.BlueThrottle)
[2026-06-17 09:10:51,115] INFO minSessionTimeout set to 6000 ms (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,115] INFO maxSessionTimeout set to 60000 ms (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,117] INFO getData response cache size is initialized with value 400. (org.apache.zookeeper.server.ResponseCache)
[2026-06-17 09:10:51,117] INFO getChildren response cache size is initialized with value 400. (org.apache.zookeeper.server.ResponseCache)
[2026-06-17 09:10:51,119] INFO zookeeper.pathStats.slotCapacity = 60 (org.apache.zookeeper.server.util.RequestPathMetricsCollector)
[2026-06-17 09:10:51,119] INFO zookeeper.pathStats.slotDuration = 15 (org.apache.zookeeper.server.util.RequestPathMetricsCollector)
[2026-06-17 09:10:51,119] INFO zookeeper.pathStats.maxDepth = 6 (org.apache.zookeeper.server.util.RequestPathMetricsCollector)
[2026-06-17 09:10:51,120] INFO zookeeper.pathStats.initialDelay = 5 (org.apache.zookeeper.server.util.RequestPathMetricsCollector)
[2026-06-17 09:10:51,120] INFO zookeeper.pathStats.delay = 5 (org.apache.zookeeper.server.util.RequestPathMetricsCollector)
[2026-06-17 09:10:51,120] INFO zookeeper.pathStats.enabled = false (org.apache.zookeeper.server.util.RequestPathMetricsCollector)
[2026-06-17 09:10:51,125] INFO The max bytes for all large requests are set to 104857600 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,126] INFO The large request threshold is set to -1 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,127] INFO zookeeper.enforce.auth.enabled = false (org.apache.zookeeper.server.AuthenticationHelper)
[2026-06-17 09:10:51,127] INFO zookeeper.enforce.auth.schemes = [] (org.apache.zookeeper.server.AuthenticationHelper)
[2026-06-17 09:10:51,127] INFO Created server with tickTime 3000 ms minSessionTimeout 6000 ms maxSessionTimeout 60000 ms clientPortListenBacklog -1 datadir /home/raslan/kafka-data/zookeeper/version-2 snapdir /home/raslan/kafka-data/zookeeper/version-2 (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,136] INFO Using org.apache.zookeeper.server.NIOServerCnxnFactory as server connection factory (org.apache.zookeeper.server.ServerCnxnFactory)
[2026-06-17 09:10:51,139] WARN maxCnxns is not configured, using default value 0. (org.apache.zookeeper.server.ServerCnxnFactory)
[2026-06-17 09:10:51,142] INFO Configuring NIO connection handler with 10s sessionless connection timeout, 2 selector thread(s), 16 worker threads, and 64 kB direct buffers. (org.apache.zookeeper.server.NIOServerCnxnFactory)
[2026-06-17 09:10:51,152] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
[2026-06-17 09:10:51,175] INFO Using org.apache.zookeeper.server.watch.WatchManager as watch manager (org.apache.zookeeper.server.watch.WatchManagerFactory)
[2026-06-17 09:10:51,175] INFO Using org.apache.zookeeper.server.watch.WatchManager as watch manager (org.apache.zookeeper.server.watch.WatchManagerFactory)
[2026-06-17 09:10:51,176] INFO zookeeper.snapshotSizeFactor = 0.33 (org.apache.zookeeper.server.ZKDatabase)
[2026-06-17 09:10:51,176] INFO zookeeper.commitLogCount=500 (org.apache.zookeeper.server.ZKDatabase)
[2026-06-17 09:10:51,182] INFO zookeeper.snapshot.compression.method = CHECKED (org.apache.zookeeper.server.persistence.SnapStream)
[2026-06-17 09:10:51,184] INFO Reading snapshot /home/raslan/kafka-data/zookeeper/version-2/snapshot.0 (org.apache.zookeeper.server.persistence.FileSnap)
[2026-06-17 09:10:51,193] INFO The digest value is empty in snapshot (org.apache.zookeeper.server.DataTree)
[2026-06-17 09:10:51,230] INFO ZooKeeper audit is disabled. (org.apache.zookeeper.audit.ZKAuditProvider)
[2026-06-17 09:10:51,231] INFO 66 txns loaded in 29 ms (org.apache.zookeeper.server.persistence.FileTxnSnapLog)
[2026-06-17 09:10:51,231] INFO Snapshot loaded in 55 ms, highest zxid is 0x42, digest is 59799150515 (org.apache.zookeeper.server.ZKDatabase)
[2026-06-17 09:10:51,234] INFO Snapshotting: 0x42 to /home/raslan/kafka-data/zookeeper/version-2/snapshot.42 (org.apache.zookeeper.server.persistence.FileTxnSnapLog)
[2026-06-17 09:10:51,237] INFO Snapshot taken in 2 ms (org.apache.zookeeper.server.ZooKeeperServer)
[2026-06-17 09:10:51,249] INFO PrepRequestProcessor (sid:0) started, reconfigEnabled=false (org.apache.zookeeper.server.PrepRequestProcessor)
[2026-06-17 09:10:51,249] INFO zookeeper.request_throttler.shutdownTimeout = 10000 ms (org.apache.zookeeper.server.RequestThrottler)
[2026-06-17 09:10:51,275] INFO Using checkIntervalMs=60000 maxPerMinute=10000 maxNeverUsedIntervalMs=0 (org.apache.zookeeper.server.ContainerManager)
[2026-06-17 09:11:27,930] INFO Creating new log file: log.43 (org.apache.zookeeper.server.persistence.FileTxnLog)
```

---

# terminal 2 : 
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-server-start.sh ~/kafka/config/server.properties
[2026-06-17 09:11:27,436] INFO Registered kafka:type=kafka.Log4jController MBean (kafka.utils.Log4jControllerRegistration$)
[2026-06-17 09:11:27,721] INFO Setting -D jdk.tls.rejectClientInitiatedRenegotiation=true to disable client-initiated TLS renegotiation (org.apache.zookeeper.common.X509Util)
[2026-06-17 09:11:27,850] INFO Registered signal handlers for TERM, INT, HUP (org.apache.kafka.common.utils.LoggingSignalHandler)
[2026-06-17 09:11:27,853] INFO starting (kafka.server.KafkaServer)
[2026-06-17 09:11:27,854] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2026-06-17 09:11:27,883] INFO [ZooKeeperClient Kafka server] Initializing a new session to localhost:2181. (kafka.zookeeper.ZooKeeperClient)
[2026-06-17 09:11:27,888] INFO Client environment:zookeeper.version=3.8.4-9316c2a7a97e1666d8f4593f34dd6fc36ecc436c, built on 2024-02-12 22:16 UTC (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,888] INFO Client environment:host.name=DESKTOP-L584EQM.localdomain (org.apache.zookeeper.ZooKeeper)[2026-06-17 09:11:27,888] INFO Client environment:java.version=17.0.19 (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,888] INFO Client environment:java.vendor=Eclipse Adoptium (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,889] INFO Client environment:java.home=/home/raslan/jdk-17.0.19+10 (org.apache.zookeeper.ZooKeeper)[2026-06-17 09:11:27,889] INFO Client environment:java.class.path=/home/raslan/kafka/bin/../libs/activation-1.1.1.jar:/home/raslan/kafka/bin/../libs/aopalliance-repackaged-2.6.1.jar:/home/raslan/kafka/bin/../libs/argparse4j-0.7.0.jar:/home/raslan/kafka/bin/../libs/audience-annotations-0.12.0.jar:/home/raslan/kafka/bin/../libs/caffeine-2.9.3.jar:/home/raslan/kafka/bin/../libs/commons-beanutils-1.9.4.jar:/home/raslan/kafka/bin/../libs/commons-cli-1.4.jar:/home/raslan/kafka/bin/../libs/commons-collections-3.2.2.jar:/home/raslan/kafka/bin/../libs/commons-digester-2.1.jar:/home/raslan/kafka/bin/../libs/commons-io-2.14.0.jar:/home/raslan/kafka/bin/../libs/commons-lang3-3.12.0.jar:/home/raslan/kafka/bin/../libs/commons-logging-1.2.jar:/home/raslan/kafka/bin/../libs/commons-validator-1.7.jar:/home/raslan/kafka/bin/../libs/connect-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-basic-auth-extension-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-json-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-mirror-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-mirror-client-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-runtime-3.9.1.jar:/home/raslan/kafka/bin/../libs/connect-transforms-3.9.1.jar:/home/raslan/kafka/bin/../libs/error_prone_annotations-2.10.0.jar:/home/raslan/kafka/bin/../libs/hk2-api-2.6.1.jar:/home/raslan/kafka/bin/../libs/hk2-locator-2.6.1.jar:/home/raslan/kafka/bin/../libs/hk2-utils-2.6.1.jar:/home/raslan/kafka/bin/../libs/jackson-annotations-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-core-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-databind-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-dataformat-csv-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-datatype-jdk8-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-jaxrs-base-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-jaxrs-json-provider-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-module-afterburner-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-module-jaxb-annotations-2.16.2.jar:/home/raslan/kafka/bin/../libs/jackson-module-scala_2.13-2.16.2.jar:/home/raslan/kafka/bin/../libs/jakarta.activation-api-1.2.2.jar:/home/raslan/kafka/bin/../libs/jakarta.annotation-api-1.3.5.jar:/home/raslan/kafka/bin/../libs/jakarta.inject-2.6.1.jar:/home/raslan/kafka/bin/../libs/jakarta.validation-api-2.0.2.jar:/home/raslan/kafka/bin/../libs/jakarta.ws.rs-api-2.1.6.jar:/home/raslan/kafka/bin/../libs/jakarta.xml.bind-api-2.3.3.jar:/home/raslan/kafka/bin/../libs/javassist-3.29.2-GA.jar:/home/raslan/kafka/bin/../libs/javax.activation-api-1.2.0.jar:/home/raslan/kafka/bin/../libs/javax.annotation-api-1.3.2.jar:/home/raslan/kafka/bin/../libs/javax.servlet-api-3.1.0.jar:/home/raslan/kafka/bin/../libs/javax.ws.rs-api-2.1.1.jar:/home/raslan/kafka/bin/../libs/jaxb-api-2.3.1.jar:/home/raslan/kafka/bin/../libs/jersey-client-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-common-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-container-servlet-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-container-servlet-core-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-hk2-2.39.1.jar:/home/raslan/kafka/bin/../libs/jersey-server-2.39.1.jar:/home/raslan/kafka/bin/../libs/jetty-client-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-continuation-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-http-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-io-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-security-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-server-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-servlet-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-servlets-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-util-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jetty-util-ajax-9.4.57.v20241219.jar:/home/raslan/kafka/bin/../libs/jline-3.25.1.jar:/home/raslan/kafka/bin/../libs/jopt-simple-5.0.4.jar:/home/raslan/kafka/bin/../libs/jose4j-0.9.4.jar:/home/raslan/kafka/bin/../libs/jsr305-3.0.2.jar:/home/raslan/kafka/bin/../libs/kafka-clients-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-group-coordinator-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-group-coordinator-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-metadata-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-raft-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-server-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-server-common-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-shell-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-storage-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-storage-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-examples-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-scala_2.13-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-streams-test-utils-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-tools-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-tools-api-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka-transaction-coordinator-3.9.1.jar:/home/raslan/kafka/bin/../libs/kafka_2.13-3.9.1.jar:/home/raslan/kafka/bin/../libs/lz4-java-1.8.0.jar:/home/raslan/kafka/bin/../libs/maven-artifact-3.9.6.jar:/home/raslan/kafka/bin/../libs/metrics-core-2.2.0.jar:/home/raslan/kafka/bin/../libs/metrics-core-4.1.12.1.jar:/home/raslan/kafka/bin/../libs/netty-buffer-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-codec-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-common-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-handler-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-resolver-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-classes-epoll-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-native-epoll-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/netty-transport-native-unix-common-4.1.119.Final.jar:/home/raslan/kafka/bin/../libs/opentelemetry-proto-1.0.0-alpha.jar:/home/raslan/kafka/bin/../libs/osgi-resource-locator-1.0.3.jar:/home/raslan/kafka/bin/../libs/paranamer-2.8.jar:/home/raslan/kafka/bin/../libs/pcollections-4.0.1.jar:/home/raslan/kafka/bin/../libs/plexus-utils-3.5.1.jar:/home/raslan/kafka/bin/../libs/protobuf-java-3.25.5.jar:/home/raslan/kafka/bin/../libs/reflections-0.10.2.jar:/home/raslan/kafka/bin/../libs/reload4j-1.2.25.jar:/home/raslan/kafka/bin/../libs/rocksdbjni-7.9.2.jar:/home/raslan/kafka/bin/../libs/scala-collection-compat_2.13-2.10.0.jar:/home/raslan/kafka/bin/../libs/scala-java8-compat_2.13-1.0.2.jar:/home/raslan/kafka/bin/../libs/scala-library-2.13.15.jar:/home/raslan/kafka/bin/../libs/scala-logging_2.13-3.9.5.jar:/home/raslan/kafka/bin/../libs/scala-reflect-2.13.15.jar:/home/raslan/kafka/bin/../libs/slf4j-api-1.7.36.jar:/home/raslan/kafka/bin/../libs/slf4j-reload4j-1.7.36.jar:/home/raslan/kafka/bin/../libs/snappy-java-1.1.10.5.jar:/home/raslan/kafka/bin/../libs/swagger-annotations-2.2.8.jar:/home/raslan/kafka/bin/../libs/trogdor-3.9.1.jar:/home/raslan/kafka/bin/../libs/zookeeper-3.8.4.jar:/home/raslan/kafka/bin/../libs/zookeeper-jute-3.8.4.jar:/home/raslan/kafka/bin/../libs/zstd-jni-1.5.6-4.jar (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,889] INFO Client environment:java.library.path=/usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,890] INFO Client environment:java.io.tmpdir=/tmp (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,890] INFO Client environment:java.compiler=<NA> (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,890] INFO Client environment:os.name=Linux (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,890] INFO Client environment:os.arch=amd64 (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,890] INFO Client environment:os.version=6.18.33.1-microsoft-standard-WSL2 (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,891] INFO Client environment:user.name=raslan (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,891] INFO Client environment:user.home=/home/raslan (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,891] INFO Client environment:user.dir=/mnt/c/tp_kafka (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,891] INFO Client environment:os.memory.free=985MB (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,891] INFO Client environment:os.memory.max=1024MB (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,891] INFO Client environment:os.memory.total=1024MB (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,895] INFO Initiating client connection, connectString=localhost:2181 sessionTimeout=18000 watcher=kafka.zookeeper.ZooKeeperClient$ZooKeeperClientWatcher$@163370c2 (org.apache.zookeeper.ZooKeeper)
[2026-06-17 09:11:27,902] INFO jute.maxbuffer value is 4194304 Bytes (org.apache.zookeeper.ClientCnxnSocket)
[2026-06-17 09:11:27,909] INFO zookeeper.request.timeout value is 0. feature enabled=false (org.apache.zookeeper.ClientCnxn)
[2026-06-17 09:11:27,913] INFO [ZooKeeperClient Kafka server] Waiting until connected. (kafka.zookeeper.ZooKeeperClient)[2026-06-17 09:11:27,915] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 09:11:27,920] INFO Socket connection established, initiating session, client: /127.0.0.1:44360, server: localhost/127.0.0.1:2181 (org.apache.zookeeper.ClientCnxn)
[2026-06-17 09:11:27,946] INFO Session establishment complete on server localhost/127.0.0.1:2181, session id = 0x1000064cf1a0000, negotiated timeout = 18000 (org.apache.zookeeper.ClientCnxn)
[2026-06-17 09:11:27,950] INFO [ZooKeeperClient Kafka server] Connected. (kafka.zookeeper.ZooKeeperClient)
[2026-06-17 09:11:28,256] INFO Cluster ID = BgHp5tiGT8SnzBtDKNITdQ (kafka.server.KafkaServer)
[2026-06-17 09:11:28,316] INFO KafkaConfig values:
        advertised.listeners = null
        alter.config.policy.class.name = null
        alter.log.dirs.replication.quota.window.num = 11
        alter.log.dirs.replication.quota.window.size.seconds = 1
        authorizer.class.name =
        auto.create.topics.enable = true
        auto.include.jmx.reporter = true
        auto.leader.rebalance.enable = true
        background.threads = 10
        broker.heartbeat.interval.ms = 2000
        broker.id = 0
        broker.id.generation.enable = true
        broker.rack = null
        broker.session.timeout.ms = 9000
        client.quota.callback.class = null
        compression.gzip.level = -1
        compression.lz4.level = 9
        compression.type = producer
        compression.zstd.level = 3
        connection.failed.authentication.delay.ms = 100
        connections.max.idle.ms = 600000
        connections.max.reauth.ms = 0
        control.plane.listener.name = null
        controlled.shutdown.enable = true
        controlled.shutdown.max.retries = 3
        controlled.shutdown.retry.backoff.ms = 5000
        controller.listener.names = null
        controller.quorum.append.linger.ms = 25
        controller.quorum.bootstrap.servers = []
        controller.quorum.election.backoff.max.ms = 1000
        controller.quorum.election.timeout.ms = 1000
        controller.quorum.fetch.timeout.ms = 2000
        controller.quorum.request.timeout.ms = 2000
        controller.quorum.retry.backoff.ms = 20
        controller.quorum.voters = []
        controller.quota.window.num = 11
        controller.quota.window.size.seconds = 1
        controller.socket.timeout.ms = 30000
        create.topic.policy.class.name = null
        default.replication.factor = 1
        delegation.token.expiry.check.interval.ms = 3600000
        delegation.token.expiry.time.ms = 86400000
        delegation.token.master.key = null
        delegation.token.max.lifetime.ms = 604800000
        delegation.token.secret.key = null
        delete.records.purgatory.purge.interval.requests = 1
        delete.topic.enable = true
        early.start.listeners = null
        eligible.leader.replicas.enable = false
        fetch.max.bytes = 57671680
        fetch.purgatory.purge.interval.requests = 1000
        group.consumer.assignors = [org.apache.kafka.coordinator.group.assignor.UniformAssignor, org.apache.kafka.coordinator.group.assignor.RangeAssignor]
        group.consumer.heartbeat.interval.ms = 5000
        group.consumer.max.heartbeat.interval.ms = 15000
        group.consumer.max.session.timeout.ms = 60000
        group.consumer.max.size = 2147483647
        group.consumer.migration.policy = disabled
        group.consumer.min.heartbeat.interval.ms = 5000
        group.consumer.min.session.timeout.ms = 45000
        group.consumer.session.timeout.ms = 45000
        group.coordinator.append.linger.ms = 10
        group.coordinator.new.enable = false
        group.coordinator.rebalance.protocols = [classic]
        group.coordinator.threads = 1
        group.initial.rebalance.delay.ms = 0
        group.max.session.timeout.ms = 1800000
        group.max.size = 2147483647
        group.min.session.timeout.ms = 6000
        group.share.delivery.count.limit = 5
        group.share.enable = false
        group.share.heartbeat.interval.ms = 5000
        group.share.max.groups = 10
        group.share.max.heartbeat.interval.ms = 15000
        group.share.max.record.lock.duration.ms = 60000
        group.share.max.session.timeout.ms = 60000
        group.share.max.size = 200
        group.share.min.heartbeat.interval.ms = 5000
        group.share.min.record.lock.duration.ms = 15000
        group.share.min.session.timeout.ms = 45000
        group.share.partition.max.record.locks = 200
        group.share.record.lock.duration.ms = 30000
        group.share.session.timeout.ms = 45000
        initial.broker.registration.timeout.ms = 60000
        inter.broker.listener.name = null
        inter.broker.protocol.version = 3.9-IV0
        kafka.metrics.polling.interval.secs = 10
        kafka.metrics.reporters = []
        leader.imbalance.check.interval.seconds = 300
        leader.imbalance.per.broker.percentage = 10
        listener.security.protocol.map = SASL_SSL:SASL_SSL,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT
        listeners = PLAINTEXT://:9092
        log.cleaner.backoff.ms = 15000
        log.cleaner.dedupe.buffer.size = 134217728
        log.cleaner.delete.retention.ms = 86400000
        log.cleaner.enable = true
        log.cleaner.io.buffer.load.factor = 0.9
        log.cleaner.io.buffer.size = 524288
        log.cleaner.io.max.bytes.per.second = 1.7976931348623157E308
        log.cleaner.max.compaction.lag.ms = 9223372036854775807
        log.cleaner.min.cleanable.ratio = 0.5
        log.cleaner.min.compaction.lag.ms = 0
        log.cleaner.threads = 1
        log.cleanup.policy = [delete]
        log.dir = /tmp/kafka-logs
        log.dir.failure.timeout.ms = 30000
        log.dirs = /home/raslan/kafka-data/kafka-logs
        log.flush.interval.messages = 9223372036854775807
        log.flush.interval.ms = null
        log.flush.offset.checkpoint.interval.ms = 60000
        log.flush.scheduler.interval.ms = 9223372036854775807
        log.flush.start.offset.checkpoint.interval.ms = 60000
        log.index.interval.bytes = 4096
        log.index.size.max.bytes = 10485760
        log.initial.task.delay.ms = 30000
        log.local.retention.bytes = -2
        log.local.retention.ms = -2
        log.message.downconversion.enable = true
        log.message.format.version = 3.0-IV1
        log.message.timestamp.after.max.ms = 9223372036854775807
        log.message.timestamp.before.max.ms = 9223372036854775807
        log.message.timestamp.difference.max.ms = 9223372036854775807
        log.message.timestamp.type = CreateTime
        log.preallocate = false
        log.retention.bytes = -1
        log.retention.check.interval.ms = 300000
        log.retention.hours = 168
        log.retention.minutes = null
        log.retention.ms = null
        log.roll.hours = 168
        log.roll.jitter.hours = 0
        log.roll.jitter.ms = null
        log.roll.ms = null
        log.segment.bytes = 1073741824
        log.segment.delete.delay.ms = 60000
        max.connection.creation.rate = 2147483647
        max.connections = 2147483647
        max.connections.per.ip = 2147483647
        max.connections.per.ip.overrides =
        max.incremental.fetch.session.cache.slots = 1000
        max.request.partition.size.limit = 2000
        message.max.bytes = 1048588
        metadata.log.dir = null
        metadata.log.max.record.bytes.between.snapshots = 20971520
        metadata.log.max.snapshot.interval.ms = 3600000
        metadata.log.segment.bytes = 1073741824
        metadata.log.segment.min.bytes = 8388608
        metadata.log.segment.ms = 604800000
        metadata.max.idle.interval.ms = 500
        metadata.max.retention.bytes = 104857600
        metadata.max.retention.ms = 604800000
        metric.reporters = []
        metrics.num.samples = 2
        metrics.recording.level = INFO
        metrics.sample.window.ms = 30000
        min.insync.replicas = 1
        node.id = 0
        num.io.threads = 8
        num.network.threads = 3
        num.partitions = 1
        num.recovery.threads.per.data.dir = 1
        num.replica.alter.log.dirs.threads = null
        num.replica.fetchers = 1
        offset.metadata.max.bytes = 4096
        offsets.commit.required.acks = -1
        offsets.commit.timeout.ms = 5000
        offsets.load.buffer.size = 5242880
        offsets.retention.check.interval.ms = 600000
        offsets.retention.minutes = 10080
        offsets.topic.compression.codec = 0
        offsets.topic.num.partitions = 50
        offsets.topic.replication.factor = 1
        offsets.topic.segment.bytes = 104857600
        password.encoder.cipher.algorithm = AES/CBC/PKCS5Padding
        password.encoder.iterations = 4096
        password.encoder.key.length = 128
        password.encoder.keyfactory.algorithm = null
        password.encoder.old.secret = null
        password.encoder.secret = null
        principal.builder.class = class org.apache.kafka.common.security.authenticator.DefaultKafkaPrincipalBuilder
        process.roles = []
        producer.id.expiration.check.interval.ms = 600000
        producer.id.expiration.ms = 86400000
        producer.purgatory.purge.interval.requests = 1000
        queued.max.request.bytes = -1
        queued.max.requests = 500
        quota.window.num = 11
        quota.window.size.seconds = 1
        remote.fetch.max.wait.ms = 500
        remote.log.index.file.cache.total.size.bytes = 1073741824
        remote.log.manager.copier.thread.pool.size = -1
        remote.log.manager.copy.max.bytes.per.second = 9223372036854775807
        remote.log.manager.copy.quota.window.num = 11
        remote.log.manager.copy.quota.window.size.seconds = 1
        remote.log.manager.expiration.thread.pool.size = -1
        remote.log.manager.fetch.max.bytes.per.second = 9223372036854775807
        remote.log.manager.fetch.quota.window.num = 11
        remote.log.manager.fetch.quota.window.size.seconds = 1
        remote.log.manager.task.interval.ms = 30000
        remote.log.manager.task.retry.backoff.max.ms = 30000
        remote.log.manager.task.retry.backoff.ms = 500
        remote.log.manager.task.retry.jitter = 0.2
        remote.log.manager.thread.pool.size = 10
        remote.log.metadata.custom.metadata.max.bytes = 128
        remote.log.metadata.manager.class.name = org.apache.kafka.server.log.remote.metadata.storage.TopicBasedRemoteLogMetadataManager
        remote.log.metadata.manager.class.path = null
        remote.log.metadata.manager.impl.prefix = rlmm.config.
        remote.log.metadata.manager.listener.name = null
        remote.log.reader.max.pending.tasks = 100
        remote.log.reader.threads = 10
        remote.log.storage.manager.class.name = null
        remote.log.storage.manager.class.path = null
        remote.log.storage.manager.impl.prefix = rsm.config.
        remote.log.storage.system.enable = false
        replica.fetch.backoff.ms = 1000
        replica.fetch.max.bytes = 1048576
        replica.fetch.min.bytes = 1
        replica.fetch.response.max.bytes = 10485760
        replica.fetch.wait.max.ms = 500
        replica.high.watermark.checkpoint.interval.ms = 5000
        replica.lag.time.max.ms = 30000
        replica.selector.class = null
        replica.socket.receive.buffer.bytes = 65536
        replica.socket.timeout.ms = 30000
        replication.quota.window.num = 11
        replication.quota.window.size.seconds = 1
        request.timeout.ms = 30000
        reserved.broker.max.id = 1000
        sasl.client.callback.handler.class = null
        sasl.enabled.mechanisms = [GSSAPI]
        sasl.jaas.config = null
        sasl.kerberos.kinit.cmd = /usr/bin/kinit
        sasl.kerberos.min.time.before.relogin = 60000
        sasl.kerberos.principal.to.local.rules = [DEFAULT]
        sasl.kerberos.service.name = null
        sasl.kerberos.ticket.renew.jitter = 0.05
        sasl.kerberos.ticket.renew.window.factor = 0.8
        sasl.login.callback.handler.class = null
        sasl.login.class = null
        sasl.login.connect.timeout.ms = null
        sasl.login.read.timeout.ms = null
        sasl.login.refresh.buffer.seconds = 300
        sasl.login.refresh.min.period.seconds = 60
        sasl.login.refresh.window.factor = 0.8
        sasl.login.refresh.window.jitter = 0.05
        sasl.login.retry.backoff.max.ms = 10000
        sasl.login.retry.backoff.ms = 100
        sasl.mechanism.controller.protocol = GSSAPI
        sasl.mechanism.inter.broker.protocol = GSSAPI
        sasl.oauthbearer.clock.skew.seconds = 30
        sasl.oauthbearer.expected.audience = null
        sasl.oauthbearer.expected.issuer = null
        sasl.oauthbearer.jwks.endpoint.refresh.ms = 3600000
        sasl.oauthbearer.jwks.endpoint.retry.backoff.max.ms = 10000
        sasl.oauthbearer.jwks.endpoint.retry.backoff.ms = 100
        sasl.oauthbearer.jwks.endpoint.url = null
        sasl.oauthbearer.scope.claim.name = scope
        sasl.oauthbearer.sub.claim.name = sub
        sasl.oauthbearer.token.endpoint.url = null
        sasl.server.callback.handler.class = null
        sasl.server.max.receive.size = 524288
        security.inter.broker.protocol = PLAINTEXT
        security.providers = null
        server.max.startup.time.ms = 9223372036854775807
        socket.connection.setup.timeout.max.ms = 30000
        socket.connection.setup.timeout.ms = 10000
        socket.listen.backlog.size = 50
        socket.receive.buffer.bytes = 102400
        socket.request.max.bytes = 104857600
        socket.send.buffer.bytes = 102400
        ssl.allow.dn.changes = false
        ssl.allow.san.changes = false
        ssl.cipher.suites = []
        ssl.client.auth = none
        ssl.enabled.protocols = [TLSv1.2, TLSv1.3]
        ssl.endpoint.identification.algorithm = https
        ssl.engine.factory.class = null
        ssl.key.password = null
        ssl.keymanager.algorithm = SunX509
        ssl.keystore.certificate.chain = null
        ssl.keystore.key = null
        ssl.keystore.location = null
        ssl.keystore.password = null
        ssl.keystore.type = JKS
        ssl.principal.mapping.rules = DEFAULT
        ssl.protocol = TLSv1.3
        ssl.provider = null
        ssl.secure.random.implementation = null
        ssl.trustmanager.algorithm = PKIX
        ssl.truststore.certificates = null
        ssl.truststore.location = null
        ssl.truststore.password = null
        ssl.truststore.type = JKS
        telemetry.max.bytes = 1048576
        transaction.abort.timed.out.transaction.cleanup.interval.ms = 10000
        transaction.max.timeout.ms = 900000
        transaction.partition.verification.enable = true
        transaction.remove.expired.transaction.cleanup.interval.ms = 3600000
        transaction.state.log.load.buffer.size = 5242880
        transaction.state.log.min.isr = 1
        transaction.state.log.num.partitions = 50
        transaction.state.log.replication.factor = 1
        transaction.state.log.segment.bytes = 104857600
        transactional.id.expiration.ms = 604800000
        unclean.leader.election.enable = false
        unclean.leader.election.interval.ms = 300000
        unstable.api.versions.enable = false
        unstable.feature.versions.enable = false
        zookeeper.clientCnxnSocket = null
        zookeeper.connect = localhost:2181
        zookeeper.connection.timeout.ms = 18000
        zookeeper.max.in.flight.requests = 10
        zookeeper.metadata.migration.enable = false
        zookeeper.metadata.migration.min.batch.size = 200
        zookeeper.session.timeout.ms = 18000
        zookeeper.set.acl = false
        zookeeper.ssl.cipher.suites = null
        zookeeper.ssl.client.enable = false
        zookeeper.ssl.crl.enable = false
        zookeeper.ssl.enabled.protocols = null
        zookeeper.ssl.endpoint.identification.algorithm = HTTPS
        zookeeper.ssl.keystore.location = null
        zookeeper.ssl.keystore.password = null
        zookeeper.ssl.keystore.type = null
        zookeeper.ssl.ocsp.enable = false
        zookeeper.ssl.protocol = TLSv1.2
        zookeeper.ssl.truststore.location = null
        zookeeper.ssl.truststore.password = null
        zookeeper.ssl.truststore.type = null
 (kafka.server.KafkaConfig)
[2026-06-17 09:11:28,363] INFO [ThrottledChannelReaper-Fetch]: Starting (kafka.server.ClientQuotaManager$ThrottledChannelReaper)
[2026-06-17 09:11:28,363] INFO [ThrottledChannelReaper-Produce]: Starting (kafka.server.ClientQuotaManager$ThrottledChannelReaper)
[2026-06-17 09:11:28,365] INFO [ThrottledChannelReaper-Request]: Starting (kafka.server.ClientQuotaManager$ThrottledChannelReaper)
[2026-06-17 09:11:28,369] INFO [ThrottledChannelReaper-ControllerMutation]: Starting (kafka.server.ClientQuotaManager$ThrottledChannelReaper)
[2026-06-17 09:11:28,423] INFO Loading logs from log dirs ArrayBuffer(/home/raslan/kafka-data/kafka-logs) (kafka.log.LogManager)
[2026-06-17 09:11:28,440] INFO Skipping recovery of 1 logs from /home/raslan/kafka-data/kafka-logs since clean shutdown file was found (kafka.log.LogManager)
[2026-06-17 09:11:28,534] INFO [LogLoader partition=premier-topic-0, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:11:28,552] INFO Completed load of Log(dir=/home/raslan/kafka-data/kafka-logs/premier-topic-0, topicId=WV18z8nWQ8yekl_6282UEQ, topic=premier-topic, partition=0, highWatermark=0, lastStableOffset=0, logStartOffset=0, logEndOffset=0) with 1 segments, local-log-start-offset 0 and log-end-offset 0 in 105ms (1/1 completed in /home/raslan/kafka-data/kafka-logs) (kafka.log.LogManager)
[2026-06-17 09:11:28,557] INFO Loaded 1 logs in 133ms (kafka.log.LogManager)
[2026-06-17 09:11:28,560] INFO Starting log cleanup with a period of 300000 ms. (kafka.log.LogManager)
[2026-06-17 09:11:28,562] INFO Starting log flusher with a default period of 9223372036854775807 ms. (kafka.log.LogManager)
[2026-06-17 09:11:28,724] INFO [kafka-log-cleaner-thread-0]: Starting (kafka.log.LogCleaner$CleanerThread)
[2026-06-17 09:11:28,739] INFO [feature-zk-node-event-process-thread]: Starting (kafka.server.FinalizedFeatureChangeListener$ChangeNotificationProcessorThread)
[2026-06-17 09:11:28,759] INFO [MetadataCache brokerId=0] Updated cache from existing None to latest Features(metadataVersion=3.9-IV0, finalizedFeatures={}, finalizedFeaturesEpoch=0). (kafka.server.metadata.ZkMetadataCache)
[2026-06-17 09:11:28,785] INFO [zk-broker-0-to-controller-forwarding-channel-manager]: Starting (kafka.server.NodeToControllerRequestThread)
[2026-06-17 09:11:29,112] INFO Updated connection-accept-rate max connection creation rate to 2147483647 (kafka.network.ConnectionQuotas)
[2026-06-17 09:11:29,132] INFO [SocketServer listenerType=ZK_BROKER, nodeId=0] Created data-plane acceptor and processors for endpoint : ListenerName(PLAINTEXT) (kafka.network.SocketServer)
[2026-06-17 09:11:29,138] INFO [zk-broker-0-to-controller-alter-partition-channel-manager]: Starting (kafka.server.NodeToControllerRequestThread)
[2026-06-17 09:11:29,167] INFO [ExpirationReaper-0-Produce]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,168] INFO [ExpirationReaper-0-Fetch]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,171] INFO [ExpirationReaper-0-DeleteRecords]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,173] INFO [ExpirationReaper-0-ElectLeader]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,175] INFO [ExpirationReaper-0-RemoteFetch]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,196] INFO [LogDirFailureHandler]: Starting (kafka.server.ReplicaManager$LogDirFailureHandler)
[2026-06-17 09:11:29,198] INFO [AddPartitionsToTxnSenderThread-0]: Starting (kafka.server.AddPartitionsToTxnManager)
[2026-06-17 09:11:29,257] INFO Creating /brokers/ids/0 (is it secure? false) (kafka.zk.KafkaZkClient)
[2026-06-17 09:11:29,284] INFO Stat of the created znode at /brokers/ids/0 is: 82,82,1781680289273,1781680289273,1,0,0,72058027009245184,238,0,82
 (kafka.zk.KafkaZkClient)
[2026-06-17 09:11:29,285] INFO Registered broker 0 at path /brokers/ids/0 with addresses: PLAINTEXT://DESKTOP-L584EQM.localdomain:9092, czxid (broker epoch): 82 (kafka.zk.KafkaZkClient)
[2026-06-17 09:11:29,340] INFO [ExpirationReaper-0-topic]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,357] INFO [ExpirationReaper-0-Heartbeat]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,359] INFO [ExpirationReaper-0-Rebalance]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,382] INFO [GroupCoordinator 0]: Starting up. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:11:29,389] INFO [GroupCoordinator 0]: Startup complete. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:11:29,412] INFO [TransactionCoordinator id=0] Starting up. (kafka.coordinator.transaction.TransactionCoordinator)
[2026-06-17 09:11:29,418] INFO [TransactionCoordinator id=0] Startup complete. (kafka.coordinator.transaction.TransactionCoordinator)
[2026-06-17 09:11:29,418] INFO [TxnMarkerSenderThread-0]: Starting (kafka.coordinator.transaction.TransactionMarkerChannelManager)
[2026-06-17 09:11:29,478] INFO [ExpirationReaper-0-AlterAcls]: Starting (kafka.server.DelayedOperationPurgatory$ExpiredOperationReaper)
[2026-06-17 09:11:29,499] INFO [Controller id=0, targetBrokerId=0] Node 0 disconnected. (org.apache.kafka.clients.NetworkClient)
[2026-06-17 09:11:29,515] WARN [Controller id=0, targetBrokerId=0] Connection to node 0 (DESKTOP-L584EQM.localdomain/127.0.1.1:9092) could not be established. Node may not be available. (org.apache.kafka.clients.NetworkClient)
[2026-06-17 09:11:29,519] INFO [Controller id=0, targetBrokerId=0] Client requested connection close from node 0 (org.apache.kafka.clients.NetworkClient)
[2026-06-17 09:11:29,537] INFO [/config/changes-event-process-thread]: Starting (kafka.common.ZkNodeChangeNotificationListener$ChangeEventProcessThread)
[2026-06-17 09:11:29,593] INFO [SocketServer listenerType=ZK_BROKER, nodeId=0] Enabling request processing. (kafka.network.SocketServer)
[2026-06-17 09:11:29,602] INFO Awaiting socket connections on 0.0.0.0:9092. (kafka.network.DataPlaneAcceptor)
[2026-06-17 09:11:29,612] INFO [KafkaServer id=0] Start processing authorizer futures (kafka.server.KafkaServer)
[2026-06-17 09:11:29,615] INFO [KafkaServer id=0] End processing authorizer futures (kafka.server.KafkaServer)
[2026-06-17 09:11:29,616] INFO [KafkaServer id=0] Start processing enable request processing future (kafka.server.KafkaServer)
[2026-06-17 09:11:29,617] INFO [KafkaServer id=0] End processing enable request processing future (kafka.server.KafkaServer)
[2026-06-17 09:11:29,626] INFO Kafka version: 3.9.1 (org.apache.kafka.common.utils.AppInfoParser)
[2026-06-17 09:11:29,627] INFO Kafka commitId: f745dfdcee2b9851 (org.apache.kafka.common.utils.AppInfoParser)
[2026-06-17 09:11:29,627] INFO Kafka startTimeMs: 1781680289617 (org.apache.kafka.common.utils.AppInfoParser)
[2026-06-17 09:11:29,629] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)
[2026-06-17 09:11:29,696] INFO [zk-broker-0-to-controller-forwarding-channel-manager]: Recorded new ZK controller, from now on will use node DESKTOP-L584EQM.localdomain:9092 (id: 0 rack: null) (kafka.server.NodeToControllerRequestThread)
[2026-06-17 09:11:29,719] INFO [ReplicaFetcherManager on broker 0] Removed fetcher for partitions Set(premier-topic-0) (kafka.server.ReplicaFetcherManager)
[2026-06-17 09:11:29,733] INFO [Partition premier-topic-0 broker=0] Log loaded for partition premier-topic-0 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:11:29,745] INFO [zk-broker-0-to-controller-alter-partition-channel-manager]: Recorded new ZK controller, from now on will use node DESKTOP-L584EQM.localdomain:9092 (id: 0 rack: null) (kafka.server.NodeToControllerRequestThread)
[2026-06-17 09:16:04,878] INFO Creating topic __consumer_offsets with configuration {compression.type=producer, cleanup.policy=compact, segment.bytes=104857600} and initial partition assignment HashMap(0 -> ArrayBuffer(0), 1 -> ArrayBuffer(0), 2 -> ArrayBuffer(0), 3 -> ArrayBuffer(0), 4 -> ArrayBuffer(0), 5 -> ArrayBuffer(0), 6 -> ArrayBuffer(0), 7 -> ArrayBuffer(0), 8 -> ArrayBuffer(0), 9 -> ArrayBuffer(0), 10 -> ArrayBuffer(0), 11 -> ArrayBuffer(0), 12 -> ArrayBuffer(0), 13 -> ArrayBuffer(0), 14 -> ArrayBuffer(0), 15 -> ArrayBuffer(0), 16 -> ArrayBuffer(0), 17 -> ArrayBuffer(0), 18 -> ArrayBuffer(0), 19 -> ArrayBuffer(0), 20 -> ArrayBuffer(0), 21 -> ArrayBuffer(0), 22 -> ArrayBuffer(0), 23 -> ArrayBuffer(0), 24 -> ArrayBuffer(0), 25 -> ArrayBuffer(0), 26 -> ArrayBuffer(0), 27 -> ArrayBuffer(0), 28 -> ArrayBuffer(0), 29 -> ArrayBuffer(0), 30 -> ArrayBuffer(0), 31 -> ArrayBuffer(0), 32 -> ArrayBuffer(0), 33 -> ArrayBuffer(0), 34 -> ArrayBuffer(0), 35 -> ArrayBuffer(0), 36 -> ArrayBuffer(0), 37 -> ArrayBuffer(0), 38 -> ArrayBuffer(0), 39 -> ArrayBuffer(0), 40 -> ArrayBuffer(0), 41 -> ArrayBuffer(0), 42 -> ArrayBuffer(0), 43 -> ArrayBuffer(0), 44 -> ArrayBuffer(0), 45 -> ArrayBuffer(0), 46 -> ArrayBuffer(0), 47 -> ArrayBuffer(0), 48 -> ArrayBuffer(0), 49 -> ArrayBuffer(0)) (kafka.zk.AdminZkClient)
[2026-06-17 09:16:05,056] INFO [ReplicaFetcherManager on broker 0] Removed fetcher for partitions HashSet(__consumer_offsets-22, __consumer_offsets-30, __consumer_offsets-25, __consumer_offsets-35, __consumer_offsets-37, __consumer_offsets-38, __consumer_offsets-13, __consumer_offsets-8, __consumer_offsets-21, __consumer_offsets-4, __consumer_offsets-27, __consumer_offsets-7, __consumer_offsets-9, __consumer_offsets-46, __consumer_offsets-41, __consumer_offsets-33, __consumer_offsets-23, __consumer_offsets-49, __consumer_offsets-47, __consumer_offsets-16, __consumer_offsets-28, __consumer_offsets-31, __consumer_offsets-36, __consumer_offsets-42, __consumer_offsets-3, __consumer_offsets-18, __consumer_offsets-15, __consumer_offsets-24, __consumer_offsets-17, __consumer_offsets-48, __consumer_offsets-19, __consumer_offsets-11, __consumer_offsets-2, __consumer_offsets-43, __consumer_offsets-6, __consumer_offsets-14, __consumer_offsets-20, __consumer_offsets-0, __consumer_offsets-44, __consumer_offsets-39, __consumer_offsets-12, __consumer_offsets-45, __consumer_offsets-1, __consumer_offsets-5, __consumer_offsets-26, __consumer_offsets-29, __consumer_offsets-34, __consumer_offsets-10, __consumer_offsets-32, __consumer_offsets-40) (kafka.server.ReplicaFetcherManager)
[2026-06-17 09:16:05,068] INFO [LogLoader partition=__consumer_offsets-3, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,071] INFO Created log for partition __consumer_offsets-3 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-3 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,073] INFO [Partition __consumer_offsets-3 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-3 (kafka.cluster.Partition)
[2026-06-17 09:16:05,073] INFO [Partition __consumer_offsets-3 broker=0] Log loaded for partition __consumer_offsets-3 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,089] INFO [LogLoader partition=__consumer_offsets-18, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,091] INFO Created log for partition __consumer_offsets-18 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-18 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,091] INFO [Partition __consumer_offsets-18 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-18 (kafka.cluster.Partition)
[2026-06-17 09:16:05,092] INFO [Partition __consumer_offsets-18 broker=0] Log loaded for partition __consumer_offsets-18 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,109] INFO [LogLoader partition=__consumer_offsets-41, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,111] INFO Created log for partition __consumer_offsets-41 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-41 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,112] INFO [Partition __consumer_offsets-41 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-41 (kafka.cluster.Partition)
[2026-06-17 09:16:05,112] INFO [Partition __consumer_offsets-41 broker=0] Log loaded for partition __consumer_offsets-41 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,126] INFO [LogLoader partition=__consumer_offsets-10, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,127] INFO Created log for partition __consumer_offsets-10 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-10 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,128] INFO [Partition __consumer_offsets-10 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-10 (kafka.cluster.Partition)
[2026-06-17 09:16:05,129] INFO [Partition __consumer_offsets-10 broker=0] Log loaded for partition __consumer_offsets-10 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,146] INFO [LogLoader partition=__consumer_offsets-33, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,147] INFO Created log for partition __consumer_offsets-33 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-33 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,149] INFO [Partition __consumer_offsets-33 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-33 (kafka.cluster.Partition)
[2026-06-17 09:16:05,149] INFO [Partition __consumer_offsets-33 broker=0] Log loaded for partition __consumer_offsets-33 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,168] INFO [LogLoader partition=__consumer_offsets-48, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,169] INFO Created log for partition __consumer_offsets-48 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-48 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,170] INFO [Partition __consumer_offsets-48 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-48 (kafka.cluster.Partition)
[2026-06-17 09:16:05,170] INFO [Partition __consumer_offsets-48 broker=0] Log loaded for partition __consumer_offsets-48 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,187] INFO [LogLoader partition=__consumer_offsets-19, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,188] INFO Created log for partition __consumer_offsets-19 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-19 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,189] INFO [Partition __consumer_offsets-19 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-19 (kafka.cluster.Partition)
[2026-06-17 09:16:05,189] INFO [Partition __consumer_offsets-19 broker=0] Log loaded for partition __consumer_offsets-19 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,204] INFO [LogLoader partition=__consumer_offsets-34, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,205] INFO Created log for partition __consumer_offsets-34 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-34 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,205] INFO [Partition __consumer_offsets-34 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-34 (kafka.cluster.Partition)
[2026-06-17 09:16:05,205] INFO [Partition __consumer_offsets-34 broker=0] Log loaded for partition __consumer_offsets-34 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,221] INFO [LogLoader partition=__consumer_offsets-4, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,222] INFO Created log for partition __consumer_offsets-4 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-4 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,223] INFO [Partition __consumer_offsets-4 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-4 (kafka.cluster.Partition)
[2026-06-17 09:16:05,223] INFO [Partition __consumer_offsets-4 broker=0] Log loaded for partition __consumer_offsets-4 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,236] INFO [LogLoader partition=__consumer_offsets-11, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,237] INFO Created log for partition __consumer_offsets-11 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-11 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,237] INFO [Partition __consumer_offsets-11 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-11 (kafka.cluster.Partition)
[2026-06-17 09:16:05,237] INFO [Partition __consumer_offsets-11 broker=0] Log loaded for partition __consumer_offsets-11 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,253] INFO [LogLoader partition=__consumer_offsets-26, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,254] INFO Created log for partition __consumer_offsets-26 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-26 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,254] INFO [Partition __consumer_offsets-26 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-26 (kafka.cluster.Partition)
[2026-06-17 09:16:05,254] INFO [Partition __consumer_offsets-26 broker=0] Log loaded for partition __consumer_offsets-26 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,270] INFO [LogLoader partition=__consumer_offsets-49, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,271] INFO Created log for partition __consumer_offsets-49 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-49 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,271] INFO [Partition __consumer_offsets-49 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-49 (kafka.cluster.Partition)
[2026-06-17 09:16:05,271] INFO [Partition __consumer_offsets-49 broker=0] Log loaded for partition __consumer_offsets-49 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,286] INFO [LogLoader partition=__consumer_offsets-39, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,287] INFO Created log for partition __consumer_offsets-39 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-39 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,287] INFO [Partition __consumer_offsets-39 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-39 (kafka.cluster.Partition)
[2026-06-17 09:16:05,287] INFO [Partition __consumer_offsets-39 broker=0] Log loaded for partition __consumer_offsets-39 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,304] INFO [LogLoader partition=__consumer_offsets-9, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,305] INFO Created log for partition __consumer_offsets-9 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-9 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,305] INFO [Partition __consumer_offsets-9 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-9 (kafka.cluster.Partition)
[2026-06-17 09:16:05,305] INFO [Partition __consumer_offsets-9 broker=0] Log loaded for partition __consumer_offsets-9 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,323] INFO [LogLoader partition=__consumer_offsets-24, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,324] INFO Created log for partition __consumer_offsets-24 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-24 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,324] INFO [Partition __consumer_offsets-24 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-24 (kafka.cluster.Partition)
[2026-06-17 09:16:05,324] INFO [Partition __consumer_offsets-24 broker=0] Log loaded for partition __consumer_offsets-24 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,342] INFO [LogLoader partition=__consumer_offsets-31, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,343] INFO Created log for partition __consumer_offsets-31 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-31 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,343] INFO [Partition __consumer_offsets-31 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-31 (kafka.cluster.Partition)
[2026-06-17 09:16:05,343] INFO [Partition __consumer_offsets-31 broker=0] Log loaded for partition __consumer_offsets-31 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,360] INFO [LogLoader partition=__consumer_offsets-46, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,361] INFO Created log for partition __consumer_offsets-46 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-46 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,361] INFO [Partition __consumer_offsets-46 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-46 (kafka.cluster.Partition)
[2026-06-17 09:16:05,361] INFO [Partition __consumer_offsets-46 broker=0] Log loaded for partition __consumer_offsets-46 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,377] INFO [LogLoader partition=__consumer_offsets-1, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,377] INFO Created log for partition __consumer_offsets-1 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-1 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,377] INFO [Partition __consumer_offsets-1 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-1 (kafka.cluster.Partition)
[2026-06-17 09:16:05,378] INFO [Partition __consumer_offsets-1 broker=0] Log loaded for partition __consumer_offsets-1 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,393] INFO [LogLoader partition=__consumer_offsets-16, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,394] INFO Created log for partition __consumer_offsets-16 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-16 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,394] INFO [Partition __consumer_offsets-16 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-16 (kafka.cluster.Partition)
[2026-06-17 09:16:05,394] INFO [Partition __consumer_offsets-16 broker=0] Log loaded for partition __consumer_offsets-16 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,412] INFO [LogLoader partition=__consumer_offsets-2, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,413] INFO Created log for partition __consumer_offsets-2 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-2 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,413] INFO [Partition __consumer_offsets-2 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-2 (kafka.cluster.Partition)
[2026-06-17 09:16:05,413] INFO [Partition __consumer_offsets-2 broker=0] Log loaded for partition __consumer_offsets-2 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,432] INFO [LogLoader partition=__consumer_offsets-25, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,433] INFO Created log for partition __consumer_offsets-25 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-25 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,433] INFO [Partition __consumer_offsets-25 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-25 (kafka.cluster.Partition)
[2026-06-17 09:16:05,433] INFO [Partition __consumer_offsets-25 broker=0] Log loaded for partition __consumer_offsets-25 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,451] INFO [LogLoader partition=__consumer_offsets-40, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,452] INFO Created log for partition __consumer_offsets-40 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-40 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,452] INFO [Partition __consumer_offsets-40 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-40 (kafka.cluster.Partition)
[2026-06-17 09:16:05,452] INFO [Partition __consumer_offsets-40 broker=0] Log loaded for partition __consumer_offsets-40 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,468] INFO [LogLoader partition=__consumer_offsets-47, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,469] INFO Created log for partition __consumer_offsets-47 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-47 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,469] INFO [Partition __consumer_offsets-47 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-47 (kafka.cluster.Partition)
[2026-06-17 09:16:05,470] INFO [Partition __consumer_offsets-47 broker=0] Log loaded for partition __consumer_offsets-47 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,486] INFO [LogLoader partition=__consumer_offsets-17, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,487] INFO Created log for partition __consumer_offsets-17 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-17 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,487] INFO [Partition __consumer_offsets-17 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-17 (kafka.cluster.Partition)
[2026-06-17 09:16:05,487] INFO [Partition __consumer_offsets-17 broker=0] Log loaded for partition __consumer_offsets-17 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,505] INFO [LogLoader partition=__consumer_offsets-32, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,505] INFO Created log for partition __consumer_offsets-32 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-32 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,506] INFO [Partition __consumer_offsets-32 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-32 (kafka.cluster.Partition)
[2026-06-17 09:16:05,506] INFO [Partition __consumer_offsets-32 broker=0] Log loaded for partition __consumer_offsets-32 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,523] INFO [LogLoader partition=__consumer_offsets-37, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,524] INFO Created log for partition __consumer_offsets-37 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-37 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,524] INFO [Partition __consumer_offsets-37 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-37 (kafka.cluster.Partition)
[2026-06-17 09:16:05,524] INFO [Partition __consumer_offsets-37 broker=0] Log loaded for partition __consumer_offsets-37 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,542] INFO [LogLoader partition=__consumer_offsets-7, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,543] INFO Created log for partition __consumer_offsets-7 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-7 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,543] INFO [Partition __consumer_offsets-7 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-7 (kafka.cluster.Partition)
[2026-06-17 09:16:05,543] INFO [Partition __consumer_offsets-7 broker=0] Log loaded for partition __consumer_offsets-7 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,560] INFO [LogLoader partition=__consumer_offsets-22, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,561] INFO Created log for partition __consumer_offsets-22 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-22 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,561] INFO [Partition __consumer_offsets-22 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-22 (kafka.cluster.Partition)
[2026-06-17 09:16:05,561] INFO [Partition __consumer_offsets-22 broker=0] Log loaded for partition __consumer_offsets-22 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,577] INFO [LogLoader partition=__consumer_offsets-29, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,578] INFO Created log for partition __consumer_offsets-29 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-29 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,578] INFO [Partition __consumer_offsets-29 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-29 (kafka.cluster.Partition)
[2026-06-17 09:16:05,578] INFO [Partition __consumer_offsets-29 broker=0] Log loaded for partition __consumer_offsets-29 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,596] INFO [LogLoader partition=__consumer_offsets-44, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,597] INFO Created log for partition __consumer_offsets-44 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-44 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,598] INFO [Partition __consumer_offsets-44 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-44 (kafka.cluster.Partition)
[2026-06-17 09:16:05,598] INFO [Partition __consumer_offsets-44 broker=0] Log loaded for partition __consumer_offsets-44 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,617] INFO [LogLoader partition=__consumer_offsets-14, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,618] INFO Created log for partition __consumer_offsets-14 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-14 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,618] INFO [Partition __consumer_offsets-14 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-14 (kafka.cluster.Partition)
[2026-06-17 09:16:05,618] INFO [Partition __consumer_offsets-14 broker=0] Log loaded for partition __consumer_offsets-14 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,636] INFO [LogLoader partition=__consumer_offsets-23, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,637] INFO Created log for partition __consumer_offsets-23 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-23 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,637] INFO [Partition __consumer_offsets-23 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-23 (kafka.cluster.Partition)
[2026-06-17 09:16:05,637] INFO [Partition __consumer_offsets-23 broker=0] Log loaded for partition __consumer_offsets-23 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,655] INFO [LogLoader partition=__consumer_offsets-38, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,656] INFO Created log for partition __consumer_offsets-38 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-38 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,656] INFO [Partition __consumer_offsets-38 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-38 (kafka.cluster.Partition)
[2026-06-17 09:16:05,656] INFO [Partition __consumer_offsets-38 broker=0] Log loaded for partition __consumer_offsets-38 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,673] INFO [LogLoader partition=__consumer_offsets-8, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,674] INFO Created log for partition __consumer_offsets-8 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-8 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,675] INFO [Partition __consumer_offsets-8 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-8 (kafka.cluster.Partition)
[2026-06-17 09:16:05,675] INFO [Partition __consumer_offsets-8 broker=0] Log loaded for partition __consumer_offsets-8 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,691] INFO [LogLoader partition=__consumer_offsets-45, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,692] INFO Created log for partition __consumer_offsets-45 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-45 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,692] INFO [Partition __consumer_offsets-45 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-45 (kafka.cluster.Partition)
[2026-06-17 09:16:05,693] INFO [Partition __consumer_offsets-45 broker=0] Log loaded for partition __consumer_offsets-45 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,708] INFO [LogLoader partition=__consumer_offsets-15, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,709] INFO Created log for partition __consumer_offsets-15 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-15 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,710] INFO [Partition __consumer_offsets-15 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-15 (kafka.cluster.Partition)
[2026-06-17 09:16:05,710] INFO [Partition __consumer_offsets-15 broker=0] Log loaded for partition __consumer_offsets-15 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,727] INFO [LogLoader partition=__consumer_offsets-30, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,729] INFO Created log for partition __consumer_offsets-30 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-30 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,729] INFO [Partition __consumer_offsets-30 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-30 (kafka.cluster.Partition)
[2026-06-17 09:16:05,729] INFO [Partition __consumer_offsets-30 broker=0] Log loaded for partition __consumer_offsets-30 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,750] INFO [LogLoader partition=__consumer_offsets-0, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,751] INFO Created log for partition __consumer_offsets-0 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-0 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,751] INFO [Partition __consumer_offsets-0 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,751] INFO [Partition __consumer_offsets-0 broker=0] Log loaded for partition __consumer_offsets-0 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,769] INFO [LogLoader partition=__consumer_offsets-35, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,770] INFO Created log for partition __consumer_offsets-35 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-35 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,770] INFO [Partition __consumer_offsets-35 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-35 (kafka.cluster.Partition)
[2026-06-17 09:16:05,770] INFO [Partition __consumer_offsets-35 broker=0] Log loaded for partition __consumer_offsets-35 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,787] INFO [LogLoader partition=__consumer_offsets-5, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,788] INFO Created log for partition __consumer_offsets-5 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-5 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,789] INFO [Partition __consumer_offsets-5 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-5 (kafka.cluster.Partition)
[2026-06-17 09:16:05,789] INFO [Partition __consumer_offsets-5 broker=0] Log loaded for partition __consumer_offsets-5 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,807] INFO [LogLoader partition=__consumer_offsets-20, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,808] INFO Created log for partition __consumer_offsets-20 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-20 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,808] INFO [Partition __consumer_offsets-20 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-20 (kafka.cluster.Partition)
[2026-06-17 09:16:05,808] INFO [Partition __consumer_offsets-20 broker=0] Log loaded for partition __consumer_offsets-20 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,824] INFO [LogLoader partition=__consumer_offsets-27, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,824] INFO Created log for partition __consumer_offsets-27 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-27 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,825] INFO [Partition __consumer_offsets-27 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-27 (kafka.cluster.Partition)
[2026-06-17 09:16:05,825] INFO [Partition __consumer_offsets-27 broker=0] Log loaded for partition __consumer_offsets-27 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,843] INFO [LogLoader partition=__consumer_offsets-42, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,844] INFO Created log for partition __consumer_offsets-42 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-42 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,844] INFO [Partition __consumer_offsets-42 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-42 (kafka.cluster.Partition)
[2026-06-17 09:16:05,844] INFO [Partition __consumer_offsets-42 broker=0] Log loaded for partition __consumer_offsets-42 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,864] INFO [LogLoader partition=__consumer_offsets-12, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,866] INFO Created log for partition __consumer_offsets-12 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-12 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,866] INFO [Partition __consumer_offsets-12 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-12 (kafka.cluster.Partition)
[2026-06-17 09:16:05,866] INFO [Partition __consumer_offsets-12 broker=0] Log loaded for partition __consumer_offsets-12 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,886] INFO [LogLoader partition=__consumer_offsets-21, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,887] INFO Created log for partition __consumer_offsets-21 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-21 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,887] INFO [Partition __consumer_offsets-21 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-21 (kafka.cluster.Partition)
[2026-06-17 09:16:05,887] INFO [Partition __consumer_offsets-21 broker=0] Log loaded for partition __consumer_offsets-21 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,905] INFO [LogLoader partition=__consumer_offsets-36, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,906] INFO Created log for partition __consumer_offsets-36 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-36 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,906] INFO [Partition __consumer_offsets-36 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-36 (kafka.cluster.Partition)
[2026-06-17 09:16:05,906] INFO [Partition __consumer_offsets-36 broker=0] Log loaded for partition __consumer_offsets-36 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,924] INFO [LogLoader partition=__consumer_offsets-6, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,924] INFO Created log for partition __consumer_offsets-6 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-6 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,925] INFO [Partition __consumer_offsets-6 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-6 (kafka.cluster.Partition)
[2026-06-17 09:16:05,925] INFO [Partition __consumer_offsets-6 broker=0] Log loaded for partition __consumer_offsets-6 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,937] INFO [LogLoader partition=__consumer_offsets-43, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,938] INFO Created log for partition __consumer_offsets-43 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-43 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,938] INFO [Partition __consumer_offsets-43 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-43 (kafka.cluster.Partition)
[2026-06-17 09:16:05,938] INFO [Partition __consumer_offsets-43 broker=0] Log loaded for partition __consumer_offsets-43 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,956] INFO [LogLoader partition=__consumer_offsets-13, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,956] INFO Created log for partition __consumer_offsets-13 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-13 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,957] INFO [Partition __consumer_offsets-13 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-13 (kafka.cluster.Partition)
[2026-06-17 09:16:05,957] INFO [Partition __consumer_offsets-13 broker=0] Log loaded for partition __consumer_offsets-13 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,973] INFO [LogLoader partition=__consumer_offsets-28, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:16:05,974] INFO Created log for partition __consumer_offsets-28 in /home/raslan/kafka-data/kafka-logs/__consumer_offsets-28 with properties {cleanup.policy=compact, compression.type="producer", segment.bytes=104857600} (kafka.log.LogManager)
[2026-06-17 09:16:05,974] INFO [Partition __consumer_offsets-28 broker=0] No checkpointed highwatermark is found for partition __consumer_offsets-28 (kafka.cluster.Partition)
[2026-06-17 09:16:05,975] INFO [Partition __consumer_offsets-28 broker=0] Log loaded for partition __consumer_offsets-28 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:16:05,989] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 3 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,991] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-3 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 18 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-18 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 41 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-41 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 10 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-10 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 33 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-33 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 48 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-48 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 19 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-19 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 34 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,994] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-34 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,994] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 4 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-4 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 11 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-11 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 26 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-26 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 49 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-49 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 39 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-39 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 9 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-9 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 24 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,995] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-24 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,995] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 31 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-31 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 46 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-46 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 1 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-1 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 16 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-16 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 2 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-2 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 25 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-25 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 40 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-40 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 47 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-47 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,996] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 17 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,996] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-17 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 32 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-32 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 37 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-37 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 7 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-7 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 22 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-22 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 29 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-29 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 44 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-44 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 14 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-14 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,997] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 23 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,997] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-23 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 38 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-38 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 8 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-8 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 45 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-45 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 15 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-15 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 30 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-30 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 0 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-0 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,998] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 35 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,998] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-35 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 5 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-5 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 20 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-20 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 27 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-27 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 42 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-42 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 12 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-12 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 21 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-21 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 36 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-36 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 6 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-6 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:05,999] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 43 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:05,999] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-43 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,000] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 13 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:06,000] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-13 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,000] INFO [GroupCoordinator 0]: Elected as the group coordinator for partition 28 in epoch 0 (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:06,000] INFO [GroupMetadataManager brokerId=0] Scheduling loading of offsets and group metadata from __consumer_offsets-28 for epoch 0 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,002] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-3 in 8 milliseconds for epoch 0, of which 3 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,004] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-18 in 10 milliseconds for epoch 0, of which 9 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,004] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-41 in 10 milliseconds for epoch 0, of which 10 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,005] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-10 in 11 milliseconds for epoch 0, of which 11 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,005] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-33 in 11 milliseconds for epoch 0, of which 11 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,006] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-48 in 12 milliseconds for epoch 0, of which 11 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,006] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-19 in 12 milliseconds for epoch 0, of which 12 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,007] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-34 in 13 milliseconds for epoch 0, of which 12 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,007] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-4 in 12 milliseconds for epoch 0, of which 12 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,008] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-11 in 13 milliseconds for epoch 0, of which 12 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,008] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-26 in 13 milliseconds for epoch 0, of which 13 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,009] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-49 in 14 milliseconds for epoch 0, of which 14 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,010] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-39 in 15 milliseconds for epoch 0, of which 15 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,011] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-9 in 15 milliseconds for epoch 0, of which 15 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,011] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-24 in 16 milliseconds for epoch 0, of which 16 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,012] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-31 in 16 milliseconds for epoch 0, of which 16 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,012] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-46 in 16 milliseconds for epoch 0, of which 16 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,013] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-1 in 17 milliseconds for epoch 0, of which 16 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,013] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-16 in 17 milliseconds for epoch 0, of which 17 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,013] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-2 in 17 milliseconds for epoch 0, of which 17 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,014] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-25 in 17 milliseconds for epoch 0, of which 17 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,014] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-40 in 18 milliseconds for epoch 0, of which 18 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,014] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-47 in 18 milliseconds for epoch 0, of which 18 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,015] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-17 in 19 milliseconds for epoch 0, of which 18 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,015] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-32 in 18 milliseconds for epoch 0, of which 18 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,015] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-37 in 18 milliseconds for epoch 0, of which 18 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,016] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-7 in 19 milliseconds for epoch 0, of which 18 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,016] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-22 in 19 milliseconds for epoch 0, of which 19 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,016] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-29 in 19 milliseconds for epoch 0, of which 19 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,017] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-44 in 20 milliseconds for epoch 0, of which 19 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,017] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-14 in 20 milliseconds for epoch 0, of which 20 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,017] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-23 in 20 milliseconds for epoch 0, of which 20 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,018] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-38 in 20 milliseconds for epoch 0, of which 19 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,018] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-8 in 20 milliseconds for epoch 0, of which 20 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,018] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-45 in 20 milliseconds for epoch 0, of which 20 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,019] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-15 in 21 milliseconds for epoch 0, of which 20 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,019] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-30 in 21 milliseconds for epoch 0, of which 21 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,019] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-0 in 21 milliseconds for epoch 0, of which 21 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,020] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-35 in 22 milliseconds for epoch 0, of which 21 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,020] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-5 in 21 milliseconds for epoch 0, of which 21 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,020] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-20 in 21 milliseconds for epoch 0, of which 21 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,021] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-27 in 22 milliseconds for epoch 0, of which 22 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,021] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-42 in 22 milliseconds for epoch 0, of which 22 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,022] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-12 in 23 milliseconds for epoch 0, of which 22 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,022] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-21 in 23 milliseconds for epoch 0, of which 23 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,022] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-36 in 23 milliseconds for epoch 0, of which 23 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,023] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-6 in 24 milliseconds for epoch 0, of which 24 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,023] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-43 in 23 milliseconds for epoch 0, of which 23 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,023] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-13 in 23 milliseconds for epoch 0, of which 23 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,023] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-28 in 23 milliseconds for epoch 0, of which 23 milliseconds was spent in the scheduler. (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:16:06,653] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group console-consumer-29451 in Empty state. Created a new member id console-consumer-5095fad1-b2a9-4aa4-ad99-6b6b85534e41 and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:06,666] INFO [GroupCoordinator 0]: Preparing to rebalance group console-consumer-29451 in state PreparingRebalance with old generation 0 (__consumer_offsets-2) (reason: Adding new member console-consumer-5095fad1-b2a9-4aa4-ad99-6b6b85534e41 with group instance id None; client reason: need to re-join with the given member-id: console-consumer-5095fad1-b2a9-4aa4-ad99-6b6b85534e41) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:06,674] INFO [GroupCoordinator 0]: Stabilized group console-consumer-29451 generation 1 (__consumer_offsets-2) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:16:06,701] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-5095fad1-b2a9-4aa4-ad99-6b6b85534e41 for group console-consumer-29451 for generation 1. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:21,577] INFO [GroupCoordinator 0]: Preparing to rebalance group console-consumer-29451 in state PreparingRebalance with old generation 1 (__consumer_offsets-2) (reason: Removing member console-consumer-5095fad1-b2a9-4aa4-ad99-6b6b85534e41 on LeaveGroup; client reason: the consumer is being closed) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:21,578] INFO [GroupCoordinator 0]: Group console-consumer-29451 with generation 2 is now empty (__consumer_offsets-2) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:21,582] INFO [GroupCoordinator 0]: Member MemberMetadata(memberId=console-consumer-5095fad1-b2a9-4aa4-ad99-6b6b85534e41, groupInstanceId=None, clientId=console-consumer, clientHost=/127.0.0.1, sessionTimeoutMs=45000, rebalanceTimeoutMs=300000, supportedProtocols=List(range, cooperative-sticky)) has left group console-consumer-29451 through explicit `LeaveGroup`; client reason: the consumer is being closed (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:25,399] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group console-consumer-92888 in Empty state. Created a new member id console-consumer-91d6203a-d1cf-4790-8ca7-0ac4e2e84366 and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:25,404] INFO [GroupCoordinator 0]: Preparing to rebalance group console-consumer-92888 in state PreparingRebalance with old generation 0 (__consumer_offsets-6) (reason: Adding new member console-consumer-91d6203a-d1cf-4790-8ca7-0ac4e2e84366 with group instance id None; client reason: need to re-join with the given member-id: console-consumer-91d6203a-d1cf-4790-8ca7-0ac4e2e84366) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:25,405] INFO [GroupCoordinator 0]: Stabilized group console-consumer-92888 generation 1 (__consumer_offsets-6) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:25,422] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-91d6203a-d1cf-4790-8ca7-0ac4e2e84366 for group console-consumer-92888 for generation 1. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:49,156] INFO [GroupCoordinator 0]: Preparing to rebalance group console-consumer-92888 in state PreparingRebalance with old generation 1 (__consumer_offsets-6) (reason: Removing member console-consumer-91d6203a-d1cf-4790-8ca7-0ac4e2e84366 on LeaveGroup; client reason: the consumer is being closed) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:49,157] INFO [GroupCoordinator 0]: Group console-consumer-92888 with generation 2 is now empty (__consumer_offsets-6) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:18:49,160] INFO [GroupCoordinator 0]: Member MemberMetadata(memberId=console-consumer-91d6203a-d1cf-4790-8ca7-0ac4e2e84366, groupInstanceId=None, clientId=console-consumer, clientHost=/127.0.0.1, sessionTimeoutMs=45000, rebalanceTimeoutMs=300000, supportedProtocols=List(range, cooperative-sticky)) has left group console-consumer-92888 through explicit `LeaveGroup`; client reason: the consumer is being closed (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:19:48,418] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group mon-groupe in Empty state. Created a new member id console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749 and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:19:48,422] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 0 (__consumer_offsets-23) (reason: Adding new member console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749 with group instance id None; client reason: need to re-join with the given member-id: console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:19:48,423] INFO [GroupCoordinator 0]: Stabilized group mon-groupe generation 1 (__consumer_offsets-23) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:19:48,442] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749 for group mon-groupe for generation 1. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:21:29,323] INFO [GroupMetadataManager brokerId=0] Group console-consumer-29451 transitioned to Dead in generation 2 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:21:29,330] INFO [GroupMetadataManager brokerId=0] Group console-consumer-92888 transitioned to Dead in generation 2 (kafka.coordinator.group.GroupMetadataManager)
[2026-06-17 09:22:43,686] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 1 (__consumer_offsets-23) (reason: Removing member console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749 on LeaveGroup; client reason: the consumer is being closed) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:22:43,686] INFO [GroupCoordinator 0]: Group mon-groupe with generation 2 is now empty (__consumer_offsets-23) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:22:43,688] INFO [GroupCoordinator 0]: Member MemberMetadata(memberId=console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749, groupInstanceId=None, clientId=console-consumer, clientHost=/127.0.0.1, sessionTimeoutMs=45000, rebalanceTimeoutMs=300000, supportedProtocols=List(range, cooperative-sticky)) has left group mon-groupe through explicit `LeaveGroup`; client reason: the consumer is being closed (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:25:21,506] INFO [NodeToControllerChannelManager id=0 name=forwarding] Node 0 disconnected. (org.apache.kafka.clients.NetworkClient)
[2026-06-17 09:27:48,281] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group mon-groupe in Empty state. Created a new member id console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:27:48,286] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 2 (__consumer_offsets-23) (reason: Adding new member console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f with group instance id None; client reason: need to re-join with the given member-id: console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:27:48,287] INFO [GroupCoordinator 0]: Stabilized group mon-groupe generation 3 (__consumer_offsets-23) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:27:48,302] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f for group mon-groupe for generation 3. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:28:26,745] INFO Creating 1 partitions for 'premier-topic' with the following replica assignment: HashMap(1 -> ReplicaAssignment(replicas=0, addingReplicas=, removingReplicas=)). (kafka.zk.AdminZkClient)
[2026-06-17 09:28:26,772] INFO [Controller id=0, targetBrokerId=0] Node 0 disconnected. (org.apache.kafka.clients.NetworkClient)
[2026-06-17 09:28:26,775] INFO [ReplicaFetcherManager on broker 0] Removed fetcher for partitions Set(premier-topic-1) (kafka.server.ReplicaFetcherManager)
[2026-06-17 09:28:26,782] INFO [LogLoader partition=premier-topic-1, dir=/home/raslan/kafka-data/kafka-logs] Loading producer state till offset 0 with message format version 2 (kafka.log.UnifiedLog$)
[2026-06-17 09:28:26,783] INFO Created log for partition premier-topic-1 in /home/raslan/kafka-data/kafka-logs/premier-topic-1 with properties {} (kafka.log.LogManager)
[2026-06-17 09:28:26,784] INFO [Partition premier-topic-1 broker=0] No checkpointed highwatermark is found for partition premier-topic-1 (kafka.cluster.Partition)
[2026-06-17 09:28:26,784] INFO [Partition premier-topic-1 broker=0] Log loaded for partition premier-topic-1 with initial high watermark 0 (kafka.cluster.Partition)
[2026-06-17 09:29:36,033] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group mon-groupe in Stable state. Created a new member id console-consumer-ba1edd17-53ce-41ed-8933-a8c449c0d839 and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:29:36,038] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 3 (__consumer_offsets-23) (reason: Adding new member console-consumer-ba1edd17-53ce-41ed-8933-a8c449c0d839 with group instance id None; client reason: need to re-join with the given member-id: console-consumer-ba1edd17-53ce-41ed-8933-a8c449c0d839) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:29:36,352] INFO [GroupCoordinator 0]: Stabilized group mon-groupe generation 4 (__consumer_offsets-23) with 2 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:29:36,364] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f for group mon-groupe for generation 4. The group has 2 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:32:48,398] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 4 (__consumer_offsets-23) (reason: Leader console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f re-joining group during Stable; client reason: cached metadata has changed) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:32:48,446] INFO [GroupCoordinator 0]: Stabilized group mon-groupe generation 5 (__consumer_offsets-23) with 2 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 09:32:48,450] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f for group mon-groupe for generation 5. The group has 2 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:18:58,962] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 5 (__consumer_offsets-23) (reason: Removing member console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f on LeaveGroup; client reason: the consumer is being closed) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:18:58,963] INFO [GroupCoordinator 0]: Member MemberMetadata(memberId=console-consumer-b03b7eeb-e100-4aea-a747-aca9a6411b6f, groupInstanceId=None, clientId=console-consumer, clientHost=/127.0.0.1, sessionTimeoutMs=45000, rebalanceTimeoutMs=300000, supportedProtocols=List(range, cooperative-sticky)) has left group mon-groupe through explicit `LeaveGroup`; client reason: the consumer is being closed (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:01,150] INFO [GroupCoordinator 0]: Stabilized group mon-groupe generation 6 (__consumer_offsets-23) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:01,177] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-ba1edd17-53ce-41ed-8933-a8c449c0d839 for group mon-groupe for generation 6. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:03,133] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group groupe-A in Empty state. Created a new member id console-consumer-dcba5333-075c-45d5-9fe2-650ff14cadac and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:03,137] INFO [GroupCoordinator 0]: Preparing to rebalance group groupe-A in state PreparingRebalance with old generation 0 (__consumer_offsets-34) (reason: Adding new member console-consumer-dcba5333-075c-45d5-9fe2-650ff14cadac with group instance id None; client reason: need to re-join with the given member-id: console-consumer-dcba5333-075c-45d5-9fe2-650ff14cadac) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:03,139] INFO [GroupCoordinator 0]: Stabilized group groupe-A generation 1 (__consumer_offsets-34) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:03,154] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-dcba5333-075c-45d5-9fe2-650ff14cadac for group groupe-A for generation 1. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:42,700] INFO [GroupCoordinator 0]: Preparing to rebalance group mon-groupe in state PreparingRebalance with old generation 6 (__consumer_offsets-23) (reason: Removing member console-consumer-ba1edd17-53ce-41ed-8933-a8c449c0d839 on LeaveGroup; client reason: the consumer is being closed) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:42,700] INFO [GroupCoordinator 0]: Group mon-groupe with generation 7 is now empty (__consumer_offsets-23) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:42,701] INFO [GroupCoordinator 0]: Member MemberMetadata(memberId=console-consumer-ba1edd17-53ce-41ed-8933-a8c449c0d839, groupInstanceId=None, clientId=console-consumer, clientHost=/127.0.0.1, sessionTimeoutMs=45000, rebalanceTimeoutMs=300000, supportedProtocols=List(range, cooperative-sticky)) has left group mon-groupe through explicit `LeaveGroup`; client reason: the consumer is being closed (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:46,966] INFO [GroupCoordinator 0]: Dynamic member with unknown member id joins group groupe-B in Empty state. Created a new member id console-consumer-c8f955ce-0f35-4bc2-a235-650165601b0f and request the member to rejoin with this id. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:46,971] INFO [GroupCoordinator 0]: Preparing to rebalance group groupe-B in state PreparingRebalance with old generation 0 (__consumer_offsets-35) (reason: Adding new member console-consumer-c8f955ce-0f35-4bc2-a235-650165601b0f with group instance id None; client reason: need to re-join with the given member-id: console-consumer-c8f955ce-0f35-4bc2-a235-650165601b0f) (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:46,972] INFO [GroupCoordinator 0]: Stabilized group groupe-B generation 1 (__consumer_offsets-35) with 1 members (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:19:46,989] INFO [GroupCoordinator 0]: Assignment received from leader console-consumer-c8f955ce-0f35-4bc2-a235-650165601b0f for group groupe-B for generation 1. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
[2026-06-17 10:22:36,182] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.SocketException: Connection reset
        at java.base/sun.nio.ch.SocketChannelImpl.throwConnectionReset(SocketChannelImpl.java:394)
        at java.base/sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:426)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doIO(ClientCnxnSocketNIO.java:74)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:350)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:38,202] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:38,204] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:39,516] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:39,517] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:41,516] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:41,518] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:43,504] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:43,505] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:44,969] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:44,969] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:46,324] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:46,324] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:47,467] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:47,467] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:48,956] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:48,957] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:50,253] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:50,255] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:52,310] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:52,311] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:53,687] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:53,688] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:55,304] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:55,305] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:56,751] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:56,752] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:58,601] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:58,602] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:22:59,852] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:22:59,852] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:01,788] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:01,790] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:03,814] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:03,816] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:04,989] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:04,990] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:06,849] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:06,851] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:08,421] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:08,422] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:10,223] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:10,224] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:11,365] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:11,366] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:13,214] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:13,215] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:15,127] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:15,129] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:16,927] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:16,927] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:18,122] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:18,123] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:19,636] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:19,637] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:21,098] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:21,099] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:23,077] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:23,078] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:24,295] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:24,296] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:25,796] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:25,797] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:27,087] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:27,088] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:28,429] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:28,430] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:30,325] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:30,326] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:31,436] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:31,437] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:32,727] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:32,728] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:34,494] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:34,495] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:36,531] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:36,533] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:37,789] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:37,790] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:38,907] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:38,908] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:40,556] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:40,556] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:41,860] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:41,862] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:43,767] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:43,768] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:45,412] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:45,413] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:46,765] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:46,767] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:48,224] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:48,225] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:49,697] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:49,697] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:51,568] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:51,569] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:53,664] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:53,665] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:54,874] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:54,875] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:55,996] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:55,997] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:57,452] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:57,453] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:23:59,093] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:23:59,095] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:00,399] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:00,401] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:01,681] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:01,682] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:03,118] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:03,118] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:05,022] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:05,023] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:06,215] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:06,217] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:07,361] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:07,362] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:08,719] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:08,719] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:10,612] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:10,612] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:12,461] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:12,462] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:13,939] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:13,940] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:16,020] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:16,021] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:18,061] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:18,063] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:19,926] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:19,927] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:21,171] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:21,172] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:23,000] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:23,000] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:24,679] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:24,679] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:26,016] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:26,017] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:27,875] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:27,876] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:29,867] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:29,868] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:31,945] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:31,946] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:33,602] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:33,603] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:35,230] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:35,231] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:37,087] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:37,088] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:38,776] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:38,777] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:40,412] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:40,413] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:42,414] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:42,415] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:43,794] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:43,795] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:45,247] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:45,248] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:46,829] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:46,830] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:48,106] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:48,107] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:49,753] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:49,755] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:51,740] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:51,741] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:53,821] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:53,823] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:55,808] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:55,809] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:57,647] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:57,648] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:24:58,857] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:24:58,858] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:00,107] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:00,108] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:01,298] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:01,298] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:02,462] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:02,463] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:03,782] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:03,783] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:05,843] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:05,844] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:07,839] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:07,840] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:09,889] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:09,890] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:11,758] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:11,759] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:13,709] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:13,710] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:14,970] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:14,972] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:16,347] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:16,348] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:17,991] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:17,991] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:19,125] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:19,126] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:20,492] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:20,493] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:22,402] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:22,403] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:23,805] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:23,806] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:25,097] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:25,099] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
java.net.ConnectException: Connection refused
        at java.base/sun.nio.ch.Net.pollConnect(Native Method)
        at java.base/sun.nio.ch.Net.pollConnectNow(Net.java:684)
        at java.base/sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:946)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:344)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1289)
[2026-06-17 10:25:27,133] INFO Opening socket connection to server localhost/127.0.0.1:2181. (org.apache.zookeeper.ClientCnxn)
[2026-06-17 10:25:27,134] WARN Session 0x1000064cf1a0000 for server localhost/127.0.0.1:2181, Closing socket connection. Attempting reconnect except it is a SessionExpiredException. (org.apache.zookeeper.ClientCnxn)
```

---

# terminal 3 : 
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic premier-topic
>Hello Romain
>Romain est tro nul au Padel et tous les sports combines
>Hello from T3
>Hello from T3 (2)
>Hello from T3 (3)
>Hello from T3 (4)
>HEllo from T3 (5)
>Hello from T3 (6)
>^Craslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ ^C
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic premier-topic \
>   --property parse.key=true --property key.separator=:
>a:msg1
>b:msg2
>c:msg3
>d:msg4
>e:msg5
>f:msg6
>test groupe A et B
org.apache.kafka.common.KafkaException: No key separator found on line number 7: 'test groupe A et B'
        at kafka.tools.ConsoleProducer$LineMessageReader.kafka$tools$ConsoleProducer$LineMessageReader$$parse(ConsoleProducer.scala:438)
        at kafka.tools.ConsoleProducer$LineMessageReader$$anon$3.hasNext(ConsoleProducer.scala:408)
        at kafka.tools.ConsoleProducer$.loopReader(ConsoleProducer.scala:91)
        at kafka.tools.ConsoleProducer$.main(ConsoleProducer.scala:100)
        at kafka.tools.ConsoleProducer.main(ConsoleProducer.scala)
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic premier-topic   --property parse.key=true --property key.separator=:
>g: test groupe A et B
>
```

---

# terminal 4 : 
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic
Hello Romain
Romain est tro nul au Padel et tous les sports combines
^CProcessed a total of 3 messages
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --from-beginning
Hello Romain
Romain est tro nul au Padel et tous les sports combines
^CProcessed a total of 3 messages
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --partition 0 --offset earliest
Hello Romain
Romain est tro nul au Padel et tous les sports combines
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group mon-groupe --from-beginning^CProcessed a total of 3 messages
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group mon-groupe --from-beginning
Hello Romain
Romain est tro nul au Padel et tous les sports combines
^CProcessed a total of 3 messages
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group mon-groupe --from-beginning
Hello Romain
Romain est tro nul au Padel et tous les sports combines
Hello from T3
Hello from T3 (2)
Hello from T3 (3)
Hello from T3 (4)
HEllo from T3 (5)
Hello from T3 (6)
msg1
msg2
msg3
msg5
^CProcessed a total of 13 messages
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group groupe-A
 test groupe A et B
```

---

# terminal 5 : 
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
console-consumer-29451
console-consumer-92888
mon-groupe
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group mon-groupe

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                           HOST            CLIENT-ID
mon-groupe      premier-topic   0          3               3               0               console-consumer-1bd3cf36-8697-41e4-ae37-0f0614d52749 /127.0.0.1      console-consumerraslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mon-groupe --reset-offsets --to-earliest --topic premier-topic --execute

Error: Assignments can only be reset if the group 'mon-groupe' is inactive, but the current state is Stable.

raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mon-groupe --reset-offsets --to-earliest --topic premier-topic --execute

Error: Assignments can only be reset if the group 'mon-groupe' is inactive, but the current state is Stable.

GROUP                          TOPIC                          PARTITION  NEW-OFFSET     raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ ^C
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mon-groupe --reset-offsets --to-earliest --topic premier-topic --execute

GROUP                          TOPIC                          PARTITION  NEW-OFFSET     mon-groupe                     premier-topic                  0          0              raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ ^C
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic premier-topic --partitions 2
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic premier-topic
Topic: premier-topic    TopicId: WV18z8nWQ8yekl_6282UEQ PartitionCount: 2       ReplicationFactor: 1    Configs:
        Topic: premier-topic    Partition: 0    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
        Topic: premier-topic    Partition: 1    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$
```

---

# terminal 6 : 
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group mon-groupe --from-beginning
msg4
msg6
^CProcessed a total of 2 messages
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group groupe-B
 test groupe A et B
```

---

# terminal de verifications finals : 
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic premier-topic
Topic: premier-topic    TopicId: WV18z8nWQ8yekl_6282UEQ PartitionCount: 2       ReplicationFactor: 1    Configs:
        Topic: premier-topic    Partition: 0    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
        Topic: premier-topic    Partition: 1    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
groupe-A
groupe-B
mon-groupe
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$
```

---
# kafka

## cli

```shell
kafka-topics.sh --create --topic aytopic --bootstrap-server localhost:9092
```

```shell
kafka-topics.sh --create --topic aytopic --bootstrap-server localhost:9092 --partitions <num_partitions> --replication-factor <replication_factor>
```

```shell
kafka-topics.sh --list --bootstrap-server localhost:9092
```

```shell
kafka-topics.sh --describe --topic aytopic --bootstrap-server localhost:9092
```

```shell
kafka-topics.sh --delete --topic aytopic --bootstrap-server localhost:9092
```

```shell
kafka-console-producer.sh --topic aytopic --bootstrap-server localhost:9092
```

```shell
kafka-console-consumer.sh --topic aytopic --bootstrap-server localhost:9092 --from-beginning
```

```shell
kafka-console-consumer.sh --topic <topic_name> --bootstrap-server <broker_host>:<broker_port> --group <group_id>
```

```shell
kafka-consumer-groups.sh --list --bootstrap-server <broker_host>:<broker_port>
```

```shell
kafka-consumer-groups.sh --describe --group <group_id> --bootstrap-server <broker_host>:<broker_port>
```

```shell
kafka-consumer-groups.sh --reset-offsets --group <group_id> --bootstrap-server <broker_host>:<broker_port> --to-earliest --execute --topic <topic_name>
```

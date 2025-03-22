CREATE KEYSPACE IF NOT EXISTS data WITH REPLICATION =
{ 'class' : 'SimpleStrategy',
'replication_factor' : '1'
};

CREATE TABLE IF NOT EXISTS data.messages1 (
    insertion_date timestamp PRIMARY KEY,
    msg text
);

CREATE TABLE IF NOT EXISTS data.messages2 (
    insertion_date timestamp PRIMARY KEY,
    msg text
);
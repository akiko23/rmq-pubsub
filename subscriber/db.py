from cassandra.cluster import Cluster
from datetime import datetime


class Database:
    def __init__(self, msg_table_name: str, cassandra_host: str = "127.0.0.1") -> None:
        self._session = Cluster([cassandra_host]).connect()
        self._table_name = msg_table_name

    def add_message(self, text: str):
        self._session.execute(
            "INSERT INTO " + f"data.{self._table_name}" + " (insertion_date, msg) values (%s, %s)",
            (datetime.now(), text)
        )

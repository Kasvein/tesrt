import os
import tempfile

from client_db import init_db, add_client, list_clients


def test_add_and_list_clients():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        db_path = tmp.name
    try:
        init_db(db_path)
        add_client("Alice", "alice@example.com", db_path)
        add_client("Bob", "bob@example.com", db_path)
        clients = list_clients(db_path)
        assert clients == [
            (1, "Alice", "alice@example.com"),
            (2, "Bob", "bob@example.com"),
        ]
    finally:
        os.remove(db_path)

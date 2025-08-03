import sqlite3
from typing import List, Tuple

DB_NAME = "clients.db"

def init_db(db_name: str = DB_NAME) -> None:
    """Initialize the database and create the clients table if it doesn't exist."""
    with sqlite3.connect(db_name) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """
        )


def add_client(name: str, email: str, db_name: str = DB_NAME) -> None:
    """Add a client to the database."""
    with sqlite3.connect(db_name) as conn:
        conn.execute(
            "INSERT INTO clients (name, email) VALUES (?, ?)", (name, email)
        )


def list_clients(db_name: str = DB_NAME) -> List[Tuple[int, str, str]]:
    """Return a list of all clients as (id, name, email) tuples."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.execute(
            "SELECT id, name, email FROM clients ORDER BY id"
        )
        return list(cursor.fetchall())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Client database application")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new client")
    add_parser.add_argument("name", help="Name of the client")
    add_parser.add_argument("email", help="Email of the client")

    subparsers.add_parser("list", help="List all clients")

    args = parser.parse_args()
    init_db()

    if args.command == "add":
        add_client(args.name, args.email)
        print("Client added.")
    elif args.command == "list":
        for client in list_clients():
            print(f"{client[0]}: {client[1]} <{client[2]}>")
    else:
        parser.print_help()

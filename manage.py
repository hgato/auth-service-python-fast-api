#!/usr/bin/env python3
"""Management CLI for the auth service."""
import sys
from src.migrations import migrate_db


def run_migrations():
    """Run database migrations."""
    print("Running migrations...")
    try:
        migrate_db()
        print("Migrations completed successfully!")
    except Exception as e:
        print(f"Error running migrations: {e}")
        sys.exit(1)


def main():
    """Main entry point for the management CLI."""
    if len(sys.argv) < 2:
        print("Usage: python manage.py <command>")
        print("Available commands:")
        print("  migrate - Run database migrations")
        sys.exit(1)

    command = sys.argv[1]

    if command == "migrate":
        run_migrations()
    else:
        print(f"Unknown command: {command}")
        print("Available commands:")
        print("  migrate - Run database migrations")
        sys.exit(1)


if __name__ == "__main__":
    main()

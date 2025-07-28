#!/bin/sh

# $1 = host (e.g., postgres_db)
host="$1"
shift

echo "Waiting for PostgreSQL at $host:5432..."

# Loop until the PostgreSQL port is reachable
until nc -z "$host" 5432; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - executing command"
exec "$@"

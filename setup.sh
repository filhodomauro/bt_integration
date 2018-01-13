#!/bin/sh
pip install requests
echo "Installing google libs..."
pip install google-auth google-auth-httplib2 google-api-python-client
echo "Installing requests..."
pip install "requests[security]"
echo "Installing sqlite3..."
sudo apt-get install sqlite3
export SQLITE3_DBS="${HOME}/.sqlite3"
export DB_NAME=bitcointrade.db
if [ ! -d "$SQLITE3_DBS" ]; then
  echo "Creating ${DB_NAME}..."
  mkdir $SQLITE3_DBS
fi
export DB_PATH="${SQLITE3_DBS}/${DB_NAME}"
echo "Importing scripts to DB ${DB_PATH}"
sqlite3 $DB_PATH < script.sql
echo "Done"

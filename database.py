import harperdb

from secret import HARPERDB_PASSWORD, HARPERDB_USERNAME, HARPERDB_URL

db = harperdb.HarperDB(
    url = HARPERDB_URL,
    username = HARPERDB_USERNAME,
    password = HARPERDB_PASSWORD
    )



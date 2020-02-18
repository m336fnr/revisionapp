import sys
import logging
#import rds_config
import pymysql
#rds settings
rds_host  = "myrevisionappdbid.c1ne2me9anxz.eu-west-2.rds.amazonaws.com"

#name = rds_config.db_username
#password = rds_config.db_password
#db_name = rds_config.db_name

name = 'admin'
password = 'Triumph600'
db_name = 'revisionappdb'

logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    item_count = 0
    with conn.cursor() as cur:
        cur.execute('insert into SUBJECTS (SUBJECT) values("CS")')
        cur.execute('insert into SUBJECTS (SUBJECT) values("ENG")')
        cur.execute('insert into SUBJECTS (SUBJECT) values("BIO")')
        conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)
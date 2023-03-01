import os


def file_exists(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError("{0} file does not exist!".format(filename))


def track_load(conn, table_name, record, success, error_message=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO metadata (destination_table, record, success, error_message) VALUES (%s, %s, %s, %s)",
        (table_name, record, success, error_message)
    )
    conn.commit()
    cur.close()

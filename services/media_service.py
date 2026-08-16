import os

try:
    import mariadb
except ImportError:  # pragma: no cover - optional dependency in local dev setups
    mariadb = None


def get_media_items():
    """Fetch all media rows from the database and normalize them for the template."""
    if mariadb is None:
        print("mariadb is not installed; returning an empty media list.")
        return []

    data = []
    try:
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'wonderrxjr',
            'password': os.getenv('dbpass'),
            'database': 'website',
        }
        conn = mariadb.connect(**config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM media")
        rows = cur.fetchall()

        for row in rows:
            data.append({
                'name': row[1],
                'medium': row[2],
                'platform': row[3],
                'notes': row[4],
            })

        conn.close()
        data = sorted(data, key=lambda item: item['name'])
    except mariadb.Error as exc:
        print(f"Error connecting to MariaDB Platform: {exc}")

    return data

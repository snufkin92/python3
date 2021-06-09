import psycopg2

# url = "postgresql://{ユーザ名}:{パスワード}@localhost:5432/postgres"
url = "postgresql://@localhost:5432/postgres"

with psycopg2.connect(url) as conn:

    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public.links;')
        print(cur.query)

        rows = cur.fetchall()

        for row in rows:
            print(row)

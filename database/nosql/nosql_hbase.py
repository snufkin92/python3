import happybase

'''
外部からアクセスできるように起動後 hbase　thrift start を実行
実行しないと
thriftpy2.transport.base.TTransportExceptionが発生
'''

conn = None

try:
    conn = happybase.Connection("localhost")
    conn.open()

    # create 'qiita', 'article'
    # 文字列はバイナリ(b)にしないとエラー発生
    conn.create_table(b"qiita", {"article": dict()})

    # put 'qiita', 'user_1', 'article:java', 'generics'
    # put 'qiita', 'user_2', 'article:python', 'scikit-learn'
    # put 'qiita', 'user_2', 'article:R', 'data.frame'
    table = conn.table(b"qiita")
    table.put(
        b"user_1", {
            b"article:java": "generics"
        }
    )

    table.put(
        b"user_2", {
            b"article:python": "scikit-learn"
            , b"article:R": "data.frame"
        }
    )

    print("### full scan:", list(table.scan()))
    print("### filter scan:", list(table.scan(row_prefix=b"user_2")))

finally:
    if conn:
        # disable 'qiita'
        conn.disable_table("qiita")

        # drop 'qiita'
        conn.delete_table("qiita")
        conn.close()

    print("### end")

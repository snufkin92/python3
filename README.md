いつも忘れるので備忘録

# パッケージング

tar.gzで固める場合

```
$ python setup.py sdist
```

[pipでインストールさせたい場合はこちらを参照](https://buildersbox.corp-sansan.com/entry/2019/07/11/110000)

# 　構文

## `if __name__ == '__main__'`
インポートされた際、意図しないコードの実行を防ぐお作法  
`__name__`は実行されているモジュール名を格納する予約語。実行しているモジュール本体の場合は`__main__`となる

## `__init__.py`
パッケージ配下のモジュールが読み込まれた際に前処理が行われるモジュール    
パッケージ配下のモジュールをアスタリスクを使って一括でimportしたい場合に使用される事が多い

## 属性
カプセル化

## `__init__ と　__new__`
`__new__`はインスタンス生成前に呼ばれ、クラスの初期化、`__init__`はインスタンス生成後に呼ばれインスタンスの初期化を行う

## ジェネレーター(generator)

シーケンスを作成する **オブジェクト**

関数の戻り値が yeild となるイメージで、イテレータのデータソースとなる場合が多い

例えば、値を格納されたリストを返すとメモリを消費するが、ジェネレータを使えば 定義（どんな値を格納するか）だけを返され、値を利用するまでリソースを節約できる

反復処理の度、最後にアクセスした場所を記憶してくれる

## 内包表記(comprehension )

1行でforループ分を表現する記述方法

タプルには内包表記はなく、ジェネレータ内包表記となる

## クロージャ(closure)

動的に生成される関数内関数（デコレータもクロージャ）

## ラムダ関数(lambda function)

1行で表現される無名（匿名）関数

# DB

## RDB

- PostgreSQL
- sqlalchemy with sqlite

## Key-Value

- dbm
- memcache

## No-SQL

- [MmongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
  サービス化していない場合は、次のコマンドで起動

```
$ mongod --dbpath データの格納先
```

ちなみにmongoシェルの起動は

```
$ mongo
```

[以下は、よく忘れるので](#参照)

|RDBでの呼称|MongoDBでの呼称|
|:---|:---|
|database|database|
|table|collection|
|row|document|
|column|field|

## Big Data

- [HBase](https://thinkit.co.jp/article/11882) ：NoSQLに分類される列志向データベース

サービス化していない場合は、次のコマンドで起動

```
$ start-hbase.sh
```

pythonなど外部からアクセスする場合は、起動後に次のコマンドも起動

```
$ hbase　thrift start
```

シェルを起動

```
$ hbase shell
```

create テーブル名 カラムファミリー名

```
> create 'qiita', 'article'
```

データ投入

```
> put 'qiita', 'user_1', 'article:java', 'generics'
> put 'qiita', 'user_2', 'article:python', 'scikit-learn' 
> put 'qiita', 'user_2', 'article:R', 'data.frame' 
```

確認（この後、pythonからアクセス）

```
hbase:***:*> scan 'qiita'
ROW                                           COLUMN+CELL                                                                                                                          
 user_1                                       column=article:java, timestamp=2021-06-09T14:10:27.135, value=generics                                                               
 user_2                                       column=article:python, timestamp=2021-06-09T14:10:33.359, value=scikit-learn                                                         
 user_2                                       column=article:R, timestamp=2021-06-09T14:11:35.321, value=data.frame     
```

削除

```
> disable 'qiita'
> drop 'qiita'
```

停止（シェルを抜けた後）

```
$ stop-hbase.sh
```

## GraphDB

- [Neo4j](https://neo4j.com/docs/api/python-driver/current/)

初期設定

|ユーザ名|パスワード|ポート|管理コンソール用ポート|
|:---|:---|:---|:---|
|neo4j|neo4j|7687|7474|

サービス化していない場合は、次のコマンドで起動

```
$ neo4j start
```

停止

```
$ neo4j stop
```

確認

```
$ neo4j status
```

管理コンソール

```
$ open http://localhost:7474
```

# テスト

## unittest

python標準のユニットテストフレームワーク

## pytest

unittestより高機能なテストフレームワーク

# web関連

## よく使用さえるフォーマット

- xml
- json

## rest

urllib、requestsモジュールによるrest

- get
- post

## flask

軽量Webアプリフレームワーク

# 参照

[第3回　MongoDBのクエリを使いこなそう](https://gihyo.jp/dev/serial/01/mongodb/0003)


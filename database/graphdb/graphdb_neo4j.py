from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
# uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "1qazxsw2"))


def clear_db(tx):
    """
    データを全削除
    """
    tx.run("MATCH (n) DETACH DELETE n")


def create_friend_of(tx, name, friend):
    """
    name を持つ Person は friend を知っている
    """
    if tx.run("MATCH (p:Person) WHERE p.name = $name RETURN p", name=name).single() is None:
        print(f"### create person:{name}")
        tx.run("CREATE (:Person {name: $name, country: 'US', age: 16 })", name=name)

    # 関係性を作成
    persons = tx.run("MATCH (p:Person) WHERE p.name = $name "
                     "CREATE (p)-[:KNOWS]->(f:Person {name: $friend}) RETURN p"
                     , name=name, friend=friend
                     )

    """
    この段階でpersonは　'neo4j.work.result.Result'　であり、このメソッド外から参照できない
    sessionとは関係ない 'neo4j.data.Record' ならば戻せる
    single() で 'neo4j.data.Record'
    [0]　(["p"]でもOK） で　'neo4j.graph.Node'　を返している
    """
    # return persons.values()
    return persons.single()[0]


def get_all_friend(tx, country):
    persons = tx.run("MATCH (p:Person) <-[:KNOWS]-(f) RETURN f")

    # TODO:countryに対するフィルタリング
    # persons = tx.run("MATCH (p:Person {country:$country})<-[:KNOWS]-(f) RETURN f", country=country)
    # persons = tx.run("MATCH (p:Person) WHERE p.country=$country<-[:KNOWS]-(f) RETURN f", country=country)
    # persons = tx.run("MATCH (p:Person)<-[:KNOWS]-(f) WHERE p.country=$country RETURN f", country=country)

    # 'neo4j.work.result.Result' に対して for-loop を実行すると person は 'neo4j.data.Record'
    results = []
    for _person in persons:
        results.append(_person[0])
        # print("### the person has KNOWS relationship: ", _person[0]["name"], _person[0]["country"])
    return results


try:
    # 何度も試す為に、データを全削除
    with driver.session() as session:
        session.write_transaction(clear_db)

    # AliceはBobを知っているという関係を作成
    with driver.session() as session:

        # write_transactionは戻り値がNoneになるので注意
        alice = session.write_transaction(create_friend_of, "Alice", "Bob")
        print(f"name={alice['name']} , country={alice['country']}, age={alice['age']}")

        #
        session.write_transaction(create_friend_of, "Nancy", "Mike")

        # KNOWSリレーションを持つ人物一覧
        persons = session.write_transaction(get_all_friend, "US")
        for person in persons:
            print(f"### the person has KNOWS relationship: name={person['name']}, country={person['country']}")

finally:
    if driver:
        driver.close()

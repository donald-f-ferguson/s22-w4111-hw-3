from py2neo import data, Graph, NodeMatcher, Node, Relationship, RelationshipMatcher

def tt():
    g = Graph(
        "neo4j+s://47647603.databases.neo4j.io:7687",
        auth=("neo4j",
              "IbqRvHo2SB-J90ITWdsA5rsXBHvT_HvIUATtUNKAjLg")
    )
    q = "match (p:Person) return p"
    res = g.run(q)

    for r in res:
        print(r)


tt()

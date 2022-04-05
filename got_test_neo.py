from got_graph_v2 import GotGraph


def get_graph():

    g = GotGraph(url="neo4j+s://47647603.databases.neo4j.io:7687",
                 auth = ("neo4j", "IbqRvHo2SB-J90ITWdsA5rsXBHvT_HvIUATtUNKAjLg")
                 )
    return g


def t1():
    g = get_graph()
    q = "match (p:Person) where p.name=$name return p"
    res = g.run_q(q, {"name": "Tom Hanks"})
    print(type(res))
    for r in res:
        print(type(r))
        print(r)
        print("Labels = ", r['p'].labels)
        print("Properties = ", dict(r['p']))



t1()
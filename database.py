from neo4j import GraphDatabase


class GraphDB:
    def __init__(self, uri, user, password):
        self.uri = "bolt://localhost:7687"
        self.username = "neo4j"
        self.password = "Yash7421"
        self.driver = GraphDatabase.driver(self.uri, auth=(self.username, self.password))

    def close(self):
        self.driver.close()

    def store_paper(self, topic, title, year, summary):
        query = """
        MERGE (t:Topic {name: $topic})
        CREATE (p:Paper {title: $title, year: $year, summary: $summary})
        MERGE (t)-[:HAS_PAPER]->(p)
        """
        with self.driver.session() as session:
            session.run(query, topic=topic, title=title, year=year, summary=summary)

    def get_papers_by_year(self, topic, year):
        query = """
        MATCH (t:Topic {name: $topic})-[:HAS_PAPER]->(p:Paper {year: $year})
        RETURN p.title, p.summary
        """
        with self.driver.session() as session:
            results = session.run(query, topic=topic, year=year)
            return [{"title": r["p.title"], "summary": r["p.summary"]} for r in results]

    def get_all_papers(self, topic):
        query = """
        MATCH (t:Topic {name: $topic})-[:HAS_PAPER]->(p:Paper)
        RETURN p.title, p.year, p.summary
        """
        with self.driver.session() as session:
            results = session.run(query, topic=topic)
            return [{"title": r["p.title"], "year": r["p.year"], "summary": r["p.summary"]} for r in results]

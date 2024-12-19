from rdflib import Graph, Namespace

# Load the ontology
rdf_graph = Graph()
rdf_graph.parse("shape.owl", format="xml")

# Define the namespace
SHAPE = Namespace("http://www.example.org/shape.owl#")

# SPARQL query
sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX shape: <http://www.example.org/shape.owl#>

SELECT ?shape ?description ?property ?application ?formula
WHERE {
  ?shape rdf:type shape:Shape .
  OPTIONAL { ?shape shape:description ?description . }
  OPTIONAL { ?shape shape:property ?property . }
  OPTIONAL { ?shape shape:application ?application . }
  OPTIONAL { ?shape shape:formula ?formula . }
}
"""

# Execute the query
results = rdf_graph.query(sparql_query)

# Print the results
print("Query Results:")
for row in results:
    print(f"Shape: {row.shape}")
    print(f"  Description: {row.description}")
    print(f"  Property: {row.property}")
    print(f"  Application: {row.application}")
    print(f"  Formula: {row.formula}")
    print("-" * 40)

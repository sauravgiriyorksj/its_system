from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os, re
from rdflib import Graph, Namespace


app = FastAPI(title="Shape Learning")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)


FILE_NAME = "shape.owl"


rdf_graph = Graph()
rdf_graph.parse(FILE_NAME, format="xml")


SHAPE = Namespace("http://www.example.org/shape.owl#")


IMAGE_FOLDER = "images"
BASE_IMAGE_URL = "http://localhost:8000"

def get_image_url(name):
    name = re.sub(r'\s+', '_', name).lower()
    image_path = os.path.join(IMAGE_FOLDER, f"{name}.png")
    if os.path.exists(image_path):
        return f"{BASE_IMAGE_URL}/{image_path}"
    return None


app.mount("/images", StaticFiles(directory=IMAGE_FOLDER), name="images")

@app.get("/shapes")
def get_all_shapes():
    sparql_query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX shape: <http://www.example.org/shape.owl#>

    SELECT ?shape ?name ?description ?property ?application ?formula
    WHERE {
      ?shape rdf:type shape:Shape .
      OPTIONAL { ?shape shape:description ?description . }
      OPTIONAL { ?shape shape:property ?property . }
      OPTIONAL { ?shape shape:application ?application . }
      OPTIONAL { ?shape shape:formula ?formula . }
    }
    """
    results = rdf_graph.query(sparql_query)
    shapes = []

    for row in results:
        shape = str(row.shape)
        description = str(row.description) if row.description else None
        property = str(row.property) if row.property else None
        application = str(row.application) if row.application else None
        formula = str(row.formula) if row.formula else None
        name = shape.split("#")[-1]  
        image_url = get_image_url(name)

        shapes.append({
            "name": name,
            "description": description,
            "property": property,
            "application": application,
            "formula": formula,
            "image_url": image_url
        })

    return {"shapes": shapes}

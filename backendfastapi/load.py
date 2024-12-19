from owlready2 import *

# File name for the ontology
FILE_NAME = "shape.owl"

# Create or load the ontology
onto = get_ontology(f"http://www.example.org/{FILE_NAME}")

with onto:
    # Define the Shape class as a subclass of Anatomy
    class Shape(Thing):
        pass

    # Define DatatypeProperties for Shape

    class description(DataProperty, FunctionalProperty):
        domain = [Shape]
        range = [str]

    class property(DataProperty, FunctionalProperty):
        domain = [Shape]
        range = [str]
    
    class application(DataProperty, FunctionalProperty):
        domain = [Shape]
        range = [str]

    class formula(DataProperty, FunctionalProperty):
        domain = [Shape]
        range = [str]


    # JSON data for systems
    systems_data = [
    {
        "name": "Triangle",
        "description": "A triangle is a three-sided polygon that is one of the most fundamental shapes in geometry. It is defined by three vertices connected by three straight sides. Triangles are categorized based on their sides (equilateral, isosceles, scalene) or angles (acute, obtuse, right). They divide a plane into two regions: interior and exterior. Triangles are studied for their properties and play a significant role in engineering, design, and mathematics. They are also used to derive trigonometric principles.",
        "property": "The sum of a triangle's interior angles is always 180 degrees. The triangle inequality theorem states that the sum of any two sides must be greater than the third side. Triangles can be inscribed in a circle (circumcircle) or have a circle inscribed inside them (incircle). Key centers like the centroid, orthocenter, circumcenter, and incenter play vital roles in geometric calculations.",
        "application": "Triangles are essential in engineering for creating stable structures like trusses and bridges. They are widely used in architecture for their strength and stability. In computer graphics, they form the basic units of 3D modeling. In mathematics, they are foundational for trigonometry and geometry. Triangles are used in navigation and astronomy to calculate distances using triangulation. Their simplicity and versatility make them indispensable in both theoretical and practical applications.",
        "formula": "Area = 1/2 × base × height"
    },
    {
        "name": "Circle",
        "description": "A circle is a two-dimensional shape defined as the set of all points equidistant from a fixed center. It is one of the most symmetrical shapes in geometry, having no edges or corners. Circles are widely studied for their mathematical and geometric properties and are used extensively in science, engineering, and art. They symbolize balance and completeness, appearing frequently in natural and human-made structures.",
        "property": "A circle’s radius is the constant distance from its center to any point on its boundary, while its diameter is twice the radius. The circumference is the perimeter of the circle, calculated as 2πr, and its area is πr². Circles have infinite lines of symmetry and can be divided into arcs, sectors, and segments. Tangent lines touch the circle at one point, while secants intersect it at two points.",
        "application": "Circles are vital in mechanical engineering for designing wheels, gears, and rotating components. In architecture, they are used in domes and arches for their aesthetic and structural properties. In physics, they describe rotational motion and angular velocity. Circles also model celestial orbits in astronomy. Artists use circles to create balance and harmony in designs. Everyday objects like coins, clocks, and plates are circular, emphasizing their functional importance.",
        "formula": "Circumference = 2πr; Area = πr²"
    },
    {
        "name": "Sphere",
        "description": "A sphere is a three-dimensional object where all points on the surface are equidistant from the center. It is one of the most symmetrical and geometrically perfect shapes. Spheres are commonly used in physics, astronomy, and engineering due to their unique properties. They appear identical from any perspective, making them ideal for modeling natural objects like planets and stars.",
        "property": "The radius of a sphere is the distance from its center to any point on its surface. The diameter is twice the radius. The surface area of a sphere is calculated as 4πr², and its volume is (4/3)πr³. Spheres have no edges or vertices and are perfectly symmetrical, appearing identical from any direction. Their constant curvature minimizes surface area for a given volume, making them highly efficient geometrically.",
        "application": "Spheres are used in astronomy to model celestial bodies like planets and stars. In physics, they help study wave propagation, gravitational fields, and fluid dynamics. Sports equipment like soccer balls and basketballs utilize spheres for uniform performance. In industry, spheres are used in ball bearings and pressure vessels. Their symmetry and efficiency make them suitable for both practical and aesthetic purposes in design, art, and manufacturing.",
        "formula": "Surface Area = 4πr²; Volume = (4/3)πr³"
    },
    {
        "name": "Square",
        "description": "A square is a quadrilateral with four equal sides and four right angles. It is a specific type of rectangle and rhombus, combining the properties of both. Squares are highly symmetric and are fundamental in geometry, design, and construction. Their simplicity and regularity make them one of the most studied shapes.",
        "property": "A square has equal sides, and its four angles are all 90 degrees. The diagonals of a square are equal in length, bisect each other at right angles, and divide the square into two congruent triangles. A square has four lines of symmetry and rotational symmetry of 90 degrees. The area is calculated as side², and the perimeter is 4 × side.",
        "application": "Squares are widely used in architecture for tiles, windows, and paving patterns. They provide structural stability in design. In mathematics, squares are used for studying symmetry and as the basis for concepts like area and squaring numbers. Squares are also prominent in art and design for creating balanced and structured compositions. Everyday objects like books and frames commonly feature square shapes.",
        "formula": "Area = side²; Perimeter = 4 × side"
    },
    {
        "name": "Hexagon",
        "description": "A hexagon is a six-sided polygon commonly seen in both natural and man-made structures. Regular hexagons have six equal sides and six equal angles, making them highly symmetric. Hexagons are efficient shapes for packing and tiling, appearing in honeycombs and engineering designs.",
        "property": "A regular hexagon has six equal sides, with each interior angle measuring 120 degrees. It can be divided into six equilateral triangles for easy calculation of area. The area of a regular hexagon is (3√3/2) × side², and its perimeter is 6 × side. Hexagons exhibit rotational symmetry of 60 degrees and six lines of reflectional symmetry. Their tiling efficiency is unmatched by other polygons.",
        "application": "Hexagons are prominent in engineering for tiling, nuts, and bolts due to their strength and efficiency. In nature, bees use hexagons in honeycombs to optimize space and minimize material usage. Architects and designers use hexagonal patterns in flooring and wall designs for aesthetic appeal. In mathematics, hexagons are studied for their tessellation properties and symmetry, making them widely applicable in both practical and theoretical contexts.",
        "formula": "Area = (3√3/2) × side²; Perimeter = 6 × side"
    },
    {
        "name": "Octagon",
        "description": "An octagon is an eight-sided polygon that is frequently used in both geometry and design. Regular octagons have eight equal sides and eight equal angles. They are often associated with stop signs and floor tiling patterns, symbolizing symmetry and balance.",
        "property": "A regular octagon has eight equal sides and eight equal angles, with each interior angle measuring 135 degrees. It can be divided into eight isosceles triangles for easy geometric calculations. The area of a regular octagon is 2(1 + √2) × side², and its perimeter is 8 × side. Octagons exhibit rotational symmetry of 45 degrees and have eight lines of reflectional symmetry.",
        "application": "Octagons are used in traffic signs, particularly stop signs, for their distinct shape and visibility. Architects incorporate octagonal patterns in floor tiling and decorative designs. In mathematics, octagons are studied for their symmetry and tessellation properties. Their aesthetic appeal and functional use make them popular in various fields, from engineering to art.",
        "formula": "Area = 2(1 + √2) × side²; Perimeter = 8 × side"
    },
       {
        "name": "Pentagon",
        "description": "A pentagon is a five-sided polygon that appears in both nature and architecture. Regular pentagons have equal sides and angles, with each interior angle measuring 108 degrees. They are known for their aesthetic appeal and structural strength. Pentagons have rotational symmetry of 72 degrees and five lines of reflectional symmetry.",
        "property": "A regular pentagon has five equal sides and five equal interior angles. It can be divided into five isosceles triangles, making area calculations straightforward. The sum of its interior angles is 540 degrees. The area is calculated using the formula (1/4)√(5(5 + 2√5)) × side², and its perimeter is 5 × side. Pentagons exhibit rotational and reflectional symmetry, making them highly versatile in design and geometry.",
        "application": "Pentagons are widely used in architecture, with famous examples like the Pentagon building in the United States. They also appear in nature, such as in the shape of starfish and flowers. In design, pentagons are used for logos, tessellations, and patterns. Their unique shape and symmetry make them visually appealing and structurally useful. In mathematics, pentagons are studied for their properties and applications in geometry.",
        "formula": "Area = (1/4)√(5(5 + 2√5)) × side²; Perimeter = 5 × side"
    },
    {
        "name": "Quadrilateral",
        "description": "A quadrilateral is a four-sided polygon with four vertices and four angles. It includes various types like squares, rectangles, rhombuses, and trapezoids. Quadrilaterals are highly versatile in geometry and are used in numerous applications in construction, design, and mathematics.",
        "property": "The interior angles of any quadrilateral sum up to 360 degrees. Quadrilaterals are categorized based on their sides and angles, such as parallelograms (opposite sides parallel), trapezoids (one pair of parallel sides), and rectangles (four right angles). The diagonals of quadrilaterals intersect at various angles depending on the type. They can have parallel or non-parallel sides, making them adaptable to many designs.",
        "application": "Quadrilaterals are essential in construction for creating walls, tiles, and windows. They are used in architectural designs to achieve both stability and aesthetic appeal. Quadrilaterals are also fundamental in tessellation and tiling patterns. In mathematics, they are studied for their symmetry, area, and perimeter calculations. Their adaptability makes them widely used in both practical and theoretical contexts.",
        "formula": "Area varies based on the type (e.g., base × height for parallelograms)."
    }
]




    # Create instances for systems
    systems_instances = {}
    for system in systems_data:
        system_instance = Shape(system["name"])
        system_instance.description = system["description"]
        system_instance.property = system["property"]
        system_instance.application = system["application"]
        system_instance.formula = system["formula"]


    # Save the ontology to a file
    onto.save(file=FILE_NAME, format="rdfxml")

# Print out organ and system details
print("Organs:")
for row in onto.Shape.instances():
    print(f"  {row.name}: Property = {row.property}, Description = {row.description}, Application = {row.application}, Formula = {row.formula}")



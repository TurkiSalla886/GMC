import xml.etree.ElementTree as ET
from xml.dom import minidom

# Sample reviews data
reviews = [
    {
        "id": 1,
        "reviewer_name": "John Doe",
        "rating": 5,
        "text": "Great product!",
        "timestamp": "2025-01-01T12:00:00Z",
        "product_id": 101
    },
    {
        "id": 2,
        "reviewer_name": "Jane Smith",
        "rating": 4,
        "text": "Good value for money.",
        "timestamp": "2025-01-02T15:30:00Z",
        "product_id": 102
    }
]

# Function to create XML from reviews
def create_xml(reviews):
    # Create the root element
    root = ET.Element("reviews")

    # Add each review as a child of the root
    for review in reviews:
        # Create a <review> element
        review_elem = ET.SubElement(root, "review")
        
        # Add sub-elements for each field
        ET.SubElement(review_elem, "review_id").text = str(review['id'])
        ET.SubElement(review_elem, "reviewer_name").text = review['reviewer_name']
        ET.SubElement(review_elem, "rating").text = str(review['rating'])
        ET.SubElement(review_elem, "review_text").text = review['text']
        ET.SubElement(review_elem, "review_timestamp").text = review['timestamp']
        ET.SubElement(review_elem, "product_id").text = str(review['product_id'])

    # Convert the ElementTree to a string
    rough_string = ET.tostring(root, encoding="utf-8")
    
    # Pretty-print the XML
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    
    return pretty_xml

# Generate the XML
xml_data = create_xml(reviews)

# Save the XML to a file
with open("product_reviews.xml", "w", encoding="utf-8") as f:
    f.write(xml_data)

# Output the XML
print(xml_data)

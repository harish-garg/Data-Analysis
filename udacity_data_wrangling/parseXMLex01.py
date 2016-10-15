import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()

print "\nChildren of root:"
for Child in root:
    print Child.tag

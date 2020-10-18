import sys
import xml.etree.ElementTree as xml

"""
add version to pom if it has not one
"""

namespaces = '{http://maven.apache.org/POM/4.0.0}'

pom_filename = sys.argv[1]  # /path/to/pom.xml

pom = xml.parse(pom_filename)
root = pom.getroot()

xml.register_namespace('', "http://maven.apache.org/POM/4.0.0")

try:
    if len(root.items()[0][1]) > 1:
        if len(root.findall(namespaces+'version')) == 0:
            print('NO VERSION')
            version = xml.Element(namespaces+'version')
            version.text = '1.0'
            root.insert(1, version)
            el = xml.ElementTree(root)
            el.write(pom_filename, encoding='utf-8', xml_declaration=True)
        else:
            print('Has version')
except IndexError:
    print(root.findall('version'))
    if len(root.findall('version')) == 0:
        print('NO VERSION')
        version = xml.Element('version')
        version.text = '1.0'
        root.insert(1, version)
        el = xml.ElementTree(root)
        el.write(pom_filename, encoding='utf-8', xml_declaration=True)
    else:
        print('Has version')

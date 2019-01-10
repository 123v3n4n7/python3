# -*- coding: utf-8 -*-
from xml.dom import minidom

import xml.etree.cElementTree
import xml.etree.cElementTree as ET
import time
#
# doc = minidom.Document()
#
# root = doc.createElement('root')
# doc.appendChild(root)
#
# name = doc.createElement('name')
# text = doc.createTextNode("Product for you")
# name.appendChild(text)
# root.appendChild(name)
#
# product = doc.createElement('product')
# product.setAttribute('color', 'white')
#
# decr = doc.createElement('decr')
# text = doc.createTextNode('text decr 1')
# decr.appendChild(text)
# decr.setAttribute('color', 'green')
# product.appendChild(decr)
#
# article = doc.createElement('article')
# text = doc.createTextNode('Text article 1')
# article.appendChild(text)
# article.setAttribute('color', 'white')
# product.appendChild(article)
#
# price = doc.createElement('article')
# text = doc.createTextNode('Text article 1')
# price.appendChild(text)
# price.setAttribute('color', 'white')
# product.appendChild(price)
#
# root.appendChild(product)
#
# product = doc.createElement('product')
# product.setAttribute('color', 'white')
#
# decr = doc.createElement('decr')
# text = doc.createTextNode('text decr 1')
# decr.appendChild(text)
# decr.setAttribute('color', 'green')
# product.appendChild(decr)
#
# article = doc.createElement('article')
# text = doc.createTextNode('Text article 1')
# article.appendChild(text)
# article.setAttribute('color', 'white')
# product.appendChild(article)
#
# price = doc.createElement('article')
# text = doc.createTextNode('Text article 1')
# price.appendChild(text)
# price.setAttribute('color', 'white')
# product.appendChild(price)
#
# root.appendChild(product)
#
# xml_str = doc.toprettyxml(indent=" ")
# with open ("product.xml", "w") as f:
#     f.write(xml_str)
############################################################
# doc = minidom.parse("product.xml")
# name = doc.getElementsByTagName("name")[0]
# print(name.firstChild.data)
#
# products = doc.getElementsByTagName("product")
# for product in products:
#     decr = doc.getElementsByTagName("decr")[0]
#     article = doc.getElementsByTagName("article")[0]
#     print("decr: {}, article: {}".format(decr.firstChild.data, article.firstChild.data))
############################################################

# root = xml.Element('zAppointment')
# appt = xml.Element('appointment')
# root.append(appt)
#
# begin = xml.SubElement(appt, 'begin')
# begin.text = '123123123123123'
#
# uid = xml.SubElement(appt, 'uid')
# uid.text = '312321312312312'
#
# alarmTime = xml.SubElement(appt, 'alarmTime', color='red')
# alarmTime.text = '1432414124124'
#
# state = xml.SubElement(appt, 'state')
#
# tree = xml.ElementTree(root)
#
# with open('elementtree12313123213.xml', 'wb') as fh:
#     tree.write(fh)
############################################################

tree = ET.ElementTree(file="elementtree12313123213.xml")
root = tree.getroot()

for begin in root.iter('begin'):
    begin.text = time.ctime()

tree = ET.ElementTree(root)
with open("elementtree12313123213.xml", 'wb') as fh:
    tree.write(fh)
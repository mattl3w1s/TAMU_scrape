import sys
import csv
from lxml import etree

ROOT_URL = sys.argv[-1]

parser = etree.HTMLParser()

tree = etree.parse(sys.stdin,parser)
result = etree.tostring(tree.getroot(),pretty_print=True,method="html")

root = tree.getroot()
department_list = root.xpath('//ul[@class="nav leveltwo"]')[0]

for a in department_list.xpath('.//li/a'):
    SCHOOL_LINK = ROOT_URL+a.xpath('./@href')[0].replace('/undergraduate',"")
    SCHOOL_NAME = a.xpath('./text()')[0]
    sys.stdout.write(f'{SCHOOL_LINK},"{SCHOOL_NAME}"\n')
    




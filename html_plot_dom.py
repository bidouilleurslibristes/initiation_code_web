import urllib
from hashlib import md5
import bs4 as BeautifulSoup

import networkx as nx
from networkx.drawing.nx_agraph import write_dot

md5s_to_name = {}  # stoque les noms déjà attribués
counts = {}  # stoque le nombre d'éléements de chaque type déjà vu
md5s = {}


def find_element_from_id(id_):
    elem = [(k, v) for k, v in md5s_to_name.items() if v == id_]
    print(elem)
    md5 = elem[0][0]
    print(md5s[md5])
    return md5s[md5]


def anotate_dom(root):
    annotations = []
    for e in root.find_all():
        if not e.text:
            continue

        parent_md5 = md5(e.parent.text.encode("utf8")).hexdigest()
        parent_name = e.parent.name

        element_md5 = md5(e.text.encode("utf8")).hexdigest()
        element_name = e.name

        md5s[parent_md5] = e.parent
        md5s[element_md5] = e

        if element_md5 not in md5s_to_name:
            if element_name in counts:
                name = "{}_{}".format(element_name, counts[element_name])
                counts[element_name] += 1
            else:
                name = element_name
                counts[element_name] = 1
            md5s_to_name[element_md5] = name

        if parent_md5 not in md5s_to_name:
            if parent_name in counts:
                name = "{}_{}".format(parent_name, counts[parent_name])
                counts[parent_name] += 1
            else:
                name = parent_name
                counts[parent_name] = 1
            md5s_to_name[parent_md5] = name


        if md5s_to_name[parent_md5] == md5s_to_name[element_md5]:
            continue

        if md5s_to_name[parent_md5] == "meta" or md5s_to_name[element_md5] == "meta" :
            continue

        if md5s_to_name[parent_md5] == "link" or md5s_to_name[element_md5] == "link" :
            continue

        if md5s_to_name[parent_md5] == "script" or md5s_to_name[element_md5] == "script" :
            continue

        if md5s_to_name[parent_md5] == "a" or md5s_to_name[element_md5] == "a" :
            continue

        edge = [md5s_to_name[parent_md5], md5s_to_name[element_md5]]
        annotations.append(edge)
    return annotations


html = urllib.request.urlopen('http://www.sciencespo-lille.eu/').read()
soup = BeautifulSoup.BeautifulSoup(html, "lxml")

G = nx.DiGraph()
relations = anotate_dom(soup.html)

for parent_name, child_name in relations:
    G.add_edge(parent_name, child_name)

write_dot(G, "/tmp/test.dot")

import IPython; IPython.embed()

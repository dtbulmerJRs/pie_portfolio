#!/usr/bin/python

from jinja2 import Environment, PackageLoader
import models
import os
env = Environment(loader=PackageLoader('models', 'templates'))

OUTPUT_DIR = './_output/'
template = env.get_template('blog-entry.html')

articles = []
for n in models.posts:
    condition = False

    articles.append({
        'title'   : n["data"].title,
        'url'     : n["data"].url,
        'current' : condition
    })
    
for post in models.posts:
    g = post["data"].spit_dict()
    a = list(articles)
    
    for x in a:
        i = a.index(x)
    
        if x["url"] == g["url"]:
            a[i]["current"] = True

        else:
            a[i]["current"] = False
    
    g["posts"] = a
                
    with open(os.path.join(OUTPUT_DIR, g["url"]), 'w') as html:
        html.write(template.render(g))
        
    if models.posts[0] == post:
        with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as html:
		        html.write(template.render(g))
\

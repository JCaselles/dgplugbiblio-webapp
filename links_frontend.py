#!/usr/bin/env python

import flask
from json import load


APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """
    If 'query' in query string, show only those links containing
    'query' value in them. Otherwise, show all links.

    """

    with open('links.json') as json_file:
        links_list = load(json_file)
        filtered_list = []
        if flask.request.args.get('query'):
            for link in links_list:
                if flask.request.args.get('query') in link:
                    filtered_list.append(link)

            return flask.render_template('index.html', links_list=filtered_list)

        else:
            return flask.render_template('index.html', links_list=links_list)



if __name__ == '__main__':
    APP.debug=True
    APP.run()

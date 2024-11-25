from flask import Blueprint

template_views = Blueprint('template_views' , __name__ , url_prefix='/')

@template_views.route('/')
def home():
    return "<h1>Template View</h1>"
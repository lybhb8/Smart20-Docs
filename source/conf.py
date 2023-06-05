# 头部添加导入
# import sphinx_book_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Smart20 BlowmoldingControlSystem'
copyright = '2023, Bobolin'
author = 'Bobolin'
release = '2.00'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys, os

sys.path.append(os.path.abspath('sphinxext'))

extensions = ['extname']

extensions = ['myst_parser']
# extensions = ['recommonmark']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

source_suffix = {
    
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}


source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'press'
html_theme = 'sphinx_rtd_theme'


html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }


# 添加你自己的 CSS 规则
html_static_path = ['_static']
html_css_files = ["custom.css"]
# 自定义徽标、和网站图标
html_logo = "_static/notebook-logo.svg"
html_favicon = "_static/favicon.ico"


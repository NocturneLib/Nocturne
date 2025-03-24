# Configuration file for the Sphinx documentation builder.

import os

# -- Project information -----------------------------------------------------
project = 'Nocturne'
copyright = '2025, 750W'
author = 'Samuel Asefa'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # This changes the header background to black
    'style_nav_header_background': '#000000',
}
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# -- Custom CSS Setup -----------
css_content = """
/* Custom Black and Gold Theme */

/* Base Body Styling */
body {
    background-color: #000000;
    color: #D4AF37;
}

/* Links */
a {
    color: #D4AF37;
}
a:hover, a:focus {
    color: #ffffff;
}

/* Navbar/Header */
.rtd-navbar, .wy-nav-side, .wy-menu-vertical {
    background-color: #000000;
}

/* Sidebar links */
.wy-menu-vertical a, .wy-menu-vertical a:visited {
    color: #D4AF37;
}
.wy-menu-vertical a.current {
    border-left: 3px solid #D4AF37;
}

/* Code blocks */
.highlight pre {
    background: #1a1a1a;
    color: #D4AF37;
}

/* Tables */
table.docutils {
    border: 1px solid #D4AF37;
}
table.docutils th, table.docutils td {
    border: 1px solid #D4AF37;
}

/* Section breaks */
.section {
    border-bottom: 1px solid #D4AF37;
}
"""

# Ensure _static directory exists and write the custom.css file if it does not
static_dir = os.path.join(os.path.dirname(__file__), '_static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

custom_css_file = os.path.join(static_dir, 'custom.css')
if not os.path.exists(custom_css_file):
    with open(custom_css_file, 'w') as f:
        f.write(css_content)

# -- Setup function to add custom CSS ----------------------------------------
def setup(app):
    app.add_css_file("custom.css")

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'

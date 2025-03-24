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
    # Override the navigation header background to match our dark theme
    'style_nav_header_background': '#1C1C1C',
}
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# -- Custom CSS Setup -----------
css_content = """
/* Custom Nocturne Theme for ReadTheDocs */

/* Overall background for all pages */
body {
    background-color: #1C1C1C;
    color: #D4AF37;
}

/* Remove any default white backgrounds from main containers */
.document, .rst-content, .wy-nav-content {
    background-color: #1C1C1C;
}

/* Links using gold and removing blue/purple defaults */
a {
    color: #D4AF37;
}
a:hover, a:focus {
    color: #ffffff;
}

/* Navbar/Header Styling */
.rtd-navbar, .wy-nav-side, .wy-menu-vertical {
    background-color: #1C1C1C;
}

/* Sidebar links styling */
.wy-menu-vertical a, .wy-menu-vertical a:visited {
    color: #D4AF37;
}
.wy-menu-vertical a.current {
    border-left: 3px solid #D4AF37;
}

/* Code blocks */
.highlight pre {
    background: #2E2E2E;
    color: #D4AF37;
}

/* Tables */
table.docutils {
    border: 1px solid #D4AF37;
    background-color: #1C1C1C;
}
table.docutils th, table.docutils td {
    border: 1px solid #D4AF37;
}

/* Section breaks and other elements */
.section, .sidebar {
    border-color: #D4AF37;
}

/* Remove any potential purple or blue accents */
a.reference, .headerlink {
    color: #D4AF37;
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
5

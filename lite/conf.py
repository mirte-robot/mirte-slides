# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------
import os
from urllib.parse import urljoin

from sphinx_revealjs.utils import get_revealjs_path

# -- Project information -----------------------------------------------------
project = "sphinx-revealjs"
copyright = "2024, Delft University of Technology"
author = "Martin Klomp"
version = ""
release = ""
footer = "&#169; " + copyright + ", CC BY-SA."

# -- General configuration ---------------------------------------------------
extensions = [
#    "atsphinx.mini18n",
    "oembedpy.ext.sphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.footnotes",
    "sphinx_revealjs.ext.screenshot",
    "sphinxcontrib.budoux",
    "sphinxcontrib.gtagjs",
    "sphinxcontrib.sass",
    "sphinxext.opengraph",
    "sphinxcontrib.youtube",
    "sphinxcontrib.video",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
#language = "en"
#locale_dirs = ["_locales"]
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "_sections"]
pygments_style = None

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for Reveal.js output ---------------------------------------------
revealjs_html_theme = "revealjs-simple"
revealjs_static_path = ["_static"]
revealjs_style_theme = "custom.css"
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "hash": True,
    "center": True,
    "transition": "slide",
    "previewLinks": True,
}
revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs/plugin/math/math.js",
    },
    {
        "name": "RevealCustomControls",
        "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/plugin.js",
    },
#    {
#        "name": "RevealChalkboard",
#        "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/chalkboard/plugin.js",
#    },
]
revealjs_css_files = [
    "revealjs/plugin/highlight/zenburn.css",
    "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/style.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
    "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/chalkboard/style.css"
]
revealjs_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/svg.js/3.1.2/svg.min.js",
    "custom.js"
]

revealjs_notes_from_comments = True

# -- Options for extensions --------------------------------------------------
# - sphinx.ext.todo
todo_include_todos = True
# - sphinxcontrib.gtagjs
if "GTAGJS_IDS" in os.environ:
    gtagjs_ids = os.environ["GTAGJS_IDS"].split(",")
# - sphinxcontrib.budoux
budoux_targets = ["h1", "h2", "h3"]
# - sphinxcontrib.sass
sass_src_dir = "_sass"
sass_out_dir = "_static"
sass_targets = {"custom.scss": "custom.css"}
sass_include_paths = [
    get_revealjs_path() / "css" / "theme",
]
# sphinxext.opengraph
ogp_site_url = os.environ.get("DEMO_URL_BASE", "http://localhost:8000/")
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta name="twitter:site" content="@attakei" />',
]

def _add_custom_controls(app, config):
    config.revealjs_script_conf["customcontrols"] = {
        "controls": [
 #           {   "icon": '<i class="fa fa-pen"></i>',
 #               "title": 'Toggle notes canvas (C)',
 #               "action": 'RevealChalkboard.toggleNotesCanvas();'
 #           },
            {
                "icon": footer,
                "action": f"location.href = 'https://www.mirte.org';",
            }
        ]
    }


def setup(app):
    app.connect("config-inited", _add_custom_controls)

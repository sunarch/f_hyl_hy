# This file is execfile()d with the current directory set to its containing dir.

import html
import os
import re
import sys
import time

sys.path.insert(0, os.path.abspath(".."))

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinxcontrib.hydomain",
]

import warnings; import sphinx.deprecation as SD
for c in (SD.RemovedInSphinx60Warning, SD.RemovedInSphinx70Warning):
    warnings.filterwarnings('ignore', category = c)

from get_version import __version__ as hy_version

# Read the Docs might dirty its checkout, so strip the dirty flag.
hy_version = re.sub(r"[+.]dirty\Z", "", hy_version)

templates_path = ["_templates"]
source_suffix = ".rst"

master_doc = "index"

# General information about the project.
project = "hy"
copyright = "%s the authors" % time.strftime("%Y")

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ".".join(hy_version.split(".")[:-1])
# The full version, including alpha/beta/rc tags.
release = hy_version
hy_descriptive_version = html.escape(hy_version)
if "+" in hy_version:
    hy_descriptive_version += " <strong style='color: red;'>(unstable)</strong>"

exclude_patterns = ["_build", "coreteam.rst"]
add_module_names = True

pygments_style = "sphinx"

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_use_smartypants = False
html_show_sphinx = False

html_context = dict(
    hy_descriptive_version=hy_descriptive_version)

highlight_language = "hylang"

intersphinx_mapping = dict(
    py=("https://docs.python.org/3/", None),
    hyrule=("https://hyrule.readthedocs.io/en/master/", None),
)

import hy
hy.I = type(hy.I)  # A trick to enable `hy:autoclass:: hy.I`


# ** Sphinx App Setup


def setup(app):
    app.add_css_file("overrides.css")

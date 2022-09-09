# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
http://www.sphinx-doc.org/en/master/config
"""
# pylint: disable=invalid-name

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys

from sphinx import application

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

import _custom  # pylint: disable=wrong-import-position; # noqa: E402

# -- Project information -----------------------------------------------------

project = 'Openschema'

# The full version, including alpha/beta/rc tags
release = _custom.VERSION


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinxcontrib.details.directive',
    'sphinxcontrib.spelling',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

intersphinx_mapping = {
    'forml': ('https://docs.forml.io/en/develop/', None),
    'pip': ('https://pip.pypa.io/en/stable/', None),
    'python': ('https://docs.python.org/3', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
}

# Warn about all references where the target cannot be found
nitpicky = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Set link name generated in the top bar.
html_title = 'OpenSchema'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_show_sourcelink = True
html_show_copyright = False
html_show_sphinx = False

# == Extensions configuration ==================================================

# -- Options for sphinx.ext.autodoc --------------------------------------------
# See: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
autodoc_typehints = 'signature'
autodoc_member_order = 'bysource'
autosummary_generate = True
autosummary_ignore_module_all = False
autosummary_imported_members = True

# -- Options for sphinx.ext.napoleon --------------------------------------------
# See: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_numpy_docstring = False


def setup(app: application.Sphinx):
    """Sphinx setup hook."""
    app.add_autodocumenter(_custom.ClassDocumenter, override=True)
    app.add_autodocumenter(_custom.AttributeDocumenter, override=True)
    app.add_directive('autosummary', _custom.Autosummary, override=True)

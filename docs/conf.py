# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import inspect
import os
import re
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))

# Need to build docs with Python 3.8 or higher for proper typing annotations, including from __future__ import annotations
assert sys.version_info.major == 3 and sys.version_info.minor >= 8

# Assign a build variable to the builtin module that inerts the @set_module decorator. This is done because set_module
# confuses Sphinx when parsing overloaded functions. When not building the documentation, the @set_module("sdr")
# decorator works as intended.
import builtins

setattr(builtins, "__sphinx_build__", True)

import numpy
import sphinx

import sdr

# -- Project information -----------------------------------------------------

project = "sdr"
copyright = "2023, Matt Hostetter"
author = "Matt Hostetter"
version = sdr.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx_last_updated_by_git",
    "sphinx_immaterial",
    "sphinx_immaterial.apidoc.python.apigen",
    "sphinx_math_dollar",
    # "myst_parser",
    "myst_nb",
    "sphinx_design",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md", ".ipynb"]

# Tell sphinx that ReadTheDocs will create an index.rst file as the main file,
# not the default of contents.rst.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_immaterial"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "extra.css",
]

# Define a custom inline Python syntax highlighting literal
rst_prolog = """
.. role:: python(code)
   :language: python
   :class: highlight
"""

# Sets the default role of `content` to :python:`content`, which uses the custom Python syntax highlighting inline literal
default_role = "python"

html_title = "sdr"
# html_favicon = "../logo/sdr-favicon-color.png"
# html_logo = "../logo/sdr-favicon-white.png"

# Sphinx Immaterial theme options
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://mhostetter.github.io/sdr/latest/",
    "repo_url": "https://github.com/mhostetter/sdr",
    "repo_name": "mhostetter/sdr",
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/mhostetter/sdr",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/sdr/",
        },
        {
            "icon": "fontawesome/brands/twitter",
            "link": "https://twitter.com/sdr_py",
        },
    ],
    "edit_uri": "",
    "globaltoc_collapse": False,
    "features": [
        # "navigation.expand",
        "navigation.tabs",
        # "toc.integrate",
        # "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        "navigation.tracking",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "analytics": {
        "provider": "google",
        "property": "G-PVMFVF4016",
    },
    "version_dropdown": True,
    "version_json": "../versions.json",
}

html_last_updated_fmt = ""
html_use_index = True
html_domain_indices = True

nitpicky = True
nitpick_ignore = [
    ("py:class", "numpy.typing.ArrayLike"),  # Wish this would work
    ("py:class", "numpy.typing.DTypeLike"),  # Wish this would work
    ("py:class", "numpy.typing.NDArray"),  # Wish this would work
]


# -- Extension configuration -------------------------------------------------

# Create hyperlinks to other documentation
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("http://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("http://matplotlib.sourceforge.net/", None),
}

autodoc_default_options = {
    "imported-members": True,
    "members": True,
    # "special-members": True,
    # "inherited-members": "ndarray",
    # "member-order": "groupwise",
}
autodoc_typehints = "signature"
autodoc_typehints_description_target = "documented"
autodoc_typehints_format = "short"

autodoc_type_aliases = {
    "npt.ArrayLike": "~numpy.typing.ArrayLike",
    "npt.DTypeLike": "~numpy.typing.DTypeLike",
    "npt.NDArray": "~numpy.typing.NDArray",
}

ipython_execlines = [
    "import math",
    "import matplotlib.pyplot as plt",
    "import numpy as np",
    "import sdr",
    "np.random.seed(0)",  # Set random seed for reproducibility
    "sdr.plot.use_style()",  # Use the sdr library matplotlib style
]
ipython_warning_is_error = False

myst_enable_extensions = ["dollarmath"]

nb_execution_mode = "off"
# nb_output_stderr = "remove-warn"

mathjax_config = {
    "tex2jax": {
        "inlineMath": [["\\(", "\\)"]],
        "displayMath": [["\\[", "\\]"]],
    },
}
mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"]],
        "displayMath": [["\\[", "\\]"]],
    }
}

# -- Sphinx Immaterial configs -------------------------------------------------

# Python apigen configuration
python_apigen_modules = {
    "sdr": "api/sdr.",
    "sdr.plot": "api/sdr.plot.",
}
python_apigen_default_groups = [
    ("class:.*", "Classes"),
    ("data:.*", "Variables"),
    ("function:.*", "Functions"),
    ("classmethod:.*", "Class methods"),
    ("method:.*", "Methods"),
    (r"method:.*\.[A-Z][A-Za-z,_]*", "Constructors"),
    (r"method:.*\.__[A-Za-z,_]*__", "Special methods"),
    (r"method:.*\.__(init|new)__", "Constructors"),
    (r"method:.*\.__(str|repr)__", "String representation"),
    (r"method:.*\.(plot).*", "Plotting"),
    ("property:.*", "Properties"),
    (r".*:.*\.is_[a-z,_]*", "Attributes"),
]
python_apigen_default_order = [
    ("class:.*", 10),
    ("data:.*", 11),
    ("function:.*", 12),
    ("classmethod:.*", 40),
    ("method:.*", 50),
    (r"method:.*\.[A-Z][A-Za-z,_]*", 20),
    (r"method:.*\.__[A-Za-z,_]*__", 28),
    (r"method:.*\.__(init|new)__", 20),
    (r"method:.*\.__(str|repr)__", 30),
    (r"method:.*\.(plot).*", 51),
    ("property:.*", 60),
    (r".*:.*\.is_[a-z,_]*", 70),
]
# python_apigen_order_tiebreaker = "alphabetical"
python_apigen_case_insensitive_filesystem = False
python_apigen_show_base_classes = True

# Python domain directive configuration
python_type_aliases = autodoc_type_aliases
python_module_names_to_strip_from_xrefs = ["collections.abc"]

# General API configuration
object_description_options = [
    ("py:.*", dict(include_rubrics_in_toc=True)),
]

sphinx_immaterial_custom_admonitions = [
    {
        "name": "seealso",
        "title": "See also",
        "classes": ["collapsible"],
        "icon": "fontawesome/regular/eye",
        "override": True,
    },
    {
        "name": "star",
        "icon": "octicons/star-16",
        "color": (255, 233, 3),  # Gold
    },
    # {
    #     "name": "fast-performance",
    #     "title": "Faster performance",
    #     "icon": "material/speedometer",
    #     "color": (47, 177, 112),  # Green: --md-code-hl-string-color
    # },
    # {
    #     "name": "slow-performance",
    #     "title": "Slower performance",
    #     "icon": "material/speedometer-slow",
    #     "color": (230, 105, 91),  # Red: --md-code-hl-number-color
    # },
]


# -- Monkey-patching ---------------------------------------------------------

# SPECIAL_MEMBERS = [
#     "__repr__",
#     "__str__",
#     "__int__",
#     "__call__",
#     "__len__",
#     "__eq__",
# ]


def autodoc_skip_member(app, what, name, obj, skip, options):
    """
    Instruct autodoc to skip members that are inherited from np.ndarray.
    """
    if name in ["__str__", "__repr__"]:
        return True

    return skip


def autodoc_process_bases(app, name, obj, options, bases):
    """
    Remove private classes or mixin classes from documented class bases.
    """
    # Determine the bases to be removed
    remove_bases = []
    for base in bases:
        if base.__name__[0] == "_" or "Mixin" in base.__name__:
            remove_bases.append(base)

    # Remove from the bases list in-place
    for base in remove_bases:
        bases.remove(base)


# # Only during Sphinx builds, monkey-patch the metaclass properties into this class as "class properties". In Python 3.9 and greater,
# # class properties may be created using `@classmethod @property def foo(cls): return "bar"`. In earlier versions, they must be created
# # in the metaclass, however Sphinx cannot find or document them. Adding this workaround allows Sphinx to document them.


# def classproperty(obj):
#     ret = classmethod(obj)
#     ret.__doc__ = obj.__doc__
#     return ret


# ArrayMeta_properties = [
#     member for member in dir(sdr.Array) if inspect.isdatadescriptor(getattr(type(sdr.Array), member, None))
# ]
# for p in ArrayMeta_properties:
#     # Fetch the class properties from the private metaclasses
#     ArrayMeta_property = getattr(sdr._domains._meta.ArrayMeta, p)

#     # Temporarily delete the class properties from the private metaclasses
#     delattr(sdr._domains._meta.ArrayMeta, p)

#     # Add a Python 3.9 style class property to the public class
#     setattr(sdr.Array, p, classproperty(ArrayMeta_property))

#     # Add back the class properties to the private metaclasses
#     setattr(sdr._domains._meta.ArrayMeta, p, ArrayMeta_property)


# FieldArrayMeta_properties = [
#     member for member in dir(sdr.FieldArray) if inspect.isdatadescriptor(getattr(type(sdr.FieldArray), member, None))
# ]
# for p in FieldArrayMeta_properties:
#     # Fetch the class properties from the private metaclasses
#     if p in ArrayMeta_properties:
#         ArrayMeta_property = getattr(sdr._domains._meta.ArrayMeta, p)
#     FieldArrayMeta_property = getattr(sdr._fields._meta.FieldArrayMeta, p)

#     # Temporarily delete the class properties from the private metaclasses
#     if p in ArrayMeta_properties:
#         delattr(sdr._domains._meta.ArrayMeta, p)
#     delattr(sdr._fields._meta.FieldArrayMeta, p)

#     # Add a Python 3.9 style class property to the public class
#     setattr(sdr.FieldArray, p, classproperty(FieldArrayMeta_property))

#     # Add back the class properties to the private metaclasses
#     if p in ArrayMeta_properties:
#         setattr(sdr._domains._meta.ArrayMeta, p, ArrayMeta_property)
#     setattr(sdr._fields._meta.FieldArrayMeta, p, FieldArrayMeta_property)


def autodoc_process_signature(app, what, name, obj, options, signature, return_annotation):
    signature = modify_type_hints(signature)
    return_annotation = modify_type_hints(return_annotation)
    return signature, return_annotation


def modify_type_hints(signature):
    """
    Fix shortening numpy type annotations in string annotations created with
    `from __future__ import annotations` that Sphinx can't process before Python
    3.10.

    See https://github.com/jbms/sphinx-immaterial/issues/161
    """
    if signature:
        signature = re.sub(r"(?<!~)np\.", "~numpy.", signature)
    return signature


def monkey_patch_parse_see_also():
    """
    Use the NumPy docstring parsing of See Also sections for convenience. This automatically
    hyperlinks plaintext functions and methods.
    """
    # Add the special parsing method from NumpyDocstring
    method = sphinx.ext.napoleon.NumpyDocstring._parse_numpydoc_see_also_section
    sphinx.ext.napoleon.GoogleDocstring._parse_numpydoc_see_also_section = method

    def _parse_see_also_section(self, section: str):
        """Copied from NumpyDocstring._parse_see_also_section()."""
        lines = self._consume_to_next_section()

        # Added: strip whitespace from lines to satisfy _parse_numpydoc_see_also_section()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

        try:
            return self._parse_numpydoc_see_also_section(lines)
        except ValueError:
            return self._format_admonition("seealso", lines)

    sphinx.ext.napoleon.GoogleDocstring._parse_see_also_section = _parse_see_also_section


def setup(app):
    monkey_patch_parse_see_also()

    app.connect("autodoc-skip-member", autodoc_skip_member)
    app.connect("autodoc-process-bases", autodoc_process_bases)
    app.connect("autodoc-process-signature", autodoc_process_signature)

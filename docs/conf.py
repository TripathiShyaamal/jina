import re
import sys
from os import path

sys.path.insert(0, path.abspath('..'))

project = 'Jina Documentation'
slug = re.sub(r'\W+', '-', project.lower())
author = 'Jina AI and its lovely contributors'
copyright = author
source_suffix = ['.rst', '.md']
master_doc = 'index'
language = 'en'

try:
    pkg_name = 'jina'
    libinfo_py = path.join('..', pkg_name, '__init__.py')
    libinfo_content = open(libinfo_py, 'r').readlines()
    version_line = [l.strip() for l in libinfo_content if l.startswith('__version__')][0]
    exec(version_line)
except FileNotFoundError:
    __version__ = '0.0.0'

version = __version__
release = __version__

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tests']
pygments_style = 'colorful'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'logo_only': False,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    # 'vcs_pageview_mode': '',
    # # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
}

html_static_path = ['_static']
html_logo = '../.github/jina-logo-square-blue-on-white-tight.svg'
html_css_files = ['main.css']
htmlhelp_basename = slug
html_show_sourcelink = True

latex_documents = [(master_doc, '{0}.tex'.format(slug), project, author, 'manual')]
man_pages = [(master_doc, slug, project, [author], 1)]
texinfo_documents = [(master_doc, slug, project, author, slug, project, 'Miscellaneous')]
epub_title = project
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode',
    'sphinxcontrib.apidoc',
    'sphinxarg.ext',
    'sphinx_rtd_theme',
    'recommonmark',
    'sphinxcontrib.autoyaml',
    'sphinx_markdown_tables',
    'sphinx_copybutton'
]

apidoc_module_dir = '../jina/'
apidoc_output_dir = 'api'
apidoc_excluded_paths = ['tests', 'legacy']
apidoc_separate_modules = True
apidoc_extra_args = ['-t', 'template/']
autodoc_member_order = 'bysource'
autodoc_mock_imports = ['argparse', 'numpy', 'np']
autoclass_content = 'both'
set_type_checking_flag = False
autoyaml_root = './chapters/yaml/'


def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field
    from sphinx.locale import _

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )

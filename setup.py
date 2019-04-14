# coding=utf-8
"""
  i2C_LCD2004 Plugin for Octoprint installation script.
"""
from setuptools import setup

#####################################################################################
### Do not forget to adjust the following variables to your own plugin.

# The plugin's identifier, has to be unique
plugin_identifier = "OctoPrint_i2C_LCD2004"

# The plugin's python package, should be "octoprint_<plugin identifier>", has to be unique
plugin_package = "OctoPrint_i2C_LCD2004"

# The plugin's human readable name. Can be overwritten within OctoPrint's internal
# data via __plugin_name__ in the plugin module
plugin_name = "OctoPrint-i2C_LCD2004"

# The plugin's version. Can be overwritten within OctoPrint's internal
# data via __plugin_version__ in the plugin module
plugin_version = "0.1.0"

# The plugin's description. Can be overwritten within OctoPrint's internal data via
# __plugin_description__ in the plugin module
plugin_description = """Octoprint plugin to display informations on an i2C connected LCD2004."""

# The plugin's author. Can be overwritten within OctoPrint's internal data via
# __plugin_author__ in the plugin module
plugin_author = "nionio6915"

# The plugin's author's mail address.
plugin_author_email = " 17693150+nionio6915@users.noreply.github.com"

# The plugin's homepage URL. Can be overwritten within OctoPrint's internal data
# via __plugin_url__ in the plugin module
plugin_url = "https://github.com/nionio6915/OctoPrint-i2C_LCD2004"

# The plugin's license. Can be overwritten within OctoPrint's internal data
# via __plugin_license__ in the plugin module
plugin_license = "AGPLv3"

# Any additional requirements besides OctoPrint should be listed here
plugin_requires = ["RPLCD", "smbus2", "fake-rpi"]

### ------------------------------------------------------------------------------------------------
### More advanced options that you usually shouldn't have to touch follow after this point
### ------------------------------------------------------------------------------------------------

# Additional package data to install for this plugin. The subfolders "templates", "static" and
# "translations" will already be installed automatically if they exist. Note that if you add
# something here you'll also need to update MANIFEST.in to match to ensure that python setup.py
# sdist produces a source distribution that contains all your files. This is sadly due to how
# python's setup.py works, see also http://stackoverflow.com/a/14159430/2028598
plugin_additional_data = []

# Any additional python packages you need to install with your plugin that are not
# contained in <plugin_package>.*
plugin_additional_packages = []

# Any python packages within <plugin_package>.* you do NOT want to install with your plugin
plugin_ignored_packages = []

# Additional parameters for the call to setuptools.setup. If your plugin wants to register
# additional entry points, define dependency links or other things like that, this is the place to
# go. Will be merged recursively with the default setup parameters as provided by
# octoprint_setuptools.create_plugin_setup_parameters using octoprint.util.dict_merge.
#
# Example:
#     plugin_requires = ["someDependency==dev"]
#     additional_setup_parameters = {"dependency_links":
#       ["https://github.com/someUser/someRepo/archive/master.zip#egg=someDependency-dev"]}
additional_setup_parameters = {}

#####################################################################################

try:
    import octoprint_setuptools
except ImportError:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
          "the same python installation that OctoPrint is installed under?")
    import sys
    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    requires=plugin_requires,
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data
)

if additional_setup_parameters:
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)

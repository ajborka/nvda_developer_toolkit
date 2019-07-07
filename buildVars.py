# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "developerToolkit",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Developer's toolkit"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""An NVDA addon that assists blind and visually impaired developers with creating visually appealing user interfaces."""),
	# version
	"addon_version" : "2019.0",
	# Author(s)
	"addon_author" : u"Andy Borka <ajborka@gmail.com>",
	# URL for the add-on documentation support
	"addon_url" : u"https://github.com/ajborka/nvda_developer_toolkit",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0")
	"addon_minimumNVDAVersion" : "2019.1.1",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.2.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["globalPlugins/developerToolkit/__init__.py", "globalPlugins/developerToolkit/dialogs.py", "globalPlugins/developerToolkit/shared.py",]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
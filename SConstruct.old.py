# NVDA add-on template  SCONSTRUCT file
#Copyright (C) 2012, 2014 Rui Batista <ruiandrebatista@gmail.com>
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import codecs
import gettext
import os
import os.path
import zipfile

import buildVars

def md2html(source, dest):
	import markdown
	lang = os.path.basename(os.path.dirname(source)).replace('_', '-')
	title="{addonSummary} {addonVersion}".format(addonSummary=buildVars.addon_info["addon_summary"], addonVersion=buildVars.addon_info["addon_version"])
	headerDic = {
		"[[!meta title=\"": "# ",
		"\"]]": " #",
	}
	with codecs.open(source, "r", "utf-8") as f:
		mdText = f.read()
		for k, v in headerDic.iteritems():
			mdText = mdText.replace(k, v, 1)
		htmlText = markdown.markdown(mdText)
	with codecs.open(dest, "w", "utf-8") as f:
		f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
			"<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\n" +
			"    \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n" +
			"<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"%s\" lang=\"%s\">\n" % (lang, lang) +
			"<head>\n" +
			"<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>\n" +
			"<link rel=\"stylesheet\" type=\"text/css\" href=\"../style.css\" media=\"screen\"/>\n" +
			"<title>%s</title>\n" % title +
			"</head>\n<body>\n"
		)
		f.write(htmlText)
		f.write("\n</body>\n</html>")

def mdTool(env):
	mdAction=env.Action(
		lambda target,source,env: md2html(source[0].path, target[0].path),
		lambda target,source,env: 'Generating %s'%target[0],
	)
	mdBuilder=env.Builder(
		action=mdAction,
		suffix='.html',
		src_suffix='.md',
	)
	env['BUILDERS']['markdown']=mdBuilder

vars = Variables()
vars.Add("version", "The version of this build", buildVars.addon_info["addon_version"])
vars.Add(BoolVariable("dev", "Whether this is a daily development version", False))
vars.Add("channel", "Update channel for this build", buildVars.addon_info["addon_updateChannel"])

env = Environment(variables=vars, ENV=os.environ, tools=['gettexttool', mdTool])
env.Append(**buildVars.addon_info)

if env["dev"]:
	import datetime
	buildDate = datetime.datetime.now()
	year, month, day = str(buildDate.year), str(buildDate.month), str(buildDate.day)
	env["addon_version"] = "".join([year, month.zfill(2), day.zfill(2), "-dev"])
	env["channel"] = "dev"
elif env["version"] is not None:
	env["addon_version"] = env["version"]
if "channel" in env and env["channel"] is not None:
	env["addon_updateChannel"] = env["channel"]

addonFile = env.File("${addon_name}-${addon_version}.nvda-addon")

def addonGenerator(target, source, env, for_signature):
	action = env.Action(lambda target, source, env : createAddonBundleFromPath(source[0].abspath, target[0].abspath) and None,
	lambda target, source, env : "Generating Addon %s" % target[0])
	return action

def manifestGenerator(target, source, env, for_signature):
	action = env.Action(lambda target, source, env : generateManifest(source[0].abspath, target[0].abspath) and None,
	lambda target, source, env : "Generating manifest %s" % target[0])
	return action

def translatedManifestGenerator(target, source, env, for_signature):
	dir = os.path.abspath(os.path.join(os.path.dirname(str(source[0])), ".."))
	lang = os.path.basename(dir)
	action = env.Action(lambda target, source, env : generateTranslatedManifest(source[1].abspath, lang, target[0].abspath) and None,
	lambda target, source, env : "Generating translated manifest %s" % target[0])
	return action

env['BUILDERS']['NVDAAddon'] = Builder(generator=addonGenerator)
env['BUILDERS']['NVDAManifest'] = Builder(generator=manifestGenerator)
env['BUILDERS']['NVDATranslatedManifest'] = Builder(generator=translatedManifestGenerator)

def createAddonHelp(dir):
	docsDir = os.path.join(dir, "doc")
	if os.path.isfile("style.css"):
		cssPath = os.path.join(docsDir, "style.css")
		cssTarget = env.Command(cssPath, "style.css", Copy("$TARGET", "$SOURCE"))
		env.Depends(addon, cssTarget)
	if os.path.isfile("readme.md"):
		readmePath = os.path.join(docsDir, "en", "readme.md")
		readmeTarget = env.Command(readmePath, "readme.md", Copy("$TARGET", "$SOURCE"))
		env.Depends(addon, readmeTarget)

def createAddonBundleFromPath(path, dest):
	""" Creates a bundle from a directory that contains an addon manifest file."""
	basedir = os.path.abspath(path)
	with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
		# FIXME: the include/exclude feature may or may not be useful. Also python files can be pre-compiled.
		for dir, dirnames, filenames in os.walk(basedir):
			relativePath = os.path.relpath(dir, basedir)
			for filename in filenames:
				pathInBundle = os.path.join(relativePath, filename)
				absPath = os.path.join(dir, filename)
				if pathInBundle not in buildVars.excludedFiles: z.write(absPath, pathInBundle)
	return dest

def generateManifest(source, dest):
	addon_info = buildVars.addon_info
	addon_info["addon_version"] = env["addon_version"]
	addon_info["addon_updateChannel"] = env["addon_updateChannel"]
	with codecs.open(source, "r", "utf-8") as f:
		manifest_template = f.read()
	manifest = manifest_template.format(**addon_info)
	with codecs.open(dest, "w", "utf-8") as f:
		f.write(manifest)

def generateTranslatedManifest(source, language, out):
	_ = gettext.translation("nvda", localedir=os.path.join("addon", "locale"), languages=[language]).ugettext
	vars = {}
	for var in ("addon_summary", "addon_description"):
		vars[var] = _(buildVars.addon_info[var])
	with codecs.open(source, "r", "utf-8") as f:
		manifest_template = f.read()
	result = manifest_template.format(**vars)
	with codecs.open(out, "w", "utf-8") as f:
		f.write(result)

def expandGlobs(files):
	return [f for pattern in files for f in env.Glob(pattern)]

addon = env.NVDAAddon(addonFile, env.Dir('addon'))

langDirs = [f for f in env.Glob(os.path.join("addon", "locale", "*"))]

#Allow all NVDA's gettext po files to be compiled in source/locale, and manifest files to be generated
for dir in langDirs:
	poFile = dir.File(os.path.join("LC_MESSAGES", "nvda.po"))
	moFile=env.gettextMoFile(poFile)
	env.Depends(moFile, poFile)
	translatedManifest = env.NVDATranslatedManifest(dir.File("manifest.ini"), [moFile, os.path.join("manifest-translated.ini.tpl")])
	env.Depends(translatedManifest, ["buildVars.py"])
	env.Depends(addon, [translatedManifest, moFile])

pythonFiles = expandGlobs(buildVars.pythonSources)
for file in pythonFiles:
	env.Depends(addon, file)

#Convert markdown files to html
createAddonHelp("addon") # We need at least doc in English and should enable the Help button for the add-on in Add-ons Manager
for mdFile in env.Glob(os.path.join('addon', 'doc', '*', '*.md')):
	htmlFile = env.markdown(mdFile)
	env.Depends(htmlFile, mdFile)
	env.Depends(addon, htmlFile)

# Pot target
i18nFiles = expandGlobs(buildVars.i18nSources)
gettextvars={
		'gettext_package_bugs_address' : 'nvda-translations@freelists.org',
		'gettext_package_name' : buildVars.addon_info['addon_name'],
		'gettext_package_version' : buildVars.addon_info['addon_version']
	}

pot = env.gettextPotFile("${addon_name}.pot", i18nFiles, **gettextvars)
env.Alias('pot', pot)
env.Depends(pot, i18nFiles)
mergePot = env.gettextMergePotFile("${addon_name}-merge.pot", i18nFiles, **gettextvars)
env.Alias('mergePot', mergePot)
env.Depends(mergePot, i18nFiles)

# Generate Manifest path
manifest = env.NVDAManifest(os.path.join("addon", "manifest.ini"), os.path.join("manifest.ini.tpl"))
# Ensure manifest is rebuilt if buildVars is updated.
env.Depends(manifest, "buildVars.py")

env.Depends(addon, manifest)
env.Default(addon)

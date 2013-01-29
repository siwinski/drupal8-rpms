PWD              = $(shell pwd)
RPMBUILD_OPTIONS = --define "_topdir $(PWD)/rpmbuild"
SPECTOOL_OPTIONS = --get-files --directory '$(PWD)/rpmbuild/SOURCES'

# TARGET: help      Print this information
.PHONY: help
help:
	# Usage:
	#   make <target>
	#
	# Targets:
	@egrep "^# TARGET:" [Mm]akefile | sed 's/^# TARGET:\s*/#   /'

# TARGET: setup     Setup
.PHONY: setup
setup:
	@mkdir -p -m 755 ./rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS}

# TARGET: core      Make core RPMs
.PHONY: core
core: CORE_SOURCE=$(shell spectool --list-files core/drupal8.spec | grep '^Source0:' | sed 's/Source0:\s*//' | xargs basename)
core: setup
	@[ -e rpmbuild/SOURCES/$(CORE_SOURCE) ] || spectool $(SPECTOOL_OPTIONS) core/drupal8.spec
	@[ -e core/$(CORE_SOURCE) ] || ln -s ../rpmbuild/SOURCES/$(CORE_SOURCE) core/$(CORE_SOURCE)
	rpmbuild $(RPMBUILD_OPTIONS) --define '_sourcedir $(PWD)/core' -ba core/drupal8.spec

# TARGET: modules   Make all module RPMs
.PHONY: modules
modules: setup

# TARGET: themes    Make all theme RPMs
.PHONY: themes
themes: setup

# TARGET: profiles  Make all profile RPMs
.PHONY: profiles
profiles: setup

# TARGET: all       Make all core, module, theme, and profile RPMs
#.PHONY: all
all: core modules themes profiles

# TARGET: clean     Delete any temporary or generated files
.PHONY: clean
clean:
	rm -rf ./rpmbuild
	find . -name '*~' -delete
	find . -name '*.gz' -delete
	find . -name '*.tgz' -delete
	find . -name '*.rpm' -delete

PWD              = $(shell pwd)
RPMBUILD_OPTIONS = --define "_topdir $(PWD)/rpmbuild"
SPECTOOL_OPTIONS = --get-files --directory '$(PWD)/rpmbuild/SOURCES'

RPM_DIST         = $(shell rpm --eval '%{dist}')
REPO_RELEASE     = $(shell \
						if [ ".fc18" == "$(RPM_DIST)" ]; then \
							echo "fedora-18"; \
						elif [ ".el6" == "$(RPM_DIST)" ]; then \
							echo "epel-6"; \
						fi)
REPO_PATH        = fedorapeople.org:/srv/repos/siwinski/drupal8/$(REPO_RELEASE)

# TARGET: help          Print this information
.PHONY: help
help:
	# Usage:
	#   make <target>
	#
	# Targets:
	@egrep "^# TARGET:" [Mm]akefile | sed 's/^# TARGET:\s*/#   /'

# TARGET: setup         Setup rpmbuild directories
.PHONY: setup
setup:
	@mkdir -p -m 755 ./rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS}
	@mkdir -p -m 755 ./rpmbuild/RPMS/noarch

# TARGET: core          Make core RPMs
.PHONY: core
core: CORE_SOURCE=$(shell spectool --list-files core/drupal8.spec | grep '^Source0:' | sed 's/Source0:\s*//' | xargs basename)
core: setup
	@[ -e rpmbuild/SOURCES/$(CORE_SOURCE) ] || spectool $(SPECTOOL_OPTIONS) core/drupal8.spec
	@[ -e core/$(CORE_SOURCE) ] || ln -s ../rpmbuild/SOURCES/$(CORE_SOURCE) core/$(CORE_SOURCE)
	rpmbuild $(RPMBUILD_OPTIONS) --define '_sourcedir $(PWD)/core' -ba core/drupal8.spec

# TARGET: modules       Make all module RPMs
.PHONY: modules
modules: setup

# TARGET: themes        Make all theme RPMs
.PHONY: themes
themes: setup

# TARGET: profiles      Make all profile RPMs
.PHONY: profiles
profiles: setup

# TARGET: all           Make all core, module, theme, and profile RPMs
.PHONY: all
all: core modules themes profiles

# TARGET: rpmlint       Run rpmlint on all spec files
.PHONY: rpmlint
rpmlint:
	@echo ""
	@for SPEC in */*.spec; do \
		echo "-------------------- $$SPEC --------------------"; \
		rpmlint ./$$SPEC; \
		echo ""; \
	done

# TARGET: repos-create  Create RPM and SRPM repos
.PHONY: repos
repos-create: repos-pull
	@echo "-------------------- Create SRPMS repo --------------------"
	createrepo --update -v rpmbuild/SRPMS/
	@echo ""
	@echo "-------------------- Create RPMS repo --------------------"
	createrepo --update -v rpmbuild/RPMS/noarch/

# TARGET: repos-pull    Pull repos from fedorapeople.org
.PHONY: repos-pull
repos-pull: setup
	@[ "" != "$(REPO_RELEASE)" ] || \
		(echo "ERROR: Invalid distribution" 1>&2; exit 1)
	@echo "-------------------- Pull SRPMS repo --------------------"
	rsync -rlptv $(REPO_PATH)/SRPMS/ rpmbuild/SRPMS/
	@echo "-------------------- Pull RPMS repo --------------------"
	rsync -rlptv $(REPO_PATH)/noarch/ rpmbuild/RPMS/noarch/


# TARGET: clean         Delete any temporary or generated files
.PHONY: clean
clean:
	rm -rf ./rpmbuild
	find . -name '*~' -delete
	find . -name '*.gz' -delete
	find . -name '*.tgz' -delete
	find . -name '*.rpm' -delete

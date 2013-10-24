# See WARNING notes in %%description

%global git_commit       784cebbe5a3ef9caa2211bca9a0ac1e510c6bb7a
%global git_commit_short %(c=%{git_commit}; echo ${c:0:7})
%global git_release      alpha4

%global drupal8          %{_datadir}/drupal8

Name:      drupal8
Version:   8.0
Release:   0.8.%{git_release}%{?dist}
Summary:   An open source content management platform

Group:     Applications/Publishing
License:   GPLv2+
URL:       http://drupal.org/community-initiatives/drupal-core
Source0:   http://drupalcode.org/project/drupal.git/snapshot/%{git_commit}.tar.gz
# RPM "magic"
Source1:   macros.%{name}
Source2:   %{name}.attr
Source3:   %{name}.prov
Source4:   %{name}.req
# Apache HTTPD conf
Source5:   %{name}.conf

BuildArch: noarch

# Drupal lists a minimum version of PHP 5.3.10, but phpci only finds a minimum
# version of 5.3.0 for core.  Since RHEL only provides PHP 5.3.3, let's try
# 5.3.3 as a minimum version so we can test on RHEL as well.  This will need
# to be changed to 5.3.5 before actual release and therefore most likely will
# not be released in EPEL.
#
# See:
# * "Bump minimum version of php required to 5.3.5" http://drupal.org/node/1751100
# * "Bump minimum version of php required to 5.3.10" http://drupal.org/node/1800122
Requires:  php >= 5.3.3

Requires:  php-Assetic
Requires:  php-EasyRdf
Requires:  php-pear(pear.symfony.com/ClassLoader) < 2.4
Requires:  php-pear(pear.symfony.com/DependencyInjection) < 2.4
Requires:  php-pear(pear.symfony.com/EventDispatcher) < 2.4
Requires:  php-pear(pear.symfony.com/HttpFoundation) < 2.4
Requires:  php-pear(pear.symfony.com/HttpKernel) < 2.4
Requires:  php-pear(pear.symfony.com/Routing) < 2.4
Requires:  php-pear(pear.symfony.com/Serializer) < 2.4
Requires:  php-pear(pear.symfony.com/Validator) < 2.4
Requires:  php-pear(pear.symfony.com/Yaml) < 2.4
Requires:  php-pear(pear.twig-project.org/Twig) >= 1.0
Requires:  php-pear(pear.twig-project.org/Twig) <  2.0
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) >= 2.3.0
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) <  2.4.0
Requires:  php-pear(guzzlephp.org/pear/Guzzle)
Requires:  php-pear(pear.phpunit.de/PHPUnit)
Requires:  php-PsrLog
Requires:  php-SymfonyCmfRouting
# phpcompatinfo
Requires:  php-bcmath
Requires:  php-bz2
Requires:  php-core
Requires:  php-ctype
Requires:  php-curl
Requires:  php-date
Requires:  php-dom
Requires:  php-filter
Requires:  php-ftp
Requires:  php-gd
Requires:  php-gmp
Requires:  php-hash
Requires:  php-iconv
Requires:  php-intl
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-recode
Requires:  php-reflection
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-standard
Requires:  php-xml
Requires:  php-zip
Requires:  php-zlib

# Virtual provides
## Core
Provides:  drupal8(core) = %{version}
## Modules
Provides:  drupal8(action) = %{version}
Provides:  drupal8(aggregator) = %{version}
Provides:  drupal8(ban) = %{version}
Provides:  drupal8(block) = %{version}
Provides:  drupal8(book) = %{version}
Provides:  drupal8(breakpoint) = %{version}
Provides:  drupal8(ckeditor) = %{version}
Provides:  drupal8(color) = %{version}
Provides:  drupal8(comment) = %{version}
Provides:  drupal8(config) = %{version}
Provides:  drupal8(contact) = %{version}
Provides:  drupal8(contextual) = %{version}
Provides:  drupal8(custom_block) = %{version}
Provides:  drupal8(datetime) = %{version}
Provides:  drupal8(dblog) = %{version}
Provides:  drupal8(edit) = %{version}
Provides:  drupal8(editor) = %{version}
Provides:  drupal8(email) = %{version}
Provides:  drupal8(entity) = %{version}
Provides:  drupal8(entity_reference) = %{version}
Provides:  drupal8(field) = %{version}
Provides:  drupal8(field_sql_storage) = %{version}
Provides:  drupal8(field_ui) = %{version}
Provides:  drupal8(file) = %{version}
Provides:  drupal8(filter) = %{version}
Provides:  drupal8(forum) = %{version}
Provides:  drupal8(hal) = %{version}
Provides:  drupal8(help) = %{version}
Provides:  drupal8(history) = %{version}
Provides:  drupal8(image) = %{version}
Provides:  drupal8(language) = %{version}
Provides:  drupal8(layout) = %{version}
Provides:  drupal8(link) = %{version}
Provides:  drupal8(locale) = %{version}
Provides:  drupal8(menu) = %{version}
Provides:  drupal8(menu_link) = %{version}
Provides:  drupal8(node) = %{version}
Provides:  drupal8(number) = %{version}
Provides:  drupal8(options) = %{version}
Provides:  drupal8(overlay) = %{version}
Provides:  drupal8(path) = %{version}
Provides:  drupal8(php) = %{version}
Provides:  drupal8(picture) = %{version}
Provides:  drupal8(rdf) = %{version}
Provides:  drupal8(rest) = %{version}
Provides:  drupal8(search) = %{version}
Provides:  drupal8(serialization) = %{version}
Provides:  drupal8(shortcut) = %{version}
Provides:  drupal8(simpletest) = %{version}
Provides:  drupal8(statistics) = %{version}
Provides:  drupal8(syslog) = %{version}
Provides:  drupal8(system) = %{version}
Provides:  drupal8(taxonomy) = %{version}
Provides:  drupal8(telephone) = %{version}
Provides:  drupal8(text) = %{version}
Provides:  drupal8(toolbar) = %{version}
Provides:  drupal8(tour) = %{version}
Provides:  drupal8(tracker) = %{version}
Provides:  drupal8(translation_entity) = %{version}
Provides:  drupal8(update) = %{version}
Provides:  drupal8(user) = %{version}
Provides:  drupal8(views) = %{version}
Provides:  drupal8(views_ui) = %{version}
Provides:  drupal8(xmlrpc) = %{version}
## Themes
Provides:  drupal8(bartik) = %{version}
Provides:  drupal8(seven) = %{version}
Provides:  drupal8(stark) = %{version}
## Profiles
Provides:  drupal8(minimal) = %{version}
Provides:  drupal8(standard) = %{version}

%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.

WARNING: This package does not use the exact dependency versions listed in
         core's composer.json because they are not available. Right now this
         package is simply trying to make sure core and its' "RPM magic"
         (%{name}-rpmbuild package) can be packaged correctly.  The running
         of tests with the available dependency versions will be added in
         the future.

         composer.json: http://drupalcode.org/project/drupal.git/blob/%{git_commit}:/composer.json

WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/drupal8-rpms/issues and prefix
         your issue title with "[%name] ".


%package rpmbuild
Summary:  Rpmbuild files for %{name}
Group:    Development/Tools
Requires: PyYAML

%description rpmbuild
%{summary}.


%prep
%setup -q -c

pushd drupal-%{git_commit_short}

# Remove unneeded files
find . -name '.git*' -delete
rm -f web.config example.gitignore

# Change PHP minimum version per previous statement regarding min PHP version
sed 's/5.3.10/5.3.3/' -i core/includes/bootstrap.inc

# Symlink vendors (bundled libraries)
# TODO: Not all removed because some are not available as separate packages yet
#       (see TODO's in "Requires: " above)
#
# It would be nice to be able to just symlink the entire vendor directory to a
# global Composer vendor directory kind of like the nodejs/npm packages do for
# node_modules... :) :) :)
# (see https://github.com/siwinski/php-composer-rpms)
#
# doctrine/common
# core/vendor/doctrine/common/lib/Doctrine/Common -> /usr/share/pear/Doctrine/Common
rm -rf core/vendor/doctrine
mkdir -p -m 755 core/vendor/doctrine/common/lib/Doctrine
ln -s %{_datadir}/pear/Doctrine/Common core/vendor/doctrine/common/lib/Doctrine/Common
#
# easyrdf/easyrdf
# core/vendor/easyrdf/easyrdf/lib/EasyRdf.php -> /usr/share/php/EasyRdf.php
# core/vendor/easyrdf/easyrdf/lib/EasyRdf -> /usr/share/php/EasyRdf
rm -rf core/vendor/easyrdf
mkdir -p -m 755 core/vendor/easyrdf/easyrdf/lib
ln -s %{_datadir}/php/EasyRdf.php core/vendor/easyrdf/easyrdf/lib/EasyRdf.php
ln -s %{_datadir}/php/EasyRdf core/vendor/easyrdf/easyrdf/lib/EasyRdf
#
# guzzle/http
# guzzle/* (some additional pkgs installed as dependencies for guzzle/http)
# Lazy-symlinking here (symlink to base Guzzle path instead individual components)
# core/vendor/guzzle/*/Guzzle -> /usr/share/pear/Guzzle
for GUZZLE_COMPONENT in core/vendor/guzzle/*; do
    rm -rf $GUZZLE_COMPONENT/*
    ln -s %{_datadir}/pear/Guzzle $GUZZLE_COMPONENT/Guzzle
done
#
# kriswallsmith/assetic
rm -rf core/vendor/kriswallsmith/assetic/*
mkdir -p -m 0755 core/vendor/kriswallsmith/assetic/src
ln -s %{_datadir}/php/Assetic core/vendor/kriswallsmith/assetic/src/Assetic
ln -s Assetic/functions.php core/vendor/kriswallsmith/assetic/src/functions.php
#
# phpunit/*
# Lazy-symlinking
for PHPUNIT_COMPONENT in core/vendor/phpunit/*; do
    rm -rf $PHPUNIT_COMPONENT
    ln -s %{pear_phpdir} $PHPUNIT_COMPONENT
done
rm -f core/vendor/bin/phpunit
ln -s %{_bindir}/phpunit core/vendor/bin/phpunit
#
# symfony/*
# Lazy-symlinking here (symlink to base Symfony path instead individual components)
# core/vendor/symfony/*/Symfony -> /usr/share/pear/Symfony
for SYMFONY_COMPONENT in core/vendor/symfony/*; do
    rm -rf $SYMFONY_COMPONENT/*
    ln -s %{_datadir}/pear/Symfony $SYMFONY_COMPONENT/Symfony
done
#
# symfony-cmf/routing
rm -rf core/vendor/symfony-cmf/routing/Symfony
ln -s %{_datadir}/php/Symfony core/vendor/symfony-cmf/routing/Symfony
#
# twig/twig
# core/vendor/twig/twig/lib/Twig -> /usr/share/pear/Twig
rm -rf core/vendor/twig
mkdir -p -m 755 core/vendor/twig/twig/lib
ln -s %{_datadir}/pear/Twig core/vendor/twig/twig/lib/Twig
#
# core/vendor/psr/log/Psr -> /usr/share/php/Psr
rm -rf core/vendor/psr/log/*
ln -s %{_datadir}/php/Psr core/vendor/psr/log/Psr

popd

cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .
cp -p %{SOURCE5} .

# Update macros' version and base path
sed -e 's:__DRUPAL8_VERSION__:%version:' \
    -e 's:__DRUPAL8__:%drupal8:' \
    -i macros.%{name}


%build
# Empty build section, nothing to build


%install
pushd drupal-%{git_commit_short}

mkdir -p -m 755 %{buildroot}%{drupal8}
cp -pr * %{buildroot}%{drupal8}/
cp -p .htaccess %{buildroot}%{drupal8}/

# Sites
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{drupal8}/sites/* %{buildroot}%{_sysconfdir}/%{name}/
rmdir %{buildroot}%{drupal8}/sites
ln -s %{_sysconfdir}/%{name} %{buildroot}%{drupal8}/sites

# Files
mkdir -p -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}/files/default
ln -s %{_localstatedir}/lib/%{name}/files/default \
      %{buildroot}%{_sysconfdir}/%{name}/default/files

popd

# RPM "magic"
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/rpm
install -p -m 0644 macros.%{name} %{buildroot}%{_sysconfdir}/rpm/
mkdir -p -m 0755 %{buildroot}%{_rpmconfigdir}/fileattrs
install -p -m 0644 %{name}.attr %{buildroot}%{_rpmconfigdir}/fileattrs/
install -p -m 0755 %{name}.prov %{buildroot}%{_rpmconfigdir}/
install -p -m 0755 %{name}.req %{buildroot}%{_rpmconfigdir}/

# Apache HTTPD conf
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/


%files
# Core
%doc drupal-%{git_commit_short}/README.txt
%doc drupal-%{git_commit_short}/composer.*
%doc drupal-%{git_commit_short}/core/*.txt
%doc drupal-%{git_commit_short}/modules/README.txt
%doc drupal-%{git_commit_short}/profiles/README.txt
%doc drupal-%{git_commit_short}/themes/README.txt
%dir %{drupal8}
     %{drupal8}/.htaccess
     %{drupal8}/*.*
     %{drupal8}/core
%dir %{drupal8}/modules
%dir %{drupal8}/profiles
     %{drupal8}/sites
%dir %{drupal8}/themes
%exclude %{drupal8}/README.txt
%exclude %{drupal8}/composer.*
%exclude %{drupal8}/core/*.txt
%exclude %{drupal8}/modules/README.txt
%exclude %{drupal8}/profiles/README.txt
%exclude %{drupal8}/themes/README.txt
# Sites
%doc drupal-%{git_commit_short}/sites/README.txt
%doc drupal-%{git_commit_short}/sites/example.sites.php
%dir     %{_sysconfdir}/%{name}
%dir     %{_sysconfdir}/%{name}/default
%config  %{_sysconfdir}/%{name}/default/default.settings.php
%exclude %{_sysconfdir}/%{name}/README.txt
%exclude %{_sysconfdir}/%{name}/example.sites.php
# Files
%{_sysconfdir}/%{name}/default/files
%dir %attr(775,root,apache) %{_localstatedir}/lib/%{name}
%dir %attr(775,root,apache) %{_localstatedir}/lib/%{name}/files
%dir %attr(775,root,apache) %{_localstatedir}/lib/%{name}/files/default
# Apache HTTPD conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%files rpmbuild
%{_sysconfdir}/rpm/macros.%{name}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%{_rpmconfigdir}/%{name}.req


%changelog
* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.8.alpha4
- Updated to release tag 8.0-alpha4

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.7.20130616git1648a47
- Updated to 2013-06-16 snapshot
- No auto-provide hidden projects
- Static virtual provides instead of dynamic

* Wed Jun 12 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.6.20130612gite952a21
- Updated to 2013-06-12 snapshot

* Sun May 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.5.20130504git5838ea9
- Updated to 2013-05-04 snapshot

* Thu Apr 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.4.20130403giteebd063
- Updated to 2013-04-03 snapshot
- Updated note about PHP minimum version
- Added php-Assetic and php-SymfonyCmfRouting requires
- Removed vendors (bundled libraries) phpci requires
- Updated composer file locations

* Thu Mar 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.3.20130309git3210003
- %%{drupal8}/sites => %%{_sysconfdir}/%%{name}
- Marked Apache config as %%config
- Marked modules/profiles/themes README.txt as %%doc
- Specific dir and file ownership
- Removed example.gitignore
- Added files dir and symlink

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.2.20130309git3210003
- Updated to latest 2013-03-09 snapshot
- *.info => *.info.yml
- Added PyYAML require for rpmbuild sub-package
- Un-bundled PHPUnit

* Mon Feb 25 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.1.20130224git8afbc08
- Initial package

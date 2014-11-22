#
# RPM spec file for drupal8
#
# Copyright (c) 2013-2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# See https://github.com/siwinski/drupal8-rpms (see README.md for TODOs)
# See WARNING notes in %%description

# Disable automatic requires/provides processing
AutoReqProv: no

# "php": ">=5.4.5"
%global php_min_ver 5.4.5

# "doctrine/annotations": "1.2.*"
%global doctrine_annotations_min_ver 1.2.0
%global doctrine_annotations_max_ver 2.0.0
# "doctrine/common": "dev-bmaster#a45d110f71c323e29f41eb0696fa230e3fa1b1b5"
# TODO: php-doctrine-common needs to be updated to include this commit
%global doctrine_common_min_ver 2.4.0
%global doctrine_common_max_ver 2.5.0
# "easyrdf/easyrdf": "0.8.*"
%global easyrdf_min_ver 0.8.0
%global easyrdf_max_ver 0.9.0
# "egulias/email-validator": "1.2.*"
%global email_validator_min_ver 1.2.0
%global email_validator_max_ver 1.3.0
# "sdboyer/gliph": "0.1.*"
%global gliph_min_ver 0.1.0
%global gliph_max_ver 0.2.0
# "guzzlehttp/guzzle": "~5.0"
%global guzzle_min_ver 5.0
%global guzzle_max_ver 6.0
# "stack/builder": "1.0.*"
%global stack_builder_min_ver 1.0.0
%global stack_builder_max_ver 1.1.0
# "symfony/*": "2.5.*"
%global symfony_min_ver 2.5.0
%global symfony_max_ver 2.6.0
# "symfony-cmf/routing": "1.3.*"
%global symfony_cmf_routing_min_ver 1.3.0
%global symfony_cmf_routing_max_ver 1.4.0
# "twig/twig": "1.16.*"
%global twig_min_ver 1.16.0
%global twig_max_ver 1.17.0
# "mikey179/vfsStream": "1.*"
%global vfsstream_min_ver 1.0
%global vfsstream_max_ver 2.0
# "zendframework/zend-feed": "2.2.*"
%global zf_min_ver 2.2.0
# DEBUG!!!
%global zf_max_ver 2.4.0

%global pre_release beta3
%global drupal8     %{_datadir}/drupal8
%global macrosdir   %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global source0_dir drupal-%{version}%{?pre_release:-%{pre_release}}

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}


Name:      drupal8
Version:   8.0.0
Release:   0.13%{?pre_release:.%{pre_release}}%{?dist}
Summary:   An open source content management platform

Group:     Applications/Publishing
License:   GPLv2+
URL:       https://drupal.org/drupal-8.0
Source0:   http://ftp.drupal.org/files/projects/drupal-%{version}%{?pre_release:-%{pre_release}}.tar.gz
# RPM "magic"
Source1:   macros.%{name}
Source2:   %{name}.attr
Source3:   %{name}.prov
Source4:   %{name}.req
# Apache HTTPD conf
Source5:   %{name}.conf

BuildArch: noarch

Requires:  httpd
Requires:  mod_php

# composer.json
Requires:  php(language) >= %{php_min_ver}
Requires:  php-phpunit-PHPUnit
Requires:  php-composer(doctrine/annotations)         >= %{doctrine_annotations_min_ver}
Requires:  php-composer(doctrine/annotations)         <  %{doctrine_annotations_max_ver}
Requires:  php-composer(doctrine/common)              >= %{doctrine_common_min_ver}
Requires:  php-composer(doctrine/common)              <  %{doctrine_common_max_ver}
Requires:  php-composer(easyrdf/easyrdf)              >= %{easyrdf_min_ver}
Requires:  php-composer(easyrdf/easyrdf)              <  %{easyrdf_max_ver}
Requires:  php-composer(egulias/email-validator)      >= %{email_validator_min_ver}
Requires:  php-composer(egulias/email-validator)      <  %{email_validator_max_ver}
Requires:  php-composer(guzzlehttp/guzzle)            >= %{guzzle_min_ver}
Requires:  php-composer(guzzlehttp/guzzle)            <  %{guzzle_max_ver}
Requires:  php-composer(mikey179/vfsStream)           >= %{vfsstream_min_ver}
Requires:  php-composer(mikey179/vfsStream)           <  %{vfsstream_max_ver}
Requires:  php-composer(sdboyer/gliph)                >= %{gliph_min_ver}
Requires:  php-composer(sdboyer/gliph)                <  %{gliph_max_ver}
Requires:  php-composer(stack/builder)                >= %{stack_builder_min_ver}
Requires:  php-composer(stack/builder)                <  %{stack_builder_max_ver}
Requires:  php-composer(symfony/class-loader)         >= %{symfony_min_ver}
Requires:  php-composer(symfony/class-loader)         <  %{symfony_max_ver}
Requires:  php-composer(symfony/css-selector)         >= %{symfony_min_ver}
Requires:  php-composer(symfony/css-selector)         <  %{symfony_max_ver}
Requires:  php-composer(symfony/dependency-injection) >= %{symfony_min_ver}
Requires:  php-composer(symfony/dependency-injection) <  %{symfony_max_ver}
Requires:  php-composer(symfony/event-dispatcher)     >= %{symfony_min_ver}
Requires:  php-composer(symfony/event-dispatcher)     <  %{symfony_max_ver}
Requires:  php-composer(symfony/http-foundation)      >= %{symfony_min_ver}
Requires:  php-composer(symfony/http-foundation)      <  %{symfony_max_ver}
Requires:  php-composer(symfony/http-kernel)          >= %{symfony_min_ver}
Requires:  php-composer(symfony/http-kernel)          <  %{symfony_max_ver}
Requires:  php-composer(symfony/routing)              >= %{symfony_min_ver}
Requires:  php-composer(symfony/routing)              <  %{symfony_max_ver}
Requires:  php-composer(symfony/serializer)           >= %{symfony_min_ver}
Requires:  php-composer(symfony/serializer)           <  %{symfony_max_ver}
Requires:  php-composer(symfony/validator)            >= %{symfony_min_ver}
Requires:  php-composer(symfony/validator)            <  %{symfony_max_ver}
Requires:  php-composer(symfony/yaml)                 >= %{symfony_min_ver}
Requires:  php-composer(symfony/yaml)                 <  %{symfony_max_ver}
Requires:  php-composer(symfony-cmf/routing)          >= %{symfony_cmf_routing_min_ver}
Requires:  php-composer(symfony-cmf/routing)          <  %{symfony_cmf_routing_max_ver}
Requires:  php-composer(twig/twig)                    >= %{twig_min_ver}
Requires:  php-composer(twig/twig)                    <  %{twig_max_ver}
Requires:  php-composer(zendframework/zend-feed)      >= %{zf_min_ver}
Requires:  php-composer(zendframework/zend-feed)      <  %{zf_max_ver}
# phpcompatinfo (computed from version 8.0-alpha13)
Requires:  php-bz2
Requires:  php-ctype
Requires:  php-curl
Requires:  php-date
Requires:  php-dom
Requires:  php-filter
Requires:  php-ftp
Requires:  php-gd
Requires:  php-hash
Requires:  php-iconv
Requires:  php-intl
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-recode
Requires:  php-reflection
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-tokenizer
Requires:  php-xml
Requires:  php-zip
Requires:  php-zlib

# Virtual provides
## Core
Provides:  drupal8(core)                = %{version}
## Modules
Provides:  drupal8(action)              = %{version}
Provides:  drupal8(aggregator)          = %{version}
Provides:  drupal8(ban)                 = %{version}
Provides:  drupal8(basic_auth)          = %{version}
Provides:  drupal8(block)               = %{version}
Provides:  drupal8(block_content)       = %{version}
Provides:  drupal8(book)                = %{version}
Provides:  drupal8(breakpoint)          = %{version}
Provides:  drupal8(ckeditor)            = %{version}
Provides:  drupal8(color)               = %{version}
Provides:  drupal8(comment)             = %{version}
Provides:  drupal8(config)              = %{version}
Provides:  drupal8(config_translation)  = %{version}
Provides:  drupal8(contact)             = %{version}
Provides:  drupal8(content_translation) = %{version}
Provides:  drupal8(contextual)          = %{version}
Provides:  drupal8(custom_block)        = %{version}
Provides:  drupal8(datetime)            = %{version}
Provides:  drupal8(dblog)               = %{version}
Provides:  drupal8(editor)              = %{version}
Provides:  drupal8(entity)              = %{version}
Provides:  drupal8(entity_reference)    = %{version}
Provides:  drupal8(field)               = %{version}
Provides:  drupal8(field_ui)            = %{version}
Provides:  drupal8(file)                = %{version}
Provides:  drupal8(filter)              = %{version}
Provides:  drupal8(forum)               = %{version}
Provides:  drupal8(hal)                 = %{version}
Provides:  drupal8(help)                = %{version}
Provides:  drupal8(history)             = %{version}
Provides:  drupal8(image)               = %{version}
Provides:  drupal8(language)            = %{version}
Provides:  drupal8(link)                = %{version}
Provides:  drupal8(locale)              = %{version}
Provides:  drupal8(menu_link)           = %{version}
Provides:  drupal8(menu_ui)             = %{version}
Provides:  drupal8(migrate)             = %{version}
Provides:  drupal8(migrate_drupal)      = %{version}
Provides:  drupal8(node)                = %{version}
Provides:  drupal8(options)             = %{version}
Provides:  drupal8(path)                = %{version}
Provides:  drupal8(quickedit)           = %{version}
Provides:  drupal8(rdf)                 = %{version}
Provides:  drupal8(responsive_image)    = %{version}
Provides:  drupal8(rest)                = %{version}
Provides:  drupal8(search)              = %{version}
Provides:  drupal8(serialization)       = %{version}
Provides:  drupal8(shortcut)            = %{version}
Provides:  drupal8(simpletest)          = %{version}
Provides:  drupal8(statistics)          = %{version}
Provides:  drupal8(syslog)              = %{version}
Provides:  drupal8(system)              = %{version}
Provides:  drupal8(taxonomy)            = %{version}
Provides:  drupal8(telephone)           = %{version}
Provides:  drupal8(text)                = %{version}
Provides:  drupal8(toolbar)             = %{version}
Provides:  drupal8(tour)                = %{version}
Provides:  drupal8(tracker)             = %{version}
Provides:  drupal8(update)              = %{version}
Provides:  drupal8(user)                = %{version}
Provides:  drupal8(views)               = %{version}
Provides:  drupal8(views_ui)            = %{version}
Provides:  drupal8(xmlrpc)              = %{version}
## Themes
Provides:  drupal8(bartik)              = %{version}
Provides:  drupal8(seven)               = %{version}
Provides:  drupal8(stark)               = %{version}
## Profiles
Provides:  drupal8(minimal)             = %{version}
Provides:  drupal8(standard)            = %{version}
## Composer
Provides:  php-composer(drupal/drupal)  = %{version}

%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.

WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/drupal8-rpms/issues and prefix
         your issue title with "[%name] ".

Optional:
* APC (php-pecl-apc)
* pthreads (http://pecl.php.net/package/pthreads)


%package rpmbuild
Summary:  Rpmbuild files for %{name}
Group:    Development/Tools
Requires: PyYAML

%description rpmbuild
%{summary}.


%prep
%setup -q -c

pushd %{source0_dir}

# Remove unneeded files
find . -name '.git*' -delete
rm -f web.config core/vendor/composer/installed.json

# Apache .htaccess
sed 's!# RewriteBase /$!# RewriteBase /\n  RewriteBase /drupal8!' \
    -i .htaccess

# Update php bin
sed 's#/bin/php#%{_bindir}/php#' \
    -i core/scripts/switch-psr4.sh \
    -i core/scripts/update-countries.sh

# Update phpunit bin
sed -e 's#DRUPAL_ROOT . "/core/vendor/phpunit/phpunit/composer/bin/phpunit"#"%{_bindir}/phpunit"#' \
    -e 's#DRUPAL_ROOT . "/core/vendor/bin/phpunit"#"%{_bindir}/phpunit"#' \
    -i core/modules/simpletest/simpletest.module

# Set Composer autoload to use include path
sed 's#\$loader->register(true);#\$loader->setUseIncludePath(true);\n        \$loader->register(true);#' \
    -i core/vendor/composer/autoload_real.php

# Fix Composer autoload files
sed "/react\/promise\/src\/functions.php/s#.*#    '%{_datadir}/php/React/Promise/functions.php',#" \
    -i core/vendor/composer/autoload_files.php

# Remove bundled Composer libraries
for BUNDLED_LIBRARY in doctrine easyrdf egulias guzzlehttp mikey179 phpunit psr react sdboyer sebastian stack symfony symfony-cmf twig zendframework
do
    # Bundled library itself
    rm -rf "core/vendor/${BUNDLED_LIBRARY}"

    # Autoloader class map, namespaces, and include paths
    sed "/\$vendorDir\s*.\s*'\/${BUNDLED_LIBRARY}\//d" \
        -i core/vendor/composer/autoload_classmap.php \
        -i core/vendor/composer/autoload_namespaces.php \
        -i core/vendor/composer/include_paths.php
done
rm -f core/vendor/bin/phpunit

# Fix script-without-shebang
chmod -x \
    LICENSE.txt \
    core/misc/icons/73b355/check.svg \
    core/misc/icons/e29700/warning.svg \
    core/misc/icons/ea2800/error.svg \
    core/modules/ban/src/BanIpManagerInterface.php \
    core/modules/simpletest/src/Tests/SimpleTestTest.php \
    core/modules/system/src/Tests/Database/DeleteTruncateTest.php

popd

# RPM "magic"
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .

# Apache HTTPD conf
cp -p %{SOURCE5} .

# Update macros' version and base path
sed -e 's:__DRUPAL8_VERSION__:%version:' \
    -e 's:__DRUPAL8__:%drupal8:' \
    -i macros.%{name}


%build
# Empty build section, nothing to build


%install
pushd %{source0_dir}

# Main
mkdir -pm 0755 %{buildroot}%{drupal8}
cp -pr * %{buildroot}%{drupal8}/

# Sites
mkdir -pm 0755 %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{drupal8}/sites/* %{buildroot}%{_sysconfdir}/%{name}/
rmdir %{buildroot}%{drupal8}/sites
ln -s %{_sysconfdir}/%{name} %{buildroot}%{drupal8}/sites

# Files
mkdir -pm 0755 %{buildroot}%{_localstatedir}/lib/%{name}/{public,private}/default
ln -s %{_localstatedir}/lib/%{name}/public/default \
      %{buildroot}%{_sysconfdir}/%{name}/default/files
ln -s public %{buildroot}%{_localstatedir}/lib/%{name}/files

# Apache .htaccess
mkdir -pm 0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 .htaccess %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.htaccess
ln -s %{_sysconfdir}/httpd/conf.d/%{name}.htaccess %{buildroot}%{drupal8}/.htaccess

popd

# RPM "magic"
mkdir -pm 0755 %{buildroot}%{macrosdir}
install -pm 0644 macros.%{name} %{buildroot}%{macrosdir}/
mkdir -pm 0755 %{buildroot}%{_rpmconfigdir}/fileattrs
install -pm 0644 %{name}.attr %{buildroot}%{_rpmconfigdir}/fileattrs/
install -pm 0755 %{name}.prov %{buildroot}%{_rpmconfigdir}/
install -pm 0755 %{name}.req %{buildroot}%{_rpmconfigdir}/

# Apache HTTPD conf
install -pm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/


%check
# Ensure RewriteBase
grep 'RewriteBase /drupal8' \
        %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.htaccess \
        --quiet \
    || exit 1

pushd %{source0_dir}

# Ensure php bin updated
grep -r '#!/bin/php' . && exit 1

# Ensure phpunit bin updated
grep 'core/vendor' core/modules/simpletest/simpletest.module && exit 1

# TODO: Ensure all bundled libraries removed

%if %{with_tests}
# Unit tests
pushd core

# Skip certain tests that require the "willReturn" function in PHPUnit MockObject > 2
#   Note: This is because of PHPUnit < 4.1
%if 0%{?fedora} < 21 && 0%{?rhel} < 7
sed 's/function testSetError/function SKIP_testSetError/' \
    -i tests/Drupal/Tests/Core/Form/FormStateTest.php
sed -e 's/function testRedirectWithResult/function SKIP_testRedirectWithResult/' \
    -e 's/function testRedirectWithRouteWithResult/function SKIP_testRedirectWithRouteWithResult/' \
    -e 's/function testRedirectWithResponseObject/function SKIP_testRedirectWithResponseObject/' \
    -e 's/function testRedirectWithoutResult/function SKIP_testRedirectWithoutResult/' \
    -i tests/Drupal/Tests/Core/Form/FormSubmitterTest.php
%endif

# Skip tests with PHPUnit 4.2+ deprecated functions
#   Note: This is because of PHPUnit > 4.1
#   See:  https://www.drupal.org/node/2331685
%if 0%{?fedora} >= 21 && 0%{?rhel} >= 7
# assertTag
rm -f tests/Drupal/Tests/Core/Utility/LinkGeneratorTest.php
# assertSelectEquals
sed 's/function testPrint/function SKIP_testPrint/' \
    -i tests/Drupal/Tests/Core/Template/AttributeTest.php
%endif

# Symfony DependencyInjection pkg does not include test files so skip this test
rm -f tests/Drupal/Tests/Core/DependencyInjection/ContainerBuilderTest.php

%{__phpunit}

popd
%else
: Test suite skipped
%endif

popd


%files
# Core
%doc %{source0_dir}/README.txt
%doc %{source0_dir}/composer.*
%doc %{source0_dir}/core/*.txt
%doc %{source0_dir}/example.*
%dir %{drupal8}
     %{drupal8}/.htaccess
     %{drupal8}/*.*
     %{drupal8}/core
%dir %{drupal8}/modules
     %{drupal8}/modules/README.txt
%dir %{drupal8}/profiles
     %{drupal8}/profiles/README.txt
     %{drupal8}/sites
%dir %{drupal8}/themes
     %{drupal8}/themes/README.txt
# Sites
%dir %{_sysconfdir}/%{name}
     %{_sysconfdir}/%{name}/*.*
%dir %{_sysconfdir}/%{name}/default
     %{_sysconfdir}/%{name}/default/*.*
# Files
%{_sysconfdir}/%{name}/default/files
%dir                         %{_localstatedir}/lib/%{name}
                             %{_localstatedir}/lib/%{name}/files
%dir                         %{_localstatedir}/lib/%{name}/private
%dir %attr(0775,root,apache) %{_localstatedir}/lib/%{name}/private/default
%dir                         %{_localstatedir}/lib/%{name}/public
%dir %attr(0775,root,apache) %{_localstatedir}/lib/%{name}/public/default
# Apache
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.htaccess

%files rpmbuild
%{macrosdir}/macros.%{name}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%{_rpmconfigdir}/%{name}.req


%changelog
* Sat Nov 22 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0.0-0.13.beta3
- Updated to 8.0.0-beta3

* Wed Jul 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.12.alpha13
- Updated to 8.0-alpha13

* Sun Jun 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.11.alpha12
- Updated to 8.0-alpha12

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.10.alpha11
- Updated to 8.0-alpha11
- Many more changes...

* Sun Jan 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.9.alpha7
- Updated to release tag 8.0-alpha7
- Updated URL
- Moved .htaccess file to Apache conf dir
- Fixed Apache conf file
- Removed PSR Log dependency (dependencies pull this in)
- Unbundle EasyRDF, Gliph, Symfony, Zend Framework 2 Feed
- Added specific file requires to make sure broken dependency if providing
  pkg moves file
- Keep modules, profiles, and themes README files in directories
- Unbundling now uses autoloader instead of symlinks

* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.8.alpha4
- Updated to release tag 8.0-alpha4
- Require correct min PHP version 5.3.10 instead of 5.3.3
- Require correct min/max pkg versions
- Use bundled Doctrine, EasyRdf, Symfony, Symfony CMF Routing, and Twig
  because required versions are not available in Fedora
- Updated phpcompatinfo requires:
  Added: openssl, tokenizer
  Removed: bcmath, gmp

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.7.20130616git1648a47
- Updated to 2013-06-16 snapshot
- No auto-provide hidden projects
- Static virtual provides instead of dynamic

* Wed Jun 12 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.6.20130612gite952a21
- Updated to 2013-06-12 snapshot

* Sun May 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.5.20130504git5838ea9
- Updated to 2013-05-04 snapshot

* Thu Apr 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.4.20130403giteebd063
- Updated to 2013-04-03 snapshot
- Updated note about PHP minimum version
- Added php-Assetic and php-SymfonyCmfRouting requires
- Removed vendors (bundled libraries) phpci requires
- Updated composer file locations

* Thu Mar 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.3.20130309git3210003
- %%{drupal8}/sites => %%{_sysconfdir}/%%{name}
- Marked Apache config as %%config
- Marked modules/profiles/themes README.txt as %%doc
- Specific dir and file ownership
- Removed example.gitignore
- Added files dir and symlink

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.2.20130309git3210003
- Updated to latest 2013-03-09 snapshot
- *.info => *.info.yml
- Added PyYAML require for rpmbuild sub-package
- Un-bundled PHPUnit

* Mon Feb 25 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.1.20130224git8afbc08
- Initial package

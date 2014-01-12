# See WARNING notes in %%description

%global git_commit       c478bf4062e910357c2dd89c9dd069ffd2d959a2
%global git_commit_short %(c=%{git_commit}; echo ${c:0:7})
%global git_release      alpha7

%global drupal8          %{_datadir}/drupal8

# "kriswallsmith/assetic": "1.1.*@alpha"
%global assetic_min_ver             1.1.0
%global assetic_max_ver             1.2.0
# "doctrine/common": "dev-bmaster#99b44f52a1b844f9c4c34e618b160664d5c27daf",
# "doctrine/annotations": "dev-master#463d926a8dcc49271cb7db5a08364a70ed6e3cd3"
%global doctrine_min_ver            2.4.0
%global doctrine_max_ver            2.5.0
# "easyrdf/easyrdf": "0.8.*@beta"
%global easyrdf_min_ver             0.8.0
%global easyrdf_max_ver             0.9.0
# "sdboyer/gliph": "0.1.*"
%global gliph_min_ver               0.1.0
%global gliph_max_ver               0.2.0
# "guzzle/http": "3.7.*"
%global guzzle_min_ver              3.7.0
%global guzzle_max_ver              3.8.0
# "phpunit/phpunit": "3.7.*"
%global phpunit_min_ver             3.7.0
%global phpunit_max_ver             3.8.0
# "symfony/*": "2.3.*"
%global symfony_min_ver             2.3.0
%global symfony_max_ver             2.4.0
# "symfony-cmf/routing": "1.1.*@alpha"
%global symfony_cmf_routing_min_ver 1.1.0
%global symfony_cmf_routing_max_ver 1.2.0
# "twig/twig": "1.12.*"
%global twig_min_ver                1.12.0
%global twig_max_ver                1.13.0
# "zendframework/zend-feed": "2.2.*"
%global zendframework_min_ver       2.2.0
%global zendframework_max_ver       2.3.0

Name:      drupal8
Version:   8.0
Release:   0.9.%{git_release}%{?dist}
Summary:   An open source content management platform

Group:     Applications/Publishing
License:   GPLv2+
URL:       https://drupal.org/drupal-8.0
Source0:   http://drupalcode.org/project/drupal.git/snapshot/%{git_commit}.tar.gz
# RPM "magic"
Source1:   macros.%{name}
Source2:   %{name}.attr
Source3:   %{name}.prov
Source4:   %{name}.req
# Apache HTTPD conf
Source5:   %{name}.conf

BuildArch: noarch

Requires:  php >= 5.3.10

Requires:  php-Assetic                     >= %{assetic_min_ver}
Requires:  php-Assetic                     <  %{assetic_max_ver}
Requires:  php-EasyRdf                     >= %{easyrdf_min_ver}
Requires:  php-EasyRdf                     <  %{easyrdf_max_ver}
Requires:  php-gliph                       >= %{gliph_min_ver}
Requires:  php-gliph                       <  %{gliph_max_ver}
Requires:  php-symfony-classloader         >= %{symfony_min_ver}
Requires:  php-symfony-classloader         <  %{symfony_max_ver}
Requires:  php-symfony-dependencyinjection >= %{symfony_min_ver}
Requires:  php-symfony-dependencyinjection <  %{symfony_max_ver}
Requires:  php-symfony-eventdispatcher     >= %{symfony_min_ver}
Requires:  php-symfony-eventdispatcher     <  %{symfony_max_ver}
Requires:  php-symfony-httpfoundation      >= %{symfony_min_ver}
Requires:  php-symfony-httpfoundation      <  %{symfony_max_ver}
Requires:  php-symfony-httpkernel          >= %{symfony_min_ver}
Requires:  php-symfony-httpkernel          <  %{symfony_max_ver}
Requires:  php-symfony-routing             >= %{symfony_min_ver}
Requires:  php-symfony-routing             <  %{symfony_max_ver}
Requires:  php-symfony-serializer          >= %{symfony_min_ver}
Requires:  php-symfony-serializer          <  %{symfony_max_ver}
Requires:  php-symfony-validator           >= %{symfony_min_ver}
Requires:  php-symfony-validator           <  %{symfony_max_ver}
Requires:  php-symfony-yaml                >= %{symfony_min_ver}
Requires:  php-symfony-yaml                <  %{symfony_max_ver}
Requires:  php-SymfonyCmfRouting           >= %{symfony_cmf_routing_min_ver}
Requires:  php-SymfonyCmfRouting           <  %{symfony_cmf_routing_max_ver}
Requires:  php-ZendFramework2-Feed         >= %{zendframework_min_ver}
Requires:  php-ZendFramework2-Feed         <  %{zendframework_max_ver}
#Requires:  php-doctrine-common             >= %{doctrine_min_ver}
#Requires:  php-doctrine-common             <  %{doctrine_max_ver}
#Requires:  php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
#Requires:  php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
Requires:  php-pear(guzzlephp.org/pear/Guzzle)  >= %{guzzle_min_ver}
Requires:  php-pear(guzzlephp.org/pear/Guzzle)  <  %{guzzle_max_ver}
Requires:  php-pear(pear.phpunit.de/PHPUnit)    >= %{phpunit_min_ver}
Requires:  php-pear(pear.phpunit.de/PHPUnit)    <  %{phpunit_max_ver}
# phpcompatinfo
Requires:  php-bz2
Requires:  php-core
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
Requires:  php-standard
Requires:  php-tokenizer
Requires:  php-xml
Requires:  php-zip
Requires:  php-zlib
# Specific files to make sure broken dependency if providing pkg moves file
Requires:  %{_datadir}/php/Assetic/functions.php

# Virtual provides
## Core
Provides:  drupal8(core)               = %{version}
## Modules
Provides:  drupal8(action)             = %{version}
Provides:  drupal8(aggregator)         = %{version}
Provides:  drupal8(ban)                = %{version}
Provides:  drupal8(block)              = %{version}
Provides:  drupal8(book)               = %{version}
Provides:  drupal8(breakpoint)         = %{version}
Provides:  drupal8(ckeditor)           = %{version}
Provides:  drupal8(color)              = %{version}
Provides:  drupal8(comment)            = %{version}
Provides:  drupal8(config)             = %{version}
Provides:  drupal8(contact)            = %{version}
Provides:  drupal8(contextual)         = %{version}
Provides:  drupal8(custom_block)       = %{version}
Provides:  drupal8(datetime)           = %{version}
Provides:  drupal8(dblog)              = %{version}
Provides:  drupal8(edit)               = %{version}
Provides:  drupal8(editor)             = %{version}
Provides:  drupal8(email)              = %{version}
Provides:  drupal8(entity)             = %{version}
Provides:  drupal8(entity_reference)   = %{version}
Provides:  drupal8(field)              = %{version}
Provides:  drupal8(field_sql_storage)  = %{version}
Provides:  drupal8(field_ui)           = %{version}
Provides:  drupal8(file)               = %{version}
Provides:  drupal8(filter)             = %{version}
Provides:  drupal8(forum)              = %{version}
Provides:  drupal8(hal)                = %{version}
Provides:  drupal8(help)               = %{version}
Provides:  drupal8(history)            = %{version}
Provides:  drupal8(image)              = %{version}
Provides:  drupal8(language)           = %{version}
Provides:  drupal8(layout)             = %{version}
Provides:  drupal8(link)               = %{version}
Provides:  drupal8(locale)             = %{version}
Provides:  drupal8(menu)               = %{version}
Provides:  drupal8(menu_link)          = %{version}
Provides:  drupal8(node)               = %{version}
Provides:  drupal8(number)             = %{version}
Provides:  drupal8(options)            = %{version}
Provides:  drupal8(overlay)            = %{version}
Provides:  drupal8(path)               = %{version}
Provides:  drupal8(php)                = %{version}
Provides:  drupal8(picture)            = %{version}
Provides:  drupal8(rdf)                = %{version}
Provides:  drupal8(rest)               = %{version}
Provides:  drupal8(search)             = %{version}
Provides:  drupal8(serialization)      = %{version}
Provides:  drupal8(shortcut)           = %{version}
Provides:  drupal8(simpletest)         = %{version}
Provides:  drupal8(statistics)         = %{version}
Provides:  drupal8(syslog)             = %{version}
Provides:  drupal8(system)             = %{version}
Provides:  drupal8(taxonomy)           = %{version}
Provides:  drupal8(telephone)          = %{version}
Provides:  drupal8(text)               = %{version}
Provides:  drupal8(toolbar)            = %{version}
Provides:  drupal8(tour)               = %{version}
Provides:  drupal8(tracker)            = %{version}
Provides:  drupal8(translation_entity) = %{version}
Provides:  drupal8(update)             = %{version}
Provides:  drupal8(user)               = %{version}
Provides:  drupal8(views)              = %{version}
Provides:  drupal8(views_ui)           = %{version}
Provides:  drupal8(xmlrpc)             = %{version}
## Themes
Provides:  drupal8(bartik)             = %{version}
Provides:  drupal8(seven)              = %{version}
Provides:  drupal8(stark)              = %{version}
## Profiles
Provides:  drupal8(minimal)            = %{version}
Provides:  drupal8(standard)           = %{version}

%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.

WARNING: This package uses bundled software because the required versions are
         not available in Fedora.  When the required versions are available in
         Fedora this package will be updated to use those.

WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/drupal8-rpms/issues and prefix
         your issue title with "[%name] ".

Optional: APC (php-pecl-apc)


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
rm -f web.config core/vendor/composer/installed.json

# Fix php bin
sed 's#/bin/php#/usr/bin/php#' -i core/scripts/update-countries.sh

# Set Composer autoload to use include path
sed 's#\$loader->register(true);#\$loader->setUseIncludePath(true);\n        \$loader->register(true);#' \
    -i core/vendor/composer/autoload_real.php

# Fix Composer autoload classmap
# NOTE: SessionHandlerInterface is required for PHP < 5.4.0
#       http://php.net/manual/en/class.sessionhandlerinterface.php
sed "/SessionHandlerInterface/s#.*#    'SessionHandlerInterface' => '%{_datadir}/php/Symfony/Component/HttpFoundation/Resources/stubs/SessionHandlerInterface.php',#" \
    -i core/vendor/composer/autoload_classmap.php

# Fix Composer autoload files
sed "/kriswallsmith\/assetic\/src\/functions.php/s#.*#    '%{_datadir}/php/Assetic/functions.php',#" \
    -i core/vendor/composer/autoload_files.php

# Remove bundled Composer libraries
for BUNDLED_LIBRARY in easyrdf guzzle kriswallsmith phpunit psr sdboyer symfony symfony-cmf zendframework
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
pushd drupal-%{git_commit_short}

mkdir -pm 755 %{buildroot}%{drupal8}
cp -pr * %{buildroot}%{drupal8}/
cp -p .htaccess %{buildroot}%{drupal8}/

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

popd

# RPM "magic"
mkdir -pm 0755 %{buildroot}%{_sysconfdir}/rpm
install -pm 0644 macros.%{name} %{buildroot}%{_sysconfdir}/rpm/
mkdir -pm 0755 %{buildroot}%{_rpmconfigdir}/fileattrs
install -pm 0644 %{name}.attr %{buildroot}%{_rpmconfigdir}/fileattrs/
install -pm 0755 %{name}.prov %{buildroot}%{_rpmconfigdir}/
install -pm 0755 %{name}.req %{buildroot}%{_rpmconfigdir}/

# Apache HTTPD conf
mkdir -pm 0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/


%files
# Core
%doc drupal-%{git_commit_short}/README.txt
%doc drupal-%{git_commit_short}/composer.*
%doc drupal-%{git_commit_short}/core/*.txt
%doc drupal-%{git_commit_short}/example.*
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
%exclude %{drupal8}/README.txt
%exclude %{drupal8}/composer.*
%exclude %{drupal8}/core/*.txt
%exclude %{drupal8}/example.*
# Sites
%dir     %{_sysconfdir}/%{name}
%dir     %{_sysconfdir}/%{name}/default
%config  %{_sysconfdir}/%{name}/default/default.settings.php
%exclude %{_sysconfdir}/%{name}/*.txt
%exclude %{_sysconfdir}/%{name}/example.*
# Files
%{_sysconfdir}/%{name}/default/files
%dir                        %{_localstatedir}/lib/%{name}
                            %{_localstatedir}/lib/%{name}/files
%dir                        %{_localstatedir}/lib/%{name}/private
%dir %attr(0775,root,apache) %{_localstatedir}/lib/%{name}/private/default
%dir                        %{_localstatedir}/lib/%{name}/public
%dir %attr(0775,root,apache) %{_localstatedir}/lib/%{name}/public/default
# Apache HTTPD conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%files rpmbuild
%{_sysconfdir}/rpm/macros.%{name}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%{_rpmconfigdir}/%{name}.req


%changelog
* Sun Jan 13 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.9.alpha7
- Updated to release tag 8.0-alpha7

* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.8.alpha4
- Updated to release tag 8.0-alpha4
- Require correct min PHP version 5.3.10 instead of 5.3.3
- Require correct min/max pkg versions
- Use bundled Doctrine, EasyRdf, Symfony, Symfony CMF Routing, and Twig
  because required versions are not available in Fedora
- Updated phpcompatinfo requires:
  Added: openssl, tokenizer
  Removed: bcmath, gmp

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

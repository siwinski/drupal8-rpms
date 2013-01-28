%global module_name      devel
%global module_datestamp 1359204477

Name:          drupal8-%{module_name}
Version:       1.0
Release:       0.%{module_datestamp}%{?dist}
Summary:       Various blocks, pages, and functions for developers

Group:         Applications/Publishing
License:       GPLv2
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-8.x-1.x-dev.tar.gz

BuildArch:     noarch
# For auto-provides and auto-requires
BuildRequires: drupal8-rpmdev

# phpci
Requires:      php-date
Requires:      php-gd
Requires:      php-pcre
Requires:      php-reflection

%description
A suite of modules containing fun for module developers and themers ...

Devel
* Helper functions for Drupal developers and inquisitive admins. This module can
  print a summary of all database queries for each page request at the bottom of
  each page. The summary includes how many times each query was executed on a
  page (shouldn't run same query multiple times), and how long each query took
  (short is good - use cache for complex queries).
* Also a dprint_r($array) function is provided, which pretty prints arrays.
  Useful during development. Similarly, a ddebug_backtrace() is offerred.
* Much more. See this helpful demo page:
  http://ratatosk.net/drupal/tutorials/debugging-drupal.html

Generate content
Accelerate development of your site or module by quickly generating nodes,
comments, terms, users, and more.

Devel Node Access (DNA)
View the node access entries for the node(s) that are shown on a page. Essential
for developers of node access modules and useful for site admins in debugging
problems with those modules.

WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/drupal8-rpms/issues and prefix
         your issue title with "[%name] ".


%prep
%setup -q -c


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{drupal8_modules}
cp -pr %{module_name} %{buildroot}%{drupal8_modules}/


%files
%doc %{module_name}/LICENSE.txt
%doc %{module_name}/README.txt
%{drupal8_modules}/%{module_name}


%changelog
* Sun Jan 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1359204477
- Initial package

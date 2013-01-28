%global module_name      token
%global module_datestamp 1336610910

Name:          drupal8-%{module_name}
Version:       1.0
Release:       0.%{module_datestamp}%{?dist}
Summary:       Provides a user interface for the Token API and some missing core tokens

Group:         Applications/Publishing
License:       GPLv2
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-8.x-1.x-dev.tar.gz

BuildArch:     noarch
# For auto-provides and auto-requires
BuildRequires: drupal8-rpmdev

# phpci
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-pcre

%description
Tokens are small bits of text that can be placed into larger documents via
simple placeholders, like %%site-name or [user]. The Token module provides a
central API for modules to use these tokens, and expose their own token values.

Note that Token module doesn't provide any visible functions to the user on its
own, it just provides token handling services for other modules.

Modules that use the Token module and provide tokens via the API include Organic
Groups, Pathauto, Comment Notify, and Commerce. Also check out the full list of
modules that use or provide tokens or the list of open issues tagged with
'token'.

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
* Sun Jan 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1336610910
- Initial package

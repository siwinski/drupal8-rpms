%global module_name admin_menu

Name:          drupal8-%{module_name}
Version:       3.0
Release:       0.dev%{?dist}
Summary:       Provides a dropdown menu to most administrative tasks

Group:         Applications/Publishing
License:       GPLv2
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-8.x-3.x-dev.tar.gz

BuildArch:     noarch
BuildRequires: drupal8-rpmbuild

# phpci
Requires:      php-date
Requires:      php-pcre
Requires:      php-pdo

%description
***** WARNING: This RPM package is not correctly versioned and will just *****
*****          build the latest DEV version.                             *****

***** WARNING: This is just a development RPM.  Please submit issues at  *****
*****          https://github.com/siwinski/drupal8-rpms/issues and       *****
*****          prefix your issue title with "[%name] ".                  *****

Provides a theme-independent administration interface (aka. navigation,
back-end). It's a helper for novice users coming from other CMS, a time-saver
for site administrators, and useful for developers and site builders.

Administrative links are displayed in a CSS/JS-based menu at the top on all
pages of your site. It not only contains regular menu items — tasks and actions
are also included, enabling fast access to any administrative resource your
Drupal site provides.


%prep
%setup -q -n %{module_name}


%build
# Empty build section, nothing to build


%install
mkdir -p -m 0755 %{buildroot}%{drupal8_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal8_modules}/%{module_name}/


%files
%doc *.txt
%{drupal8_modules}/%{module_name}
%exclude %{drupal8_modules}/%{module_name}/*.txt


%changelog
* Tue Jun 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.0-0.dev
- Initial package

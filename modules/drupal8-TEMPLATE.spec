%global module_name      __MODULE__

Name:          drupal8-%{module_name}
Version:       __VERSION__
Release:       1%{?dist}
Summary:       __SUMMARY__

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-8.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal8-rpmbuild

# phpci
Requires:      php-

%description
__DESCRIPTION__

WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/drupal8-rpms/issues and prefix
         your issue title with "[%name] ".


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
* ddd MMM DD YYYY __NAME__ <__EMAIL__> __VERSION__-1
- Initial package

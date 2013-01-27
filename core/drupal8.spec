%global git_commit 117a617bd81545f68e4eab1e69f0a7f4eb66dd24
%global git_date   20130125

%global git_commit_short %(c=%{git_commit}; echo ${c:0:7})
%global git_release      %{git_date}git%{git_commit_short}

Name:      drupal8
Version:   8.0
Release:   0.1.%{git_release}%{?dist}
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
# Core:    php >= 5.3.0
# Vendors: php >= 5.4.0 (bundled libraries)
Requires:  php >= 5.4.0
# phpci
Requires:  php-bcmath
Requires:  php-bz2
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
Requires:  php-recode
Requires:  php-reflection
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-ssh2
Requires:  php-xml
Requires:  php-zip
Requires:  php-zlib
# phpci: Vendors (bundled libraries)
Requires:  php-fileinfo
Requires:  php-openssl
Requires:  php-pdo
Requires:  php-sockets
Requires:  php-sqlite3
Requires:  php-tokenizer

%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.


%prep
%setup -q -n drupal-%{git_commit_short}

# Remove unnecessary files
rm -f .gitattributes .editorconfig web.config

# Update macros' version and release
cp %{SOURCE1} .
sed -e 's/__DRUPAL8_VERSION__/%version/' \
    -e 's/__DRUPAL8_RELEASE__/%(echo %release | sed 's/%{dist}//')/' \
    -i macros.%{name}


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr * %{buildroot}%{_datadir}/%{name}/
rm -f %{buildroot}%{_datadir}/%{name}/macros.%{name}

# RPM "magic"
install -Dp -m 0644 macros.%{name} %{buildroot}%{_sysconfdir}/rpm/macros.%{name}
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/%{name}.attr
install -Dp -m 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/%{name}.prov
install -Dp -m 0755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/%{name}.req

# Apache HTTPD conf
install -Dp -m 0644 %SOURCE5 %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf


%files
%doc README.txt
%{_datadir}/%{name}
# RPM "magic"
%{_sysconfdir}/rpm/macros.%{name}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%{_rpmconfigdir}/%{name}.req
# Apache HTTPD conf
%{_sysconfdir}/httpd/conf.d/%{name}.conf


%changelog
* Sun Jan 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 8.0-0.1.20130125git117a617
- Initial package

%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	URL2
%define		_status		beta
%define		_pearname	Net_URL2

Summary:	%{_pearname} - easy parsing of URLs
Summary(pl.UTF-8):	%{_pearname} - prosta analiza adresów URL
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b1173c64fdb3c9e7e06d49de10b6bd68
URL:		http://pear.php.net/package/Net_URL2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy parsing of URLs and their constituent parts.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pozwala na prostą analizę adresów URL oraz ich części.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Net_URL2/{docs/example.php,docs/6470.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/URL2.php

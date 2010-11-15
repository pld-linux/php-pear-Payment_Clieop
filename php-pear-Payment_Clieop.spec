%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Payment_Clieop
Summary:	%{_pearname} - create clieop03 file to send to Dutch Bank
Summary(pl.UTF-8):	%{_pearname} - tworzenie pliku clieop03 do wysyłania Dutch Banku
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	261ba9a3f34f5f88e026a74e3bbb42f5
URL:		http://pear.php.net/package/Payment_Clieop/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear > 4:1.0-9.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These classes can create a clieop03 file for you which you can send to
a Dutch Bank. Ofcourse you need also a Dutch bank account.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Te klasy potrafią tworzyć plik clieop03, które można wysyłać do Dutch
Banku. Oczywiście potrzebne jest jeszcze konto w Dutch Banku.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs
mv .%{php_pear_dir}/data/Payment_Clieop/* docs/%{_pearname}/docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Payment/Clieop.php
%{php_pear_dir}/Payment/Clieop

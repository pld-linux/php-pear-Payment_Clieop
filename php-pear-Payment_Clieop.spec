# ToDo:
# - where should Samples/ go ?

%include	/usr/lib/rpm/macros.php
%define		_class		Payment
%define		_subclass	Clieop
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create clieop03 file to send to Dutch Bank
Summary(pl):	%{_pearname} - tworzenie pliku clieop03 do wysy³ania Dutch Banku
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
# Source0-md5:	89ce9d473c0cb61a0d18da6a7966389d
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Payment_Clieop/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These classes can create a clieop03 file for you which you can send to
a Dutch Bank. Ofcourse you need also a Dutch bank account.

This class has in PEAR status: %{_status}.

%description -l pl
Te klasy potrafi± tworzyæ plik clieop03, które mo¿na wysy³aæ do
Dutch Banku. Oczywi¶cie potrzebne jest jeszcze konto w Dutch Banku.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php

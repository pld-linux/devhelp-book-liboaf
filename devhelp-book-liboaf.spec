Summary:	DevHelp book: liboaf
Summary(pl.UTF-8):   Książka do DevHelpa o liboaf
Name:		devhelp-book-liboaf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/liboaf.tar.gz
# Source0-md5:	b0f72225d0332cad34fe16795622313e
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about liboaf.

%description -l pl.UTF-8
Książka do DevHelpa o liboaf.

%prep
%setup -q -c -n liboaf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/liboaf,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/liboaf.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/liboaf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*

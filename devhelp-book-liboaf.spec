Summary:	DevHelp book: liboaf
Summary(pl):	Ksi±¿ka do DevHelp'a o liboaf
Name:		devhelp-book-liboaf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/liboaf.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about liboaf

%description -l pl
Ksi±¿ka do DevHelp o liboaf

%prep
%setup -q -c liboaf -n liboaf

%build
mv -f book liboaf
mv -f book.devhelp liboaf.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/liboaf
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install liboaf.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install liboaf/* $RPM_BUILD_ROOT%{_prefix}/books/liboaf

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs

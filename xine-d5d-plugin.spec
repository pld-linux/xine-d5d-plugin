%define		_name		d5d021
Summary:	DVD CSS input plugin for Xine
Summary(pl):	Plugin odczytu DVD CSS dla Xine
Name:		xine-d5d-plugin
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://debianlinux.net/%{_name}.txt
URL:		http://debianlinux.net/captain_css.html
BuildRequires:	xine-lib-devel >= 0.9.3
BuildRequires:	autoconf
Requires:	xine-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pluginsdir	%{_libdir}/xine/plugins

%description
Using our software, you are able to view all of your encrypted and locked 
dvds without even noticing that someone tried real hard to keep you from 
doing so... finally dvd playback _REALLY_ comes to linux.

%description -l pl
U¿ywajac tej wtyczki mozna ogladac wszelkie, zakodowane plyty DVD.

%prep
sh %{_name}.txt
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_pluginsdir}/*

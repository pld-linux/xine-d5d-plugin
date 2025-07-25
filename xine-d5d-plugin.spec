%define		_name		xine-d5d
Summary:	DVD CSS input plugin for Xine
Summary(pl.UTF-8):	Wtyczka do odczytu DVD CSS dla Xine
Name:		%{_name}-plugin
Version:	0.2.7
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://debianlinux.net/%{_name}-%{version}.tgz
# Source0-md5:	dccb93df7c2dc09574d802bd19a1f7aa
Patch0:		%{_name}-plugin-configure.patch
Patch1:		%{_name}-plugin-api.patch
URL:		http://debianlinux.net/captain_css.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xine-lib-devel >= 0.9.13
%requires_eq	xine-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pluginsdir	%{_libdir}/xine/plugins

%description
Using our software, you are able to view all of your encrypted and locked
dvds without even noticing that someone tried real hard to keep you from
doing so... finally dvd playback _REALLY_ comes to linux.

%description -l pl.UTF-8
Używając tej wtyczki można oglądać wszelkie zakodowane płyty DVD.

%prep
%setup -q -n %{_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_pluginsdir}/*

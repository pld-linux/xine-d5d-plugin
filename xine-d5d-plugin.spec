%define		_name		d5d011
%define		_prgname	xine-d5d
Summary:	DVD CSS input plugin for Xine
Summary(pl):	Wtyczka do odczytu DVD CSS dla Xine
Name:		%{_prgname}-plugin
Version:	0.1.1
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://debianlinux.net/%{_name}.txt
Patch0:		%{name}-version.patch
URL:		http://debianlinux.net/captain_css.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xine-lib-devel >= 0.9.3
Requires:	xine-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pluginsdir	%{_libdir}/xine/plugins

%description
Using our software, you are able to view all of your encrypted and locked
dvds without even noticing that someone tried real hard to keep you from
doing so... finally dvd playback _REALLY_ comes to linux.

%description -l pl
U�ywaj�c tej wtyczki mo�na ogl�da� wszelkie zakodowane p�yty DVD.

%prep
%setup -T -c %{_prgname}-%{version}
sh %{SOURCE0}
tar xzf %{_prgname}-%{version}.tar.gz
%patch -p1

%build
cd %{_prgname}-%{version}
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd %{_prgname}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_prgname}-%{version}/README
%attr(755,root,root) %{_pluginsdir}/*

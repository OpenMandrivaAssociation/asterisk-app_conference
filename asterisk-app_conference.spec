%define		version 2.0.1
%define asterisk_version 1.6.1.2

Summary:	A channel-independent conference application for the Asterisk PBX
Name:		asterisk-app_conference
Version:	%{version}
Release:	%mkrel %{asterisk_version}.2
License:	GPL
Group:		System/Servers
URL:		https://sourceforge.net/projects/appconference/
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/appconference/appconference-%{version}.tar.gz
#Patch0:		app_conference-2.0.1-svnversion.diff
BuildRequires:	asterisk-devel = %{asterisk_version}, subversion
Requires:	asterisk = %{asterisk_version}
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
A channel-independent conference application for the Asterisk PBX.

%prep

%setup -q -n appconference-%{version}
#%patch0 -p1

find . -type f | xargs perl -pi -e "s|/usr/lib|%{_libdir}|g"

%build

%make ASTERISK_INCLUDE_DIR="%{includedir}" CFLAGS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_prefix}%{_libdir}/asterisk/modules
%makeinstall INSTALL_PREFIX="%{buildroot}"

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%attr(0755,root,root) %{_prefix}%{_libdir}/asterisk/modules/app_conference.so

%changelog
* Wed Feb 24 2009 Gergely Lonyai <aleph@mandriva.org> 2.0.1-1mdv2009.1
- 2.0.1

* Sun Feb 19 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.20051221.1mdk
- initial Mandriva package

%define snap 20051221

Summary:	A channel-independent conference application for the Asterisk PBX
Name:		asterisk-app_conference
Version:	0.0.1
Release:	%mkrel 0.%{snap}.1
License:	GPL
Group:		System/Servers
URL:		http://iaxclient.sourceforge.net/
Source0:	app_conference-%{version}-%{snap}.tar.bz2
Patch0:		app_conference-0.0.1-20051221-mdv_conf.diff
BuildRequires:	asterisk-devel
Requires:	asterisk
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
A channel-independent conference application for the Asterisk PBX.

%prep

%setup -q -n app_conference
%patch0 -p0

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%make CFLAGS="%{optflags} -pipe -Wall -fPIC -DPIC -D_REENTRANT -D_GNU_SOURCE"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/asterisk
install -m0755 app_conference.so %{buildroot}%{_libdir}/asterisk/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%attr(0755,root,root) %{_libdir}/asterisk/app_conference.so


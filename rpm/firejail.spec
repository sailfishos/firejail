Name: firejail
Version: 0.9.62
Release: 1
Summary: Linux namepaces sandbox program
License: GPLv2+
Source0: https://github.com/netblue30/firejail/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/netblue30/firejail

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%configure \
    --disable-x11 \
    --disable-overlayfs \
    --disable-contrib-install
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/bash-completion

%files
%license COPYING
%defattr(-,root,root,-)
%attr(4755, -, -) %{_bindir}/firejail
%{_bindir}/firecfg
%{_bindir}/firemon
%{_libdir}/firejail
%config %{_sysconfdir}/firejail

%files doc
%defattr(-,root,root,-)
%{_docdir}/firejail
%{_mandir}/man1/*
%{_mandir}/man5/*

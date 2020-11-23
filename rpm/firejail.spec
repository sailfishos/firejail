Name: firejail
Version: 0.9.63
Release: 1
Summary: Linux namepaces sandbox program
License: GPLv2+
Source0: %{name}-%{version}.tar.bz2
Patch1:  0001-Preserve-process-effective-group-for-privileged-grou.patch
Patch2:  0002-Fix-symlinks-that-go-though-proc-self.patch
Patch3:  0003-Add-utility-functions-for-handing-comma-separa.patch
Patch4:  0004-Allow-changing-protocol-list-after-initial-set.patch
Patch5:  0005-Add-missing-linefeeds-in-stderr-logging.patch
URL: https://github.com/netblue30/firejail

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%configure \
    --disable-man \
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

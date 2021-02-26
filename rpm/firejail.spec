Name: firejail
Version: 0.9.64.4
Release: 1
Summary: Linux namepaces sandbox program
License: GPLv2+
Source0: %{name}-%{version}.tar.bz2
# Upstreamed and will be in a future version
Patch1:  0001-Fix-symlinks-that-go-though-proc-self.patch
Patch2:  0002-fcopy-Fix-memory-leaks.patch
Patch3:  0003-sandbox-Do-not-leave-file-mounts-underneath-private-.patch
Patch4:  0004-Add-missing-linefeeds-in-stderr-logging.patch
Patch5:  0005-Add-checks-to-fs_private_dir_mount.patch
Patch6:  0006-Add-mkdir-and-mkfile-command-line-options-for-fireja.patch
Patch7:  0007-Add-utility-functions-for-handling-comma-separated-l.patch
Patch8:  0008-Allow-changing-protocol-list-after-initial-set.patch
# Sailfish OS patches
Patch9:  0009-Preserve-process-effective-group-for-privileged-grou.patch
Patch10: 0010-Implement-Sailfish-OS-specific-privileged-data-optio.patch

URL: https://github.com/sailfishos/firejail

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

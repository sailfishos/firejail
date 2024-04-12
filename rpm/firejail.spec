Name: firejail
Version: 0.9.72
Release: 1
Summary: Linux namepaces sandbox program
License: GPLv2+
Source0: %{name}-%{version}.tar.bz2
# Sailfish OS patches
Patch1: 0001-Preserve-process-effective-group-for-privileged-grou.patch
Patch2: 0002-Implement-Sailfish-OS-specific-privileged-data-optio.patch
Patch3: 0003-Add-profile-files-to-a-list-when-processing-argument.patch
Patch4: 0004-Implement-template-addition-for-replacing-keys-in-pr.patch
Patch5: 0005-Retain-symlink-chains.patch
Patch6: 0006-Add-xstat-tracing-and-optionally-log-only-failing-ca.patch
Patch7: 0007-Revert-deprecating-shell-3-5196.patch
Patch8: 0008-refactor-make-rundir-lock-variables-global.patch
Patch9: 0009-modif-improve-flock-handling.patch
Patch10: 0010-modif-populate-run-firejail-while-holding-flock.patch

URL: https://github.com/sailfishos/firejail

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces.

%package profiles
Summary: %{name} profiles
Requires: %{name} = %{version}-%{release}

%description profiles
%{summary} plus firecfg and jailcheck tools.

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
rm -rf %{buildroot}%{_datadir}/zsh/site-functions/_firejail

%files
%license COPYING
%defattr(-,root,root,-)
%attr(4755, -, -) %{_bindir}/%{name}
%{_bindir}/firemon
%exclude %{_sysconfdir}/%{name}/firecfg.config
%{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*.config
%{_sysconfdir}/%{name}/disable-*.inc
%{_sysconfdir}/%{name}/whitelist-*.inc

%files profiles
%{_bindir}/firecfg
%{_bindir}/jailcheck
%{_sysconfdir}/%{name}/firecfg.config
%exclude %{_sysconfdir}/%{name}/*.config
%exclude %{_sysconfdir}/%{name}/disable-*.inc
%exclude %{_sysconfdir}/%{name}/whitelist-*.inc
%{_sysconfdir}/%{name}

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}

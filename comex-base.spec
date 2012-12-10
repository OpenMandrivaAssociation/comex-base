Summary:   Base component for comex project
Name:      comex-base
Version:   0.1.8.5
Release:   %mkrel 1
License:   GPLv2
#ExcludeArch: ppc64
Group:     Office
Source0:   http://comex-project.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:   mono.snk
#Source1:   https://raw.github.com/mono/mono/master/mcs/class/mono.snk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL:       http://comex-project.googlecode.com/
BuildArch: noarch
# don't generate debug file because is empty
# % define debug_package %{nil}

BuildRequires: mono-devel
BuildRequires: log4net-devel
BuildRequires: pkgconfig

Requires: mono
Requires: log4net
Requires: pcsc-lite
Requires: libpcsclite1
# libpcsclite-devel required because contain /usr/lib/libpcsclite.so
# not contained in to libpcsclite1
#Requires: libpcsclite-devel


%description
Is base component of a simple application that can be used to exchange
data with smartcards using PC/SC standard readers or smartmouse
phoenix serial reader.

%package devel
Summary:	Base component for comex project
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	pkgconfig

%description devel
Is base component of a simple application that can be used to exchange
data with smartcards using PC/SC standard readers or smartmouse
phoenix serial reader.


%prep
%setup -q

%build
# Use the mono system key instead of generating our own here.
%if %mdvver >= 201100
  cp /etc/pki/mono/mono.snk comex-base/comex-base.snk
%else
  cp -f %{SOURCE1} comex-base/comex-base.snk
%endif
%configure2_5x --prefix=/usr --libdir=%_prefix/lib 
%make

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_datadir}/pkgconfig
%makeinstall_std linuxpkgconfigdir=%{_datadir}/pkgconfig
mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i %{buildroot}%{_prefix}/lib/%{name}/comex-base.dll \
        -f \
        -package %{name} \
        -root %{buildroot}%{_prefix}/lib/ \
        -gacdir %{buildroot}%{_prefix}/lib/mono/gac



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl comex-base/Docs/readme
%_prefix/lib/mono/gac/comex-base/
%_prefix/lib/mono/comex-base
%_prefix/lib/%{name}/
%{_datadir}/%{name}/

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc



%changelog
* Sun Oct 30 2011 Armando Basile <hman@mandriva.org> 0.1.8.5-1
+ Revision: 707871
- release 0.1.8.5
- removed changelog section from spec file

* Tue Oct 04 2011 Armando Basile <hman@mandriva.org> 0.1.8.4-1
+ Revision: 702867
- added tarball
- release 0.1.8.4

* Fri Sep 23 2011 Armando Basile <hman@mandriva.org> 0.1.7.3-1
+ Revision: 701155
- import comex-base


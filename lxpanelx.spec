# This spec-file is the one from Fedora lxpanel-0.5.8-1.src.rpm package with minor corrections. 

%global	svnrev 146

Name:           lxpanelx
Version:        0.5.6
Release:        1.svn%{svnrev}
Summary:        Fork of lxpanel - a lightweight X11 desktop panel with improved taskbar.

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://lxpanelx.googlecode.com/svn/trunk
# See get_sources script.
Source0:        lxpanelx-%{version}-svn%{svnrev}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=564746
Patch0:         lxpanel-0.5.5-dsofix.patch
# distro specific patches
Patch100:       lxpanel-0.5.4-default.patch
Patch101:       lxpanel-0.3.8.1-nm-connection-editor.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides:	lxpanel

#BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  gtk2-devel 
BuildRequires:  intltool
BuildRequires:  libXpm-devel
BuildRequires:  startup-notification-devel
# required for alsa mixer plugin
BuildRequires:  alsa-lib-devel
# required for netstatus plugin
BuildRequires:  wireless-tools-devel
BuildRequires:  menu-cache-devel >= 0.3.0

%description
lxpanelx is forx of lxpanel, a lightweight X11 desktop panel. It works with any ICCCM / NETWM compliant window manager (eg sawfish, metacity, xfwm4, kwin) and features a tasklist, pager, launchbar, clock, menu and sytray. Fork provides the improved tasklist with manual or auto windows grouping.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel 
Requires:       libXpm-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}-svn%{svnrev}
%patch0 -p1 -b .dsofix

%patch100 -p1 -b .default
%patch101 -p1 -b .system-config-network

#ugly hack to build the current trunk version
touch -c Makefile.in

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang lxpanel

%clean
rm -rf $RPM_BUILD_ROOT


%files -f lxpanel.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/lxpanel*
%{_datadir}/lxpanel/
%{_libdir}/lxpanel/
%{_mandir}/man1/lxpanel*

%files devel
%defattr(-,root,root,-)
%{_includedir}/lxpanel/
%{_libdir}/pkgconfig/lxpanel.pc

%changelog
* Fri Nov 11 2011 Aleksandra Bookwar <alpha@bookwar.info> - 0.5.6-1.svn146
- Initial build of lxpanelx fork

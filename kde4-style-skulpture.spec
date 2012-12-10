%define shortname skulpture

Name: kde4-style-%{shortname} 
Summary: Skulpture Theme for KDE4
Version: 0.2.3
Release: %mkrel 2
Source0: http://www.kde-look.org/CONTENT/content-files/59031-%{shortname}-%{version}.tar.bz2
Patch0: skulpture-0.1.3-kdeplugin-cmake.patch
Patch1: kde4-style-skulpture-kwin.patch
URL: http://www.kde-look.org/content/show.php/Skulpture?content=59031
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL 
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel

%description
Skulpture theme for KDE 4

%files 
%{_kde_libdir}/kde4/kstyle_skulpture_config.so
%{_kde_libdir}/kde4/kwin3_skulpture.so
%{_kde_libdir}/kde4/kwin_skulpture_config.so
%{_kde_appsdir}/color-schemes/
%{_kde_appsdir}/kstyle/themes/
%{_kde_appsdir}/kwin/
%{_kde_appsdir}/skulpture
%{_kde_plugindir}/styles/*

#--------------------------------------------------------------------------------

%prep 
%setup -q -n %shortname-%version
%patch0 -p1
%patch1 -p1 -b .kwin

%build 
%cmake_kde4 
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
popd

%clean 
rm -rf $RPM_BUILD_ROOT 




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2011.0
+ Revision: 619954
- the mass rebuild of 2010.0 packages

* Mon Jul 06 2009 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.2.3-1mdv2010.0
+ Revision: 392971
- New version 0.2.3
- Added patch to fix a KWin crash

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 0.2.2-2mdv2009.1
+ Revision: 336449
- New version 0.2.2

* Mon Dec 01 2008 Leonardo de Amaral Vidal <leonardoav@mandriva.com> 0.2.0-1mdv2009.1
+ Revision: 308843
- New version 0.2.0

* Fri Jul 04 2008 Helio Chissini de Castro <helio@mandriva.com> 0.1.3-3mdv2009.0
+ Revision: 231721
- Patch for install in proper kde4 plugindir

* Fri Jul 04 2008 Funda Wang <fwang@mandriva.org> 0.1.3-2mdv2009.0
+ Revision: 231544
- fix url

* Thu Jul 03 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.1.3-1mdv2009.0
+ Revision: 231217
- Using qt4plugins macro instead of qt4dir.
- Upgraded to version 0.1.3.
- Updated the correct install dir or libskulpture.so.
- Removed kwin_qtcurve_config.so commented line.

* Fri May 16 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.1.2-1mdv2009.0
+ Revision: 208122
- import kde4-style-skulpture



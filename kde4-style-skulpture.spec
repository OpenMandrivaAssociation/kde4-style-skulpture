%define shortname skulpture

Name: kde4-style-%{shortname} 
Summary: Skulpture Theme for KDE4
Version: 0.2.3
Release: %mkrel 1
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



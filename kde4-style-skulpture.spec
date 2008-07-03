%define shortname skulpture

Name: kde4-style-%{shortname} 
Summary: Skulpture Theme for KDE4
Version: 0.1.3
Release: %mkrel 1
Source0: %{shortname}-%{version}.tar.bz2
URL: http://www.kde-look.org
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL 
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel

%description
Skulpture theme for KDE 4

%prep 
%setup -q -n %shortname-%version

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

%files 
%{_kde_libdir}/kde4/kstyle_skulpture_config.so
%{_kde_libdir}/kde4/kwin3_skulpture.so
%{_kde_libdir}/kde4/kwin_skulpture_config.so
%{qt4dir}/plugins/styles/libskulpture.so
%{_kde_appsdir}/color-schemes/
%{_kde_appsdir}/kstyle/themes/
%{_kde_appsdir}/kwin/


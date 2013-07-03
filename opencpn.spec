%define		oname	OpenCPN

Name:		opencpn
Summary:	A concise ChartPlotter/Navigator
Version:	3.0.2
Release:	2
License:	GPLv2+
Group:		Sciences/Geosciences
URL:		http://opencpn.org
Source0:	http://prdownloads.sourceforge.net/project/opencpn/%{name}/%{version}/%{oname}-%{version}-Source.tar.gz
Source1:	opencpn.rpmlintrc
BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	gpsd-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	mesa-common-devel
BuildRequires:	wxgtku-devel
BuildRequires:	zlib-devel
# Building with TinyXML from repositories causes segfault at start
BuildConflicts:	tinyxml-devel

%description
A cross-platform ship-borne GUI application supporting

* GPS/GPDS Postition Input
* BSB Raster Chart Display
* S57 Vector ENChart Display
* AIS Input Decoding
* Waypoint Autopilot Navigation

Pilot charts can be downloaded from http://opencpn.org/ocpn/downloadpilotcharts

%prep
%setup -q -n %{oname}-%{version}-Source

%build
cmake	. \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DCMAKE_BUILD_TYPE=release \
	-DCMAKE_SKIP_RPATH:BOOL=ON
%make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README
%{_bindir}/*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*


%changelog
* Wed Jul 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.2-1
+ Revision: 810119
- version update 3.0.2

* Sun Jan 15 2012 Andrey Bondrov <abondrov@mandriva.org> 2.5.0-1
+ Revision: 760900
- New version 2.5.0, switch to utf8 version of wxGTK2.8

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-2mdv2011.0
+ Revision: 613533
- rebuild

* Sun Feb 07 2010 Funda Wang <fwang@mandriva.org> 1.3.6-1mdv2010.1
+ Revision: 501636
- fix summary
- import opencpn


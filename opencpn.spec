%define		oname	OpenCPN

Name:		opencpn
Summary:	OpenCPN: A concise ChartPlotter/Navigator
Version:	3.0.2
Release:	1
License:	GPLv2+
Group:		Sciences/Geosciences
URL:		http://opencpn.org
Source0:	http://prdownloads.sourceforge.net/project/opencpn/%{name}/%{version}/%{oname}-%{version}-Source.tar.gz
BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	gpsd-devel
BuildRequires:	gtk+2-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
Buildrequires:	wxgtku-devel
Buildrequires:	zlib-devel
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

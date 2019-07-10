%define _disable_ld_no_undefined 1
%define _disable_lto 1
%global __requires_exclude ^lib(S57ENC|GARMINHOST|TEXCMP|NMEA0183)\\.so.*$

%define		oname	OpenCPN

Name:		opencpn
Summary:	A concise ChartPlotter/Navigator
Version:	5.0.0
Release:	1
License:	GPLv2+
Group:		Sciences/Geosciences
URL:		http://opencpn.org
Source0:	https://github.com/%{oname}/%{oname}/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	opencpn.rpmlintrc
Patch10:	opencpn-5.0.0-link_wxgtk.patch

BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	gpsd-devel
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	mesa-common-devel
#BuildRequires:	wxgtku-devel
BuildRequires:	zlib-devel
BuildRequires:	gettext
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgps)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	wxgtku3.0-devel
# Building with TinyXML from repositories causes segfault at start
BuildRequires:	tinyxml-devel

Requires:	gpsd-clients


%description
A cross-platform ship-borne GUI application supporting

* GPS/GPDS Postition Input
* BSB Raster Chart Display
* S57 Vector ENChart Display
* AIS Input Decoding
* Waypoint Autopilot Navigation

Pilot charts can be downloaded from http://opencpn.org/ocpn/downloadpilotcharts

%prep
%setup -q -n %{oname}-%{version}
%autopatch -p1

rm -rf plugins/chartdldr_pi

# Be sure to use system tinyxml headers and not bundled ones
rm -f src/tinyxml*.cpp include/tinyxml.h

%build
%cmake	-DBUNDLE_DOCS=ON \
	-DBUNDLE_TCDATA=ON \
	-DBUNDLE_GSHHS=CRUDE \
	-DBUILD_SHARED_LIBS=OFF
%make_build

%install
%make_install -C build

%find_lang %{name}
%find_lang %{name}-grib_pi
%find_lang %{name}-dashboard_pi
%find_lang %{name}-wmm_pi

desktop-file-install  \
 --dir=%{buildroot}%{_datadir}/applications \
 --remove-category='Science' \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

cp -f data/license.txt %{buildroot}%{_datadir}/%{name}/doc
cp -f data/doc/help_en_US.html %{buildroot}%{_datadir}/%{name}/doc

# Remove Debian-only docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files -f %{name}.lang -f %{name}-dashboard_pi.lang -f %{name}-grib_pi.lang -f %{name}-wmm_pi.lang
%doc README
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/opencpn.1.xz


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


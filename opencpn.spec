Name: opencpn
Summary: OpenCPN: A concise ChartPlotter/Navigator.
Version: 1.3.6
Release: %mkrel 1
License: GPLv2+
Group: Sciences/Geosciences
Source0: http://prdownloads.sourceforge.net/project/opencpn/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:	opencpn-1.3.6-locale-install.patch
Patch1: opencpn-1.3.6-glib-2.21.patch
URL: http://sourceforge.net/projects/opencpn/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel 
BuildRequires: wxGTK2.8-devel
Buildrequires: imagemagick

%description
A cross-platform ship-borne GUI application supporting

* GPS/GPDS Postition Input
* BSB Raster Chart Display 
* S57 Vector ENChart Display 
* AIS Input Decoding 
* Waypoint Autopilot Navigation

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p0 

%build
autoreconf -fi
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std

# install and resize icons
#mkdir -p %buildroot{%_iconsdir}
mkdir -p %buildroot%{_liconsdir}
mkdir -p %buildroot%{_miconsdir}
#install -dm 755 %buildroot%{_liconsdir}/%{name}.png 
#install -dm 755 %buildroot%{_miconsdir}/%{name}.png 
cp %buildroot%{_iconsdir}/%{name}.png %buildroot%{_liconsdir}/%{name}.png
cp %buildroot%{_iconsdir}/%{name}.png %buildroot%{_miconsdir}/%{name}.png
convert %buildroot%{_liconsdir}/%{name}.png -resize 48x48 %buildroot%{_liconsdir}/%{name}.png 
convert %buildroot%{_miconsdir}/%{name}.png -resize 16x16 %buildroot%{_miconsdir}/%{name}.png 
convert %buildroot%{_iconsdir}/%{name}.png -resize 32x32 %buildroot%{_iconsdir}/%{name}.png

%find_lang %name --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang 
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING ChangeLog
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

Name: x11-driver-video-chips
Version: 1.1.1
Release: %mkrel 4
Summary: The X.org driver for Chips and Technologies
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-chips-%{version}.tar.bz2
# Default to SWcursor on CT65550 as hardware cursor is reported broken on this chip
Patch0: x11-driver-video-chips-CT65550-swcursor.patch 
# Disable 2D acceleration on C&T 69000 by default, since it is reported to be broken
Patch1: x11-driver-video-chips-CT69000-noaccel.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Chips and Technologies boards

%prep
%setup -q -n xf86-video-chips-%{version}
%patch0 -p1 -b .chips-CT65550-swcursor 
%patch1 -p1 -b .chips-CT69000-noaccel

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/chips_drv.la
%{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.*

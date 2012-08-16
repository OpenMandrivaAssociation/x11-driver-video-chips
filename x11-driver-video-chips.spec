Name: x11-driver-video-chips
Version: 1.2.5
Release: 1
Summary: X.org driver for Chips and Technologies
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-chips-%{version}.tar.bz2
Patch1: 0001-Import-existing-patches-that-were-originally-Red-Ha.patch
Patch2: x11-driver-video-chips-1.2.5-debian-iopl_h.patch

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-chips is the X.org driver for Chips and Technologies boards.

%prep
%setup -qn xf86-video-chips-%{version}
%patch1 -p1
%patch2 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.*

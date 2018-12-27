%define _disable_ld_no_undefined 1

Summary:	X.org driver for Chips and Technologies
Name:		x11-driver-video-chips
Version:	1.3.0
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-chips-%{version}.tar.bz2
Patch1:		0001-Import-existing-patches-that-were-originally-Red-Ha.patch
Patch2:		x11-driver-video-chips-1.2.5-debian-iopl_h.patch
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-chips is the X.org driver for Chips and Technologies boards.

%prep
%setup -qn xf86-video-chips-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.*

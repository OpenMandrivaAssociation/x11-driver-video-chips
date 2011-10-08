Name: x11-driver-video-chips
Version: 1.2.4
Release: %mkrel 4
Summary: X.org driver for Chips and Technologies
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-chips-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Patch1: 0001-Import-existing-patches-that-were-originally-Red-Ha.patch

%description
x11-driver-video-chips is the X.org driver for Chips and Technologies boards.

%prep
%setup -q -n xf86-video-chips-%{version}

%patch1 -p1

%build
%configure2_5x
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

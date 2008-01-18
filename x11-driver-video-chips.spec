%define debug_package	%{nil}

Name: x11-driver-video-chips
Version: 1.1.1
Release: %mkrel 6
Summary: The X.org driver for Chips and Technologies
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-input-chips-1.1.1@mandriva suggested on upstream
# Tag at git checkout d449ee092bbc8b4e08371b8067f1d8e320c4297e
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-chips  xorg/drivers/xf86-video-chips
# cd xorg/drivers/xf86-video/chips
# git-archive --format=tar --prefix=xf86-video-chips-1.1.1/ xf86-input-chips-1.1.1@mandriva | bzip2 -9 > xf86-video-chips-1.1.1.tar.bz2
########################################################################
Source0: xf86-video-chips-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-chips-1.1.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Import-existing-patches-that-were-originally-Red-Ha.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Chips and Technologies boards

%prep
%setup -q -n xf86-video-chips-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.*

Name: x11-driver-video-chips
Version: 1.2.5
Release: 2
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


%changelog
* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.4-5
+ Revision: 748386
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.4-4
+ Revision: 703683
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.4-3
+ Revision: 683562
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-2
+ Revision: 671142
- mass rebuild

* Mon Feb 28 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.4-1
+ Revision: 640988
- New version: 1.2.4

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.3-3mdv2011.0
+ Revision: 595739
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Jul 26 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.3-1mdv2011.0
+ Revision: 560878
- New version: 1.2.3

* Thu Aug 20 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-1mdv2010.0
+ Revision: 418375
- new release

* Tue Aug 11 2009 Funda Wang <fwang@mandriva.org> 1.2.1-2mdv2010.0
+ Revision: 414548
- use configure2_5x

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.1-1mdv2009.1
+ Revision: 317846
- New version 1.2.1

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 308213
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265905
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194213
- Update to version 1.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-8mdv2008.1
+ Revision: 165523
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-7mdv2008.1
+ Revision: 156600
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-6mdv2008.1
+ Revision: 154879
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-input-chips-1.1.1@mandriva suggested on upstream
  Tag at git checkout d449ee092bbc8b4e08371b8067f1d8e320c4297e, that is
  a few harmless commits (adding .csvignore, .gitignore, etc) commits after
  the chips-1_1_1 existing tag.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-5mdv2008.1
+ Revision: 98687
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdv2008.0
+ Revision: 75755
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Fri Jun 02 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-02 19:21:24 (31881)
- Default to SWcursor on CT65550 as hardware cursor is reported broken on this chip
- Disable 2D acceleration on C&T 69000 by default, since it is reported to be broken
- Remove old tarball

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository


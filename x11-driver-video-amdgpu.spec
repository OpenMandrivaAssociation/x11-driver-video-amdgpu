Summary:	X.org driver for AMD Technologies
Name:		x11-driver-video-amdgpu
Version:	19.0.1
Release:	3
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-amdgpu-%{version}.tar.bz2
# ( crazy ) See: fdo bug 111122 & 111244
Source1:    amdgpu-mesa.sh
# upstream patches
Patch0:   Retry-get_fb_ptr-in-get_fb.patch
Patch1:   dri3-Always-flush-glamor-before-sharing-pixmap-stora.patch
# ( crazy ) See: fdo bug 111122 & 111244
# This may be removed for mesa 19.3.x++ and kernel 5.4++
# I do have HW hits all these bugs so I can test once newer sw is released
Patch2:   revert-a2b32e72fdaff3007a79b84929997d8176c2d512.patch

BuildRequires:	pkgconfig(libdrm) >= 2.4.65
BuildRequires:	pkgconfig(libdrm_amdgpu) >= 2.4.65
BuildRequires:	pkgconfig(xorg-macros) >= 1.19
BuildRequires:	pkgconfig(xextproto) >= 7.3.0
BuildRequires:	pkgconfig(xorg-server) >= 1.19.6
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	x11-proto-devel >= 7.7
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
# (tpg) this is needed to get VDPAU works out of box
Requires:	%{_lib}vdpau-driver-radeonsi
Requires:	%{_lib}dri-drivers-radeon

%description
x11-driver-video-amdgpu is the X.org driver for AMD Technologies.

%prep
%setup -qn xf86-video-amdgpu-%{version}
[ -e autogen.sh ] && ./autogen.sh || :
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -D -m755 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/

%files
%{_sysconfdir}/profile.d/*
%{_libdir}/xorg/modules/drivers/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4.*

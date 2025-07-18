%define _disable_ld_no_undefined 1
Summary:	X.org driver for AMD Technologies
Name:		x11-driver-video-amdgpu
Version:	23.0.1~20250620
Release:	1
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	https://github.com/X11Libre/xf86-video-amdgpu/archive/refs/heads/master.tar.gz#/xf86-video-amdgpu-%{version}.tar.gz
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
%autosetup -n xf86-video-amdgpu-master -p1
[ -e autogen.sh ] && ./autogen.sh || :

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%doc %{_mandir}/man4/amdgpu.4.*

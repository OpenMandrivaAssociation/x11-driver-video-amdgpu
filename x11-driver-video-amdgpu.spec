%define _disable_ld_no_undefined 1
%define abi 25
Summary:	xlibre driver for AMD Technologies
Name:		x11-driver-video-amdgpu
Version:	25.1.0
Release:	1
Group:		System/X11
License:	MIT
URL:		https://github.com/X11Libre
Source0:	https://github.com/X11Libre/xf86-video-amdgpu/archive/refs/tags/xlibre-xf86-video-amdgpu-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(libdrm) >= 2.4.65
BuildRequires:	pkgconfig(libdrm_amdgpu) >= 2.4.65
BuildRequires:	pkgconfig(xorg-macros) >= 1.19
BuildRequires:	pkgconfig(xextproto) >= 7.3.0
BuildRequires:	pkgconfig(xorg-server) >= 1.19.6
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	x11-proto-devel >= 7.7
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Requires:	%{_lib}dri-drivers

%description
x11-driver-video-amdgpu is the xlibre driver for AMD Technologies.

%prep
%autosetup -n xf86-video-amdgpu-xlibre-xf86-video-amdgpu-%{version} -p1
[ -e autogen.sh ] && ./autogen.sh || :

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/xlibre-%{abi}/drivers/video/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%doc %{_mandir}/man4/amdgpu.4.*

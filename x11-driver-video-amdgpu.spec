Summary:	X.org driver for AMD Technologies
Name:		x11-driver-video-amdgpu
Version:	1.0.0
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-amdgpu-%{version}.tar.bz2
BuildRequires:	pkgconfig(libdrm) >= 2.4.65
BuildRequires:	pkgconfig(libdrm_amdgpu) >= 2.4.65
BuildRequires:	pkgconfig(xorg-macros) >= 1.19
BuildRequires:	pkgconfig(xextproto) >= 7.3.0
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(gbm)
BuildRequires:	x11-proto-devel >= 7.7
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
# (tpg) this is needed to get VDPAU works out of box
Requires:	%{_lib}vdpau-driver-radeonsi
Requires:	%{_lib}dri-drivers-radeon

%description
x11-driver-video-amdgpu is the X.org driver for AMD Technologies.

%prep
%setup -qn xf86-video-amdgpu-%{version}

%build
%configure
%make

%install
%makeinstall_std

%files

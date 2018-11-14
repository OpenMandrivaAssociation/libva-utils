%define major 2
%define libname %mklibname va %{major}
%define devname %mklibname va -d
%bcond_without utils

Summary:	Tools for libva (including vainfo)
Name:		libva-utils
Version:	2.3.0
Release:	1
Group:		System/Libraries
License:	MIT
Url:		http://freedesktop.org/wiki/Software/vaapi
Source0:	https://github.com/intel/libva-utils/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libva) >= %{version}
BuildRequires:	pkgconfig(libva-drm) >= %{version}
BuildRequires:	pkgconfig(libva-x11) >= %{version}
BuildRequires:	pkgconfig(libva-wayland) >= %{version}
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(wayland-client)

%description
The %{name} package contains tools that are provided as part
of libva, including the vainfo tool for determining what (if any)
libva support is available on a system.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/avcenc
%{_bindir}/jpegenc
%{_bindir}/mpeg2vaenc
%{_bindir}/h264encode
%{_bindir}/loadjpeg
%{_bindir}/mpeg2vldemo
%{_bindir}/putsurface*
%{_bindir}/vainfo
%{_bindir}/vavpp
%{_bindir}/vp9enc

%define major 2
%define libname %mklibname va %{major}
%define devname %mklibname va -d
%define va_version 1.11.0

Summary:	Tools for libva (including vainfo)
Name:		libva-utils
Version:	2.22.0
Release:	1
Group:		System/Libraries
License:	MIT
Url:		https://freedesktop.org/wiki/Software/vaapi
Source0:	https://github.com/intel/libva-utils/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libva) >= %{va_version}
BuildRequires:	pkgconfig(libva-drm) >= %{va_version}
BuildRequires:	pkgconfig(libva-x11) >= %{va_version}
BuildRequires:	pkgconfig(libva-wayland) >= %{va_version}
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	meson

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
%{_bindir}/av1encode
%{_bindir}/avcenc
%{_bindir}/avcstreamoutdemo
%{_bindir}/hevcencode
%{_bindir}/h264encode
%{_bindir}/jpegenc
%{_bindir}/mpeg2vaenc
%{_bindir}/loadjpeg
%{_bindir}/mpeg2vldemo
%{_bindir}/putsurface*
%{_bindir}/sfcsample
%{_bindir}/vacopy
%{_bindir}/vainfo
%{_bindir}/vavpp
%{_bindir}/vpp3dlut
%{_bindir}/vpphdr_tm
%{_bindir}/vppblending
%{_bindir}/vppchromasitting
%{_bindir}/vppdenoise
%{_bindir}/vppscaling_csc
%{_bindir}/vppscaling_n_out_usrptr
%{_bindir}/vppsharpness
%{_bindir}/vp8enc
%{_bindir}/vp9enc

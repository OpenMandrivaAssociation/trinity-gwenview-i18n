%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg gwenview-i18n
%define tde_prefix /opt/trinity
%define tde_appdir %{tde_datadir}/applications
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		1.4.2
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Internationalization support for Gwenview [Trinity]
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

BuildArch:	noarch

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/graphics/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DBIN_INSTALL_DIR="%{tde_bindir}"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DBUILD_ALL=ON -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig


%description
Gwenview is a fast and easy to use image viewer/browser for TDE.
All common image formats are supported, such as PNG(including transparency),
JPEG(including EXIF tags and lossless transformations), GIF, XCF (Gimp
image format), BMP, XPM and others. Standard features include slideshow,
fullscreen view, image thumbnails, drag'n'drop, image zoom, full network
transparency using the KIO framework, including basic file operations and
browsing in compressed archives, non-blocking GUI with adjustable views.
Gwenview also provides image and directory KParts components for use e.g. in
Konqueror. Additional features, such as image renaming, comparing,
converting, and batch processing, HTML gallery and others are provided by the
KIPI image framework.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"


%install -a
## File lists
%find_lang gwenview


%files -f gwenview.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%lang(da) %{tde_tdedocdir}/HTML/da/gwenview/
%lang(de) %{tde_tdedocdir}/HTML/de/gwenview/
%lang(et) %{tde_tdedocdir}/HTML/et/gwenview/
%lang(fr) %{tde_tdedocdir}/HTML/fr/gwenview/
%lang(it) %{tde_tdedocdir}/HTML/it/gwenview/
%lang(nl) %{tde_tdedocdir}/HTML/nl/gwenview/
%lang(pl) %{tde_tdedocdir}/HTML/pl/gwenview/
%lang(pt) %{tde_tdedocdir}/HTML/pt/gwenview/
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/gwenview/
%lang(ru) %{tde_tdedocdir}/HTML/ru/gwenview/
%lang(sv) %{tde_tdedocdir}/HTML/sv/gwenview/


Summary: Libraries for NetCDF
Name: netcdf
Version: 4.4.1.1
Release: 1%{?dist}
License: BSD-like
Group: Development/Libraries
URL: http://www.unidata.ucar.edu/software/netcdf/

Source: ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: libcurl-devel
BuildRequires: make

%description
The Unidata network Common Data Form (netCDF) is an interface for
scientific data access and a freely-distributed software library that
provides an implementation of the interface.  The netCDF library also
defines a machine-independent format for representing scientific data.
Together, the interface, library, and format support the creation,
access, and sharing of scientific data.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
# need to package HDF5 library before we can enable netcdf-4 features
%configure \
    --disable-netcdf-4 \
    --enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__rm} -f %{buildroot}%{_infodir}/dir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/nccopy
%{_bindir}/ncdump
%{_bindir}/ncgen
%{_bindir}/ncgen3
%{_libdir}/libnetcdf.so.*

%files devel
%{_bindir}/nc-config
%{_includedir}/netcdf*
%{_libdir}/libnetcdf.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
%changelog
* Tue Jan 10 2017 Daniel Berry <dberry@boundlessgeo.com> - 4.4.1.1-1
- Updated to release 4.4.1.1.

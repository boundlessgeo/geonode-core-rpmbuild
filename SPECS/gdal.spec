Summary: Geospatial Data Abstraction Library
Name: gdal
Version: 2.1.2
Release: 1%{?dist}
License: MIT/X
Group: Applications/Engineering
URL: http://www.gdal.org/

%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
Source0: http://download.osgeo.org/gdal/gdal-%{version}.tar.gz
%if 0%{?rhel} == 6
Source1: MrSID_DSDK-9.5.1.4427-linux.x86-64.gcc44.tar.gz
%else if 0%{?rhel} == 7
Source1: MrSID_DSDK-9.5.1.4427-linux.x86-64.gcc48.tar.gz
%endif
BuildRequires: gcc
BuildRequires: geos-devel >= 3.3.3
BuildRequires: proj-devel
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: sqlite-devel
BuildRequires: libkml-devel
BuildRequires: openjpeg2-devel
BuildRequires: postgresql96-devel
BuildRequires: poppler-devel
BuildRequires: xerces-c-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: ant
BuildRequires: chrpath
BuildRequires: libtool
BuildRequires: hdf5-devel
BuildRequires: netcdf-devel
%{?el6:BuildRequires: swig}
%{?el6:BuildRequires: python27-devel}
%{?el7:BuildRequires: python-devel}
%{?el7:BuildRequires: swig = 1.3.40}

Requires: geos >= 3.3.3
%{?el6:Requires: swig}
%{?el7:Requires: swig = 1.3.40}
Requires: proj
Requires: poppler
Requires: postgresql96-libs
Requires: expat
Requires: curl
Requires: sqlite
Requires: xerces-c
Requires: libkml
Requires: openjpeg2
Requires: hdf5
Requires: netcdf
Requires: proj-devel

Patch0: gdal_driverpath.patch
Patch1: gdal_GDALmake.opt.in.patch

%description
The Geospatial Data Abstraction Library (GDAL) is a unifying C/C++ API for
accessing raster geospatial data, and currently includes formats like
GeoTIFF, Erdas Imagine, Arc/Info Binary, CEOS, DTED, GXF, and SDTS. It is
intended to provide efficient access, suitable for use in viewer
applications, and also attempts to preserve coordinate systems and
metadata. Perl, C, and C++ interfaces are available.

# gdal-devel
%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%package python
Summary: Python bindings for gdal and ogr
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%{?el6:Requires: python27}
%{?el7:Requires: python}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%description python
This package contains Python bindings for GDAL/OGR library.

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h

%prep
%setup
%ifarch x86_64
# In RedHat land, 32-bit libs go in /usr/lib and 64-bit ones go in /usr/lib64.
# The default driver search paths need changing to reflect this.
%patch0
%endif
%patch1

%build

sed -i 's|@LIBTOOL@|%{_bindir}/libtool|g' GDALmake.opt.in
tar -xf %{SOURCE1} -C .

# copying mrsid and mrsid_lidar lib and include to /usr/local because build fails if we point at location within the build directory
mrsid_name=$(basename %{SOURCE1} .tar.gz)
mkdir -p %{buildroot}/usr/local/{include,lib}
/bin/cp -rf %{_builddir}/%{name}-%{version}/$mrsid_name/Lidar_DSDK/lib/* %{buildroot}/usr/local/lib
/bin/cp -rf %{_builddir}/%{name}-%{version}/$mrsid_name/Lidar_DSDK/include/* %{buildroot}/usr/local/include
/bin/cp -rf %{_builddir}/%{name}-%{version}/$mrsid_name/Raster_DSDK/lib/* %{buildroot}/usr/local/lib
/bin/cp -rf %{_builddir}/%{name}-%{version}/$mrsid_name/Raster_DSDK/include/* %{buildroot}/usr/local/include

export LD_LIBRARY_PATH=%{buildroot}/usr/local/lib:$LD_LIBRARY_PATH

%if 0%{?rhel} == 6
%configure --datadir=/usr/share/gdal --disable-static --with-pg=/usr/pgsql-9.6/bin/pg_config --disable-rpath --with-poppler --with-mrsid=%{buildroot}/usr/local  --with-mrsid_lidar=%{buildroot}/usr/local --with-spatialite --with-curl --with-expat --with-python=/usr/local/bin/python2.7 --with-java --with-hdf5 --with-netcdf
%else if 0%{?rhel} == 7
%configure --datadir=/usr/share/gdal --disable-static --with-pg=/usr/pgsql-9.6/bin/pg_config --disable-rpath --with-poppler --with-mrsid=%{buildroot}/usr/local  --with-mrsid_lidar=%{buildroot}/usr/local --with-spatialite --with-curl --with-expat --with-python --with-java --with-hdf5 --with-netcdf
%endif

make
make %{?_smp_mflags}

# Java SWIG bindings
cd swig/java
sed -i '1iJAVA_HOME=/usr/lib/jvm/java-openjdk' java.opt
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%ifarch x86_64 # 32-bit libs go in /usr/lib while 64-bit libs go in /usr/lib64
%define lib_dir /usr/lib64
%else
%define lib_dir /usr/lib
%endif
mkdir -p %{buildroot}/%{lib_dir}/gdalplugins
mrsid_name=$(basename %{SOURCE1} .tar.gz)
cp $mrsid_name/Raster_DSDK/lib/libltidsdk.so* %{buildroot}/%{lib_dir}
cp $mrsid_name/Lidar_DSDK/lib/liblti_lidar_dsdk.so* %{buildroot}/%{lib_dir}
cp $mrsid_name/Lidar_DSDK/lib/liblaslib.so %{buildroot}/%{lib_dir}
# Remove RPATHs
chrpath -d swig/java/*.so
cp swig/java/*.so %{buildroot}%{lib_dir}
cp swig/java/gdal.jar %{buildroot}%{lib_dir}/gdal-%{version}.jar

# Grep reports BUILDROOT inside our object files; disable that test.
QA_SKIP_BUILD_ROOT=1
export QA_SKIP_BUILD_ROOT

%if 0%{?rhel} == 6
mkdir -p %{buildroot}/usr/local/lib
mv %{buildroot}/usr/lib/python2.7 %{buildroot}/usr/local/lib
find %{buildroot}%{_bindir} -type f -name '*.py' -exec sed -i 's_bin/env python.*_bin/env python2.7_' {} +
%endif

%clean
rm -rf %{buildroot}
rm -f /usr/local/lib/{libgeos*,libltidsdk*,libtbb*,liblti_lidar_dsdk*,liblaslib.so} && rm -f /usr/local/include/*.h && rm -rf /usr/local/include/{lidar,nitf}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/gdal/
%{_libdir}/lib*
%{_libdir}/gdal-%{version}.jar
%{_libdir}/pkgconfig/gdal.pc

%files python
%defattr(-,root,root,-)
%if 0%{?rhel} == 6
/usr/local/lib/python2.7
%else if 0%{?rhel} == 7
%{python_sitearch}
%endif

%{_bindir}/*.py

%changelog
* Sat Nov 12 2016 amirahav <arahav@boundlessgeo.com> [2.1.2-1]
- Bump to 2.1.2 and Postgres 9.6
* Thu Nov 03 2016 BerryDaniel <dberry@boundlessgeo.com> [2.0.3-1]
- Updated to 2.0.3

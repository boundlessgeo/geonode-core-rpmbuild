#!/bin/bash
TODO: just download all sources
echo 'downloading sources'
echo '-------------------'

version=`rpm -qa \*-release | grep -Ei "redhat|centos" | cut -d"-" -f3`

pushd erlang; wget https://github.com/erlang/otp/archive/OTP-18.3.4.4.tar.gz; popd
pushd libkml; wget https://github.com/google/libkml/archive/release-1.2.tar.gz; popd
pushd openjpeg2; wget https://github.com/uclouvain/openjpeg/archive/v2.1.2.tar.gz; popd
pushd gdal; wget http://download.osgeo.org/gdal/2.1.2/gdal-2.1.2.tar.gz; popd
pushd tomcat8; wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.5.9/bin/apache-tomcat-8.5.9.tar.gz; popd
pushd postgis; wget http://download.osgeo.org/postgis/source/postgis-2.3.1.tar.gz; popd
pushd hdf5; wget http://hdf4.org/ftp/HDF5/current18/src/hdf5-1.8.18.tar.gz; popd
pushd netcdf; wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz; popd
pushd socat; wget http://www.dest-unreach.org/socat/download/socat-1.7.2.4.tar.bz2; popd
if [ $version == 7 ];then
  pushd gdal; wget https://s3.amazonaws.com/yum-geonode.boundlessps.com/src/MrSID_DSDK-9.5.1.4427-linux.x86-64.gcc48.tar.gz; popd
else
  pushd gdal; wget https://s3.amazonaws.com/yum-geonode.boundlessps.com/src/MrSID_DSDK-9.5.1.4427-linux.x86-64.gcc44.tar.gz; popd
  pushd gdal; wget https://github.com/mm2/Little-CMS/archive/lcms2.8.tar.gz; popd
  pushd python27; wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz; popd
  pushd python27; wget https://pypi.python.org/packages/1d/04/97e37cf85972ea19364c22db34ee8192db3876a80ed5bffd6413dcdabe2d/setuptools-28.7.1.tar.gz; popd
  pushd python27; wget https://pypi.python.org/packages/8b/2c/c0d3e47709d0458816167002e1aa3d64d03bdeb2a9d57c5bd18448fd24cd/virtualenv-15.0.3.tar.gz; popd
fi

echo '-------------------'
echo 'finished get sources'

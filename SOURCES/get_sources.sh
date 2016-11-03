#!/bin/bash

echo 'downloading sources'
echo '-------------------'

version=`rpm -qa \*-release | grep -Ei "redhat|centos" | cut -d"-" -f3`

pushd erlang; wget https://github.com/erlang/otp/archive/OTP-18.3.4.4.tar.gz; popd
pushd libkml; wget https://github.com/google/libkml/archive/release-1.2.tar.gz; popd
pushd openjpeg2; wget https://github.com/uclouvain/openjpeg/archive/v2.1.2.tar.gz; popd
pushd gdal; wget http://download.osgeo.org/gdal/2.0.3/gdal-2.0.3.tar.gz; popd
pushd tomcat8; wget http://apache.mirror.rafal.ca/tomcat/tomcat-8/v8.5.6/bin/apache-tomcat-8.5.6.tar.gz; popd

if [ $version == 7 ];then
  pushd erlang; wget https://s3.amazonaws.com/yum-geonode.boundlessps.com/src/MrSID_DSDK-9.5.1.4427-linux.x86-64.gcc48.tar.gz; popd
else
  pushd gdal; wget https://s3.amazonaws.com/yum-geonode.boundlessps.com/src/MrSID_DSDK-9.5.1.4427-linux.x86-64.gcc44.tar.gz; popd
  pushd gdal; wget https://github.com/mm2/Little-CMS/archive/lcms2.8.tar.gz; popd
  pushd python27; wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz; popd
  pushd python27; wget https://pypi.python.org/packages/1d/04/97e37cf85972ea19364c22db34ee8192db3876a80ed5bffd6413dcdabe2d/setuptools-28.7.1.tar.gz; popd
  pushd python27; wget https://github.com/pypa/virtualenv/archive/15.0.3.tar.gz; popd
fi

echo '-------------------'
echo 'finished get sources'

#!/usr/bin/env bash
version=`rpm -qa \*-release | grep -Ei "redhat|centos" | cut -d"-" -f3`
if [ $version == 7 ];then
  sudo yum -y update
  rpm -ivh http://yum.postgresql.org/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm
  sudo yum -y install ant \
                 autoconf \
                 bzip2-devel \
                 chrpath \
                 cmake \
                 cppunit \
                 createrepo \
                 libdb-devel \
                 dos2unix \
                 doxygen \
                 expat-devel \
                 freetype-devel \
                 httpd-devel \
                 gcc \
                 gcc-c++ \
                 gdbm-devel \
                 geos-devel \
                 gettext-devel \
                 git \
                 gtk2-devel \
                 java-1.8.0-openjdk-devel \
                 json-c-devel \
                 libcurl-devel \
                 libjpeg-turbo-devel \
                 libtiff-devel \
                 libtool \
                 libpng-devel \
                 libxml2-devel \
                 libxslt-devel \
                 littlecms-devel \
                 make \
                 openssl-devel \
                 openldap-devel \
                 poppler-devel \
                 postgresql95-devel \
                 proj-devel \
                 readline-devel \
                 rpmdevtools \
                 sqlite-devel \
                 swig \
                 tk-devel \
                 unzip \
                 xerces-c-devel \
                 zip \
                 zlib-devel

else
  curl -o /etc/yum.repos.d/exchange.repo https://yum.boundlessps.com/geoshape.repo
  sudo yum -y update
  sudo yum -y install ant \
                 autoconf \
                 bzip2-devel \
                 chrpath \
                 cmake \
                 cppunit \
                 createrepo \
                 db4-devel \
                 dos2unix \
                 doxygen \
                 expat-devel \
                 freetype-devel \
                 httpd-devel \
                 gcc \
                 gcc-c++ \
                 gdbm-devel \
                 geos-devel \
                 gettext-devel \
                 git \
                 gtk2-devel \
                 java-1.8.0-openjdk-devel \
                 json-c-devel \
                 libcurl-devel \
                 libjpeg-turbo-devel \
                 libtiff-devel \
                 libtool \
                 libpng-devel \
                 libxml2-devel \
                 libxslt-devel \
                 littlecms-devel \
                 make \
                 openssl-devel \
                 openldap-devel \
                 poppler-devel \
                 postgresql95-devel \
                 proj-devel \
                 readline-devel \
                 rpmdevtools \
                 sqlite-devel \
                 swig \
                 tk-devel \
                 unzip \
                 xerces-c-devel \
                 zip \
                 zlib-devel
fi

pushd /vagrant/SOURCES
./get_sources.sh
popd

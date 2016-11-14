#!/usr/bin/env bash
version=`rpm -qa \*-release | grep -Ei "redhat|centos" | cut -d"-" -f3`
if [ $version == 7 ];then
echo "[boundlessps]
name=boundlessps
baseurl=https://yum.boundlessps.com/el7/x86_64
enabled=1
gpgcheck=1
gpgkey=https://yum.boundlessps.com/RPM-GPG-KEY-yum.boundlessps.com
" > /etc/yum.repos.d/boundlessps.repo
  rpm -ivh https://yum.postgresql.org/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
  rpm -ivh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
  sudo yum -y update
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
                 postgresql96-devel \
                 proj-devel \
                 readline-devel \
                 rpmdevtools \
                 sqlite-devel \
                 swig-1.3.40 \
                 tk-devel \
                 unzip \
                 xerces-c-devel \
                 zip \
                 zlib-devel \
                 hdf5-devel \
                 netcdf-devel

else
echo "[boundlessps]
name=boundlessps
baseurl=https://yum.boundlessps.com/el6/x86_64
enabled=1
gpgcheck=1
gpgkey=https://yum.boundlessps.com/RPM-GPG-KEY-yum.boundlessps.com
" > /etc/yum.repos.d/boundlessps.repo

  rpm -ivh https://yum.postgresql.org/9.6/redhat/rhel-6-x86_64/pgdg-centos96-9.6-3.noarch.rpm
  rpm -ivh https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
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
                 postgresql96-devel \
                 proj-devel \
                 readline-devel \
                 rpmdevtools \
                 sqlite-devel \
                 swig \
                 tk-devel \
                 unzip \
                 xerces-c-devel \
                 zip \
                 zlib-devel \
                 hdf5-devel \
                 netcdf-devel
fi

pushd /vagrant/SOURCES
./get_sources.sh
popd

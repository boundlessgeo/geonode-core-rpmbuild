%define name python27-virtualenv
%define version 15.0.3
%define release 1%{?dist}
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

Summary: Virtual Python Environment builder.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/8b/2c/c0d3e47709d0458816167002e1aa3d64d03bdeb2a9d57c5bd18448fd24cd/virtualenv-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27 python27-setuptools
Requires: python27 python27-setuptools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
A tool to create isolated Python environments.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n virtualenv-%{version} -n virtualenv-%{version}

%build
   python2.7 setup.py build

%install
   python2.7 setup.py install --prefix=/usr/local --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
   rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Nov 03 2016 BerryDaniel <dberry@boundlessgeo.com> [15.0.3-1]
- Updated to 15.0.3

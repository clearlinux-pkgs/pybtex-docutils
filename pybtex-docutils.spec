#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybtex-docutils
Version  : 1.0.1
Release  : 25
URL      : https://files.pythonhosted.org/packages/41/3b/69c21deab7974b76018124b441c059edc6d6cec970ac038e5f62682eac8a/pybtex-docutils-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/3b/69c21deab7974b76018124b441c059edc6d6cec970ac038e5f62682eac8a/pybtex-docutils-1.0.1.tar.gz
Summary  : A docutils backend for pybtex.
Group    : Development/Tools
License  : MIT
Requires: pybtex-docutils-license = %{version}-%{release}
Requires: pybtex-docutils-python = %{version}-%{release}
Requires: pybtex-docutils-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(pybtex)

%description
pybtex-docutils
===============
|imagegithub| |imagecodecov|
A docutils backend for pybtex.

%package license
Summary: license components for the pybtex-docutils package.
Group: Default

%description license
license components for the pybtex-docutils package.


%package python
Summary: python components for the pybtex-docutils package.
Group: Default
Requires: pybtex-docutils-python3 = %{version}-%{release}

%description python
python components for the pybtex-docutils package.


%package python3
Summary: python3 components for the pybtex-docutils package.
Group: Default
Requires: python3-core
Provides: pypi(pybtex_docutils)
Requires: pypi(docutils)
Requires: pypi(pybtex)

%description python3
python3 components for the pybtex-docutils package.


%prep
%setup -q -n pybtex-docutils-1.0.1
cd %{_builddir}/pybtex-docutils-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637348340
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybtex-docutils
cp %{_builddir}/pybtex-docutils-1.0.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/pybtex-docutils/b060e9b6372c36f719c9b9f2ccff3fd48c732512
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybtex-docutils/b060e9b6372c36f719c9b9f2ccff3fd48c732512

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

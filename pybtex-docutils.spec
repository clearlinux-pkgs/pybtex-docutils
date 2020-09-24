#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybtex-docutils
Version  : 0.2.2
Release  : 12
URL      : https://files.pythonhosted.org/packages/ee/4a/b93e424f93821abf74b189b9432cb92aab6e4663405016ca5d97667f2748/pybtex-docutils-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ee/4a/b93e424f93821abf74b189b9432cb92aab6e4663405016ca5d97667f2748/pybtex-docutils-0.2.2.tar.gz
Summary  : A docutils backend for pybtex.
Group    : Development/Tools
License  : MIT
Requires: pybtex-docutils-license = %{version}-%{release}
Requires: pybtex-docutils-python = %{version}-%{release}
Requires: pybtex-docutils-python3 = %{version}-%{release}
Requires: docutils
Requires: pybtex
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : pybtex
BuildRequires : six

%description
A docutils backend for pybtex.
* Download: http://pypi.python.org/pypi/pybtex-docutils/#downloads

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
Requires: pypi(six)

%description python3
python3 components for the pybtex-docutils package.


%prep
%setup -q -n pybtex-docutils-0.2.2
cd %{_builddir}/pybtex-docutils-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583539200
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybtex-docutils
cp %{_builddir}/pybtex-docutils-0.2.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/pybtex-docutils/764cddd5a1c88d5cac5366ee273879602b4d14c6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybtex-docutils/764cddd5a1c88d5cac5366ee273879602b4d14c6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

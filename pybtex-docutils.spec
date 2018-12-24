#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybtex-docutils
Version  : 0.2.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/3e/ec/3bba74a029a032f4260dcb3ceb927da1f9dfa77bc94720d49c47ee446390/pybtex-docutils-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/ec/3bba74a029a032f4260dcb3ceb927da1f9dfa77bc94720d49c47ee446390/pybtex-docutils-0.2.1.tar.gz
Summary  : A docutils backend for pybtex.
Group    : Development/Tools
License  : MIT
Requires: pybtex-docutils-license = %{version}-%{release}
Requires: pybtex-docutils-python = %{version}-%{release}
Requires: pybtex-docutils-python3 = %{version}-%{release}
Requires: docutils
Requires: six
BuildRequires : buildreq-distutils3

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

%description python3
python3 components for the pybtex-docutils package.


%prep
%setup -q -n pybtex-docutils-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545682338
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybtex-docutils
cp LICENSE.rst %{buildroot}/usr/share/package-licenses/pybtex-docutils/LICENSE.rst
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybtex-docutils/LICENSE.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

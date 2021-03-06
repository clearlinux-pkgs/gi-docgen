#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gi-docgen
Version  : 2022.1
Release  : 4
URL      : https://gitlab.gnome.org/GNOME/gi-docgen/-/archive/2022.1/gi-docgen-2022.1.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/gi-docgen/-/archive/2022.1/gi-docgen-2022.1.tar.gz
Summary  : Documentation tool for GObject-based libraries
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-3.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 MIT MPL-1.1 OFL-1.1
Requires: gi-docgen-bin = %{version}-%{release}
Requires: gi-docgen-license = %{version}-%{release}
Requires: gi-docgen-man = %{version}-%{release}
Requires: gi-docgen-python = %{version}-%{release}
Requires: gi-docgen-python3 = %{version}-%{release}
Requires: graphviz-extras
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markdown)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(pygments)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(toml)
BuildRequires : pypi(typogrify)
BuildRequires : pypi(wheel)
Patch1: backport-unfatal-warnings.patch

%description
<!--
SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-or-later
-->
GI-DocGen: Documentation tool for GObject-based libraries
-------------------------------------------------------------------------------

%package bin
Summary: bin components for the gi-docgen package.
Group: Binaries
Requires: gi-docgen-license = %{version}-%{release}

%description bin
bin components for the gi-docgen package.


%package dev
Summary: dev components for the gi-docgen package.
Group: Development
Requires: gi-docgen-bin = %{version}-%{release}
Provides: gi-docgen-devel = %{version}-%{release}
Requires: gi-docgen = %{version}-%{release}

%description dev
dev components for the gi-docgen package.


%package license
Summary: license components for the gi-docgen package.
Group: Default

%description license
license components for the gi-docgen package.


%package man
Summary: man components for the gi-docgen package.
Group: Default

%description man
man components for the gi-docgen package.


%package python
Summary: python components for the gi-docgen package.
Group: Default
Requires: gi-docgen-python3 = %{version}-%{release}

%description python
python components for the gi-docgen package.


%package python3
Summary: python3 components for the gi-docgen package.
Group: Default
Requires: python3-core
Provides: pypi(gi_docgen)
Requires: pypi(jinja2)
Requires: pypi(markdown)
Requires: pypi(markupsafe)
Requires: pypi(pygments)
Requires: pypi(toml)
Requires: pypi(typogrify)

%description python3
python3 components for the gi-docgen package.


%prep
%setup -q -n gi-docgen-2022.1
cd %{_builddir}/gi-docgen-2022.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648246260
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gi-docgen
cp %{_builddir}/gi-docgen-2022.1/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/gi-docgen/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/gi-docgen-2022.1/LICENSES/CC-BY-SA-3.0.txt %{buildroot}/usr/share/package-licenses/gi-docgen/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51
cp %{_builddir}/gi-docgen-2022.1/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/gi-docgen/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/gi-docgen-2022.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gi-docgen/3cb34cfc72e87654683f2894299adf912d14b284
cp %{_builddir}/gi-docgen-2022.1/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/gi-docgen/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/gi-docgen-2022.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gi-docgen/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
cp %{_builddir}/gi-docgen-2022.1/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/gi-docgen/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
cp %{_builddir}/gi-docgen-2022.1/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/gi-docgen/ca2fd1439eb3e23507f13855e5450c5d617db83d
cp %{_builddir}/gi-docgen-2022.1/LICENSES/OFL-1.1.txt %{buildroot}/usr/share/package-licenses/gi-docgen/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gi-docgen

%files dev
%defattr(-,root,root,-)
/usr/share/pkgconfig/gi-docgen.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gi-docgen/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
/usr/share/package-licenses/gi-docgen/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/gi-docgen/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/gi-docgen/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/gi-docgen/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/gi-docgen/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/gi-docgen/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
/usr/share/package-licenses/gi-docgen/ca2fd1439eb3e23507f13855e5450c5d617db83d
/usr/share/package-licenses/gi-docgen/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gi-docgen.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

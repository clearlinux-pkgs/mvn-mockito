#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mockito
Version  : 1.9.5
Release  : 4
URL      : https://github.com/mockito/mockito/archive/v1.9.5.tar.gz
Source0  : https://github.com/mockito/mockito/archive/v1.9.5.tar.gz
Source1  : https://repo1.maven.org/maven2/org/mockito/mockito-all/1.8.2/mockito-all-1.8.2.jar
Source2  : https://repo1.maven.org/maven2/org/mockito/mockito-all/1.8.2/mockito-all-1.8.2.pom
Source3  : https://repo1.maven.org/maven2/org/mockito/mockito-all/1.8.5/mockito-all-1.8.5.jar
Source4  : https://repo1.maven.org/maven2/org/mockito/mockito-all/1.8.5/mockito-all-1.8.5.pom
Source5  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar
Source6  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.pom
Source7  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.jar
Source8  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: mvn-mockito-data = %{version}-%{release}
Requires: mvn-mockito-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Some fragments of Mockito source code might be inspired by libraries of licenses collected in this folder.

%package data
Summary: data components for the mvn-mockito package.
Group: Data

%description data
data components for the mvn-mockito package.


%package license
Summary: license components for the mvn-mockito package.
Group: Default

%description license
license components for the mvn-mockito package.


%prep
%setup -q -n mockito-1.9.5

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-mockito
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-mockito/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-mockito/NOTICE
cp cglib-and-asm/licenses/asm-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/cglib-and-asm_licenses_asm-license.txt
cp cglib-and-asm/licenses/cglib-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/cglib-and-asm_licenses_cglib-license.txt
cp doc/licenses/commons-lang-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/doc_licenses_commons-lang-license.txt
cp doc/licenses/easymock-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/doc_licenses_easymock-license.txt
cp doc/licenses/jmock-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/doc_licenses_jmock-license.txt
cp lib/build/sorcerer-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/lib_build_sorcerer-license.txt
cp lib/repackaged/asm-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/lib_repackaged_asm-license.txt
cp lib/repackaged/cglib-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/lib_repackaged_cglib-license.txt
cp lib/run/hamcrest-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/lib_run_hamcrest-license.txt
cp lib/run/objenesis-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/lib_run_objenesis-license.txt
cp src/org/mockito/internal/creation/jmock/jmock-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/src_org_mockito_internal_creation_jmock_jmock-license.txt
cp src/org/mockito/internal/matchers/apachecommons/commons-lang-license.txt %{buildroot}/usr/share/package-licenses/mvn-mockito/src_org_mockito_internal_matchers_apachecommons_commons-lang-license.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.2/mockito-all-1.8.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.2/mockito-all-1.8.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.5/mockito-all-1.8.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.5/mockito-all-1.8.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.2/mockito-all-1.8.2.jar
/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.2/mockito-all-1.8.2.pom
/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.5/mockito-all-1.8.5.jar
/usr/share/java/.m2/repository/org/mockito/mockito-all/1.8.5/mockito-all-1.8.5.pom
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.pom
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.jar
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-mockito/LICENSE
/usr/share/package-licenses/mvn-mockito/NOTICE
/usr/share/package-licenses/mvn-mockito/cglib-and-asm_licenses_asm-license.txt
/usr/share/package-licenses/mvn-mockito/cglib-and-asm_licenses_cglib-license.txt
/usr/share/package-licenses/mvn-mockito/doc_licenses_commons-lang-license.txt
/usr/share/package-licenses/mvn-mockito/doc_licenses_easymock-license.txt
/usr/share/package-licenses/mvn-mockito/doc_licenses_jmock-license.txt
/usr/share/package-licenses/mvn-mockito/lib_build_sorcerer-license.txt
/usr/share/package-licenses/mvn-mockito/lib_repackaged_asm-license.txt
/usr/share/package-licenses/mvn-mockito/lib_repackaged_cglib-license.txt
/usr/share/package-licenses/mvn-mockito/lib_run_hamcrest-license.txt
/usr/share/package-licenses/mvn-mockito/lib_run_objenesis-license.txt
/usr/share/package-licenses/mvn-mockito/src_org_mockito_internal_creation_jmock_jmock-license.txt
/usr/share/package-licenses/mvn-mockito/src_org_mockito_internal_matchers_apachecommons_commons-lang-license.txt

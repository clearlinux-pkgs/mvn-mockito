#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mockito
Version  : 1.9.5
Release  : 1
URL      : https://github.com/mockito/mockito/archive/v1.9.5.tar.gz
Source0  : https://github.com/mockito/mockito/archive/v1.9.5.tar.gz
Source1  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar
Source2  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.pom
Source3  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.jar
Source4  : https://repo1.maven.org/maven2/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-mockito-data = %{version}-%{release}

%description
Some fragments of Mockito source code might be inspired by libraries of licenses collected in this folder.

%package data
Summary: data components for the mvn-mockito package.
Group: Data

%description data
data components for the mvn-mockito package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.pom
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.jar
/usr/share/java/.m2/repository/org/mockito/mockito-core/1.9.5/mockito-core-1.9.5.pom

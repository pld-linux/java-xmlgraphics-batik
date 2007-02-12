Summary:	Java SVG support
Summary(pl.UTF-8):	Wsparcie dla SVG dla języka Java
Name:		batik
Version:	1.6
%define	_snap	408156
Release:	1.%{_snap}.1
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	%{name}-svn-%{_snap}.tar.bz2
# Source0-md5:	4b0d5ee20c804c244b547f3427502652
URL:		http://xml.apache.org/batik/
BuildRequires:	jdk
BuildRequires:	unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
Java SVG support.

%description -l pl.UTF-8
Wsparcie dla SVG dla języka Java.

%package doc
Summary:	Documentation for the Batik library
Summary(pl.UTF-8):	Dokumentacja dla biblioteki Batik
Group:		Documentation

%description doc
Documentation for the Batik library.

%description doc -l pl.UTF-8
Dokumentacja dla biblioteki Batik.

%prep
%setup -q -n xml-%{name}

%build
JAVA_HOME=%{_libdir}/java
#JAVA_HOME=/usr/lib/jvm/java-sun-1.5.0.06
export JAVA_HOME

#sh build.sh dist-tgz # does not work :-(
sh build.sh dist-zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}/%{name}/lib

install %{name}-%{version}/lib/*.jar $RPM_BUILD_ROOT%{_javaclassdir}/%{name}/lib
install %{name}-%{version}/*.jar $RPM_BUILD_ROOT%{_javaclassdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README
%dir %{_javaclassdir}/%{name}
%{_javaclassdir}/%{name}/*.jar
%dir %{_javaclassdir}/%{name}/lib
%{_javaclassdir}/%{name}/lib/*.jar

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{version}/docs/* %{name}-%{version}/samples

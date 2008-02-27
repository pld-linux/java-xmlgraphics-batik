Summary:	Java SVG support
Summary(pl.UTF-8):	Wsparcie dla SVG dla języka Java
Name:		batik
Version:	1.7
Release:	0.1
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xmlgraphics/batik/%{name}-src-%{version}.zip
# Source0-md5:	c117ca2241907f62a2b3031167ebf917
URL:		http://xml.apache.org/batik/
BuildRequires:	forrest
BuildRequires:	jdk
BuildRequires:	jpackage-utils
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
%setup -q

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"

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

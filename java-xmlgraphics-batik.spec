Summary:	Java SVG support
Summary(pl):	Wsparcie dla SVG dla jêzyka Java
Name:		batik
Version:	1.5.1
Release:	1
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://archive.apache.org/dist/xml/batik/%{name}-src-%{version}.zip
# Source0-md5:	8a3ba8b76dcef9415216d6a5b9685a9c
URL:		http://xml.apache.org/batik/
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
Java SVG support.

%description -l pl
Wsparcie dla SVG dla jêzyka Java.

%prep
%setup -q -n xml-%{name}

%build
JAVA_HOME=%{_libdir}/java
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
%doc README %{name}-%{version}/docs/* %{name}-%{version}/samples
%dir %{_javaclassdir}/%{name}
%{_javaclassdir}/%{name}/*.jar
%dir %{_javaclassdir}/%{name}/lib
%{_javaclassdir}/%{name}/lib/*.jar

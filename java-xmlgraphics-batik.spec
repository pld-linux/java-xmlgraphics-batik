
Summary:	Java SVG support
Summary(pl):	Wsparcie dla SVG dla jêzyka Java
Name:		batik
Version:	1.1.1
Release:	1
License:	Apache Software License
Group:		Applications/Publishing/XML/Java
URL:		http://xml.apache.org/batik
Source0:	http://xml.apache.org/batik/dist/%{name}-src-%{version}.zip
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java/

%description
Java SVG support.

%description -l pl
Wsparcie dla SVG dla jêzyka Java.

%prep
%setup -q -n xml-%{name}

%build
JAVA_HOME=%{_libdir}/java-sdk
export JAVA_HOME

#sh build.sh dist-tgz # does not work :-(
sh build.sh dist-zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}/%{name}/lib

install %{name}-%{version}/lib/*.jar $RPM_BUILD_ROOT%{_javaclassdir}/%{name}/lib
install %{name}-%{version}/*.jar $RPM_BUILD_ROOT%{_javaclassdir}/%{name}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz %{name}-%{version}/docs/* %{name}-%{version}/samples
%{_javaclassdir}/%{name}/*.jar
%{_javaclassdir}/%{name}/lib/*.jar

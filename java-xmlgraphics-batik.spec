
Summary:	Java SVG support
Summary(pl):	Wsparcie dla SVG dla jêzyka Java
Name:		batik
Version:	1.1.1
Release:	1
License:	Apache Software License
Group:		Applications/Publishing/XML/Java
Group(de):	Applikationen/Publizieren/XML/Java
Group(es):	Aplicaciones/Editoración/XML/Java
Group(pl):	Aplikacje/Publikowanie/XML/Java
Group(pt_BR):	Aplicações/Editoração/XML/Java
URL:		http://xml.apache.org/batik
Source0:	http://xml.apache.org/batik/dist/%{name}-src-%{version}.zip
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java/
%define		jredir			%{_libdir}/java-sdk/jre/lib

%description
Java SVG support.

%description -l pl
Wsparcie dla SVG dla jêzyka Java.

%prep
%setup -q -n xml-%{name}

%build
JAVA_HOME=%{_libdir}/java-sdk
export JAVA_HOME

sh build.sh compile
sh build.sh html

( cd classes
  jar cf ../%{name}.jar .
)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}

install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz %{name}-%{version}/docs/* %{name}-%{version}/samples
%{_javaclassdir}/*.jar

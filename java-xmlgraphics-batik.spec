Summary:	Java SVG support
Summary(pl):	Wsparcie dla SVG dla j�zyka Java
Name:		batik
Version:	1.1.1
Release:	2
License:	Apache
Group:		Applications/Publishing/XML/Java
URL:		http://xml.apache.org/batik/
Source0:	http://xml.apache.org/batik/dist/%{name}-src-%{version}.zip
# Source0-md5:	8601c9cba32607393c1556c1e1200b53
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java/

%description
Java SVG support.

%description -l pl
Wsparcie dla SVG dla j�zyka Java.

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
%{_javaclassdir}/%{name}/*.jar
%{_javaclassdir}/%{name}/lib/*.jar

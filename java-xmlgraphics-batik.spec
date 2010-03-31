# TODO:
# - generate docs without using forrest. It seems to be possible.
#
# Conditional build:
%bcond_with	doc		# build with docs (require apache-forrest)
%bcond_with	bootstrap	# break BR loop batik-fop
#
%define		_rel	5
Summary:	Java SVG support
Summary(pl.UTF-8):	Wsparcie dla SVG dla języka Java
Name:		batik
Version:	1.7
Release:	%{_rel}%{?with_bootstrap:.bootstrap}
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xmlgraphics/batik/%{name}-src-%{version}.zip
# Source0-md5:	c117ca2241907f62a2b3031167ebf917
Patch0:		%{name}-nodocs.patch
URL:		http://xml.apache.org/batik/
%{!?with_bootstrap:BuildRequires:	fop}
%{?with_doc:BuildRequires:	java-forrest}
BuildRequires:	java-xalan
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rhino
BuildRequires:	unzip
BuildRequires:	xml-commons-external
Requires:	java-xalan
Requires:	jre >= 1.4
Requires:	rhino
Requires:	xalan-c
Requires:	xml-commons-external
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%if %{without doc}
%patch0 -p0
%endif

rm lib/js.jar lib/xalan*.jar lib/xerces*.jar lib/xml-apis*.jar

%build
unset CLASSPATH || :
export JAVA_HOME=%{java_home}

jars='js xalan xercesImpl xml-apis xml-apis-ext'
for jar in $jars; do
	ln -s $(find-jar $jar) lib
done

%if %{without bootstrap}
	rm lib/pdf-transcoder.jar
	ln -s $(find-jar fop-transcoder) lib
%endif

#sh build.sh dist-tgz # does not work :-(
sh build.sh dist-zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}/lib

cd %{name}-%{version}
for jar in batik*.jar; do
	base=$(basename $jar .jar)
	install $jar $RPM_BUILD_ROOT%{_javadir}/$base-%{version}.jar
	ln -s $base-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$base.jar
done

cd lib
for jar in batik*.jar; do
  install $jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$jar
done

%if %{with bootstrap}
	install -p pdf-transcoder.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/pdf-transcoder.jar
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES KEYS NOTICE README
# ??? WTF dir for .jar?
%dir %{_javadir}/batik*.jar
%{_javadir}/%{name}

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc %{name}-%{version}/docs/* %{name}-%{version}/samples
%endif

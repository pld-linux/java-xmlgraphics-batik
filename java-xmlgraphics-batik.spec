# TODO:
# - generate docs without using forrest. It seems to be possible.
#
# Conditional build:
%bcond_with	doc		# build with docs (require apache-forrest)
%bcond_with	bootstrap	# break BR loop batik-fop

%include	/usr/lib/rpm/macros.java

%define		_rel	6
%define		srcname	xmlgraphics-batik
Summary:	Java SVG support
Summary(pl.UTF-8):	Wsparcie dla SVG dla języka Java
Name:		java-xmlgraphics-batik
Version:	1.7
Release:	%{_rel}%{?with_bootstrap:.bootstrap}
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xmlgraphics/batik/batik-src-%{version}.zip
# Source0-md5:	c117ca2241907f62a2b3031167ebf917
Patch0:		%{name}-nodocs.patch
URL:		http://xml.apache.org/batik/
%{?with_doc:BuildRequires:	java-forrest}
BuildRequires:	java-sun >= 1.4
BuildRequires:	java-xalan
%{!?with_bootstrap:BuildRequires:	java-xmlgraphics-fop}
BuildRequires:	jpackage-utils
BuildRequires:	rhino
BuildRequires:	unzip
BuildRequires:	xml-commons-external
Requires:	java-sun-jre >= 1.4
Requires:	java-xalan
Requires:	rhino
Requires:	xml-commons-external
Obsoletes:	batik
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
%setup -q -n batik-%{version}

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
	ln -s $(find-jar xmlgraphics-fop) lib
%endif

#sh build.sh dist-tgz # does not work :-(
sh build.sh dist-zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/%{srcname}

cd batik-%{version}
for jar in batik*.jar; do
	base=$(basename $jar .jar)
	install $jar $RPM_BUILD_ROOT%{_javadir}/xmlgraphics-$base-%{version}.jar
	ln -s xmlgraphics-$base-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xmlgraphics-$base.jar
done

cd lib
for jar in batik*.jar; do
  install $jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}/$jar
done

%if %{with bootstrap}
  install -p pdf-transcoder.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}/pdf-transcoder.jar
%endif

cd ../extensions
for jar in batik*.jar; do
  install $jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}/extension-${jar#batik-}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES KEYS NOTICE README
%{_javadir}/%{srcname}*.jar
%{_javadir}/%{srcname}

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc %{name}-%{version}/docs/* %{name}-%{version}/samples
%endif

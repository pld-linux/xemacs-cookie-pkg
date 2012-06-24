Summary:	Spook and Yow (Zippy quotes)
Summary(pl.UTF-8):	Spook i Yow (zestawy cytatów)
Name:		xemacs-cookie-pkg
%define 	srcname	cookie
Version:	1.15
Release:	3
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	70b4bde06580ec71df2a23aa95808bb7
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spook and Yow (Zippy quotes).

%description -l pl.UTF-8
Spook i Yow - zestawy cytatów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/xemacs-packages/lisp/cookie/ChangeLog
%doc %{_datadir}/xemacs-packages/pkginfo/MANIFEST.cookie
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*

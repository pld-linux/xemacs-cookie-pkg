Summary:	Spook and Yow (Zippy quotes)
Summary(pl):	Spook i Yow (zestawy cytatów)
Name:		xemacs-cookie-pkg
%define 	srcname	cookie
Version:	1.13
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spook and Yow (Zippy quotes).

%description -l pl
Spook i Yow - zestawy cytatów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/cookie/ChangeLog

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/cookie/ChangeLog.gz
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc

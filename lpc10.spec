Summary:	LPC-10 2400 bps Voice Coder
Summary(pl):	Koder g這su LPC-10 2400 bps
Name:		lpc10
Version:	1.5
Release:	1
License:	unknown
Group:		Applications/Sound
Source0:	http://www.arl.wustl.edu/~jaf/lpc/%{name}-%{version}.tar.gz
URL:		http://www.arl.wustl.edu/~jaf/lpc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LPC-10 2400 bps Voice Coder.

%description -l pl
Koder g這su LPC-10 2400 bps.

%package devel
Summary:	LPC-10 2400 bps Voice Coder library and headers
Summary(pl):	Biblioteka i pliki nag堯wkowe kodera g這su LPC-10 2400 bps
Group:		Development/Libraries

%description devel
LPC-10 2400 bps Voice Coder library and headers.

%description devel -l pl
Biblioteka i pliki nag堯wkowe kodera g這su LPC-10 2400 bps.

%prep
%setup -q

%build
%{__make} -C lpc55-C/lpc10 \
	CFLAGS="%{rpmcflags} -I.. -Wall"
%{__make} -C lpc55-C \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install lpc55-C/liblpc10.a $RPM_BUILD_ROOT%{_libdir}
install lpc55-C/lpc10.h $RPM_BUILD_ROOT%{_includedir}
install lpc55-C/{,un}nuke{,2} $RPM_BUILD_ROOT%{_bindir}

mv -f lpc55-C/README README.tools
mv -f lpc55-C/lpc10/README README.lpc10

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.tools
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc FAQ README README-1.0 README.lpc10
%{_libdir}/lib*.a
%{_includedir}/*.h

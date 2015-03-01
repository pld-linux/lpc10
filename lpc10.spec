Summary:	LPC-10 2400 bps Voice Coder
Summary(pl.UTF-8):	Koder głosu LPC-10 2400 bps
Name:		lpc10
Version:	1.5
Release:	5
License:	unknown
Group:		Applications/Sound
Source0:	http://www.arl.wustl.edu/~jaf/lpc/%{name}-%{version}.tar.gz
# Source0-md5:	c6d9174b78c4aafa67ae50b232a3aef3
Patch0:		%{name}-shared.patch
URL:		http://www.arl.wustl.edu/~jaf/lpc/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LPC-10 2400 bps Voice Coder library and tools.

%description -l pl.UTF-8
Koder głosu LPC-10 2400 bps - biblioteka i narzędzia.

%package devel
Summary:	LPC-10 2400 bps Voice Coder headers files
Summary(pl.UTF-8):	Pliki nagłówkowe kodera głosu LPC-10 2400 bps
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
LPC-10 2400 bps Voice Coder headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe kodera głosu LPC-10 2400 bps.

%package static
Summary:	LPC-10 2400 bps Voice Coder static library
Summary(pl.UTF-8):	Statyczna biblioteka kodera głosu LPC-10 2400 bps
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LPC-10 2400 bps Voice Coder static library.

%description static -l pl.UTF-8
Statyczna biblioteka kodera głosu LPC-10 2400 bps.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C lpc55-C \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C lpc55-C install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%{__mv} lpc55-C/README README.tools
%{__mv} lpc55-C/lpc10/README README.lpc10

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ README README-1.0 README.lpc10 README.tools
%attr(755,root,root) %{_bindir}/nuke
%attr(755,root,root) %{_bindir}/nuke2
%attr(755,root,root) %{_bindir}/unnuke
%attr(755,root,root) %{_bindir}/unnuke2
%attr(755,root,root) %{_libdir}/liblpc10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblpc10.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblpc10.so
%{_libdir}/liblpc10.la
%{_includedir}/lpc10.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblpc10.a

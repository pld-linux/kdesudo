#
# Conditional build:
#
%define		qtver		4.6.3
%define		kdever		4.4.5

Summary:	Kdesudo
Summary(pl.UTF-8):	Kdesudo
Name:		kdesudo
Version:	3.4.2.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://launchpad.net/kdesudo/3.x/3.4.2.3/+download/%{name}-%{version}.tar.gz
# Source0-md5:	d744b9bce49aa2879c3bc07591899319
URL:		https://launchpad.net/kdesudo
Patch0:		%{name}-nodoc.patch
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.577
Requires:	sudo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KdeSudo is a frontend for sudo. Unlike kdesu, it uses directly sudo as
backend.

%description -l pl.UTF-8
Kdesudo to frontend dla sudo. W przeciwieństwie do kdesu, używa sudo
bezpośrednio jako backend.

%prep
%setup -q
%patch0 -p0

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdesudo

%define		efl_ver		1.8

Summary:	Epour - EFL based BitTorrent client
Summary(pl.UTF-8):	Epour - klient BitTorrenta oparty na bibliotekach EFL
Name:		epour
Version:	0.6.0
Release:	1
License:	BSD
Group:		Applications/Network
Source0:	http://download.enlightenment.org/rel/apps/epour/%{name}-%{version}.tar.xz
# Source0-md5:	2828085e727b026707098e851d437c43
URL:		http://git.enlightenment.org/apps/epour.git/
BuildRequires:	python-devel >= 2
BuildRequires:	python-distutils-extra
BuildRequires:	rpmbuild(macros) >= 1.241
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python-dbus
Requires:	python-e_dbus >= %{efl_ver}
Requires:	python-ecore >= %{efl_ver}
Requires:	python-elementary >= %{efl_ver}
Requires:	python-evas >= %{efl_ver}
Requires:	python-libtorrent-rasterbar >= 0.16.0
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epour is a BitTorrent client based on EFL and rb-libtorrent libraries.

%description -l pl.UTF-8
Epour to klient BitTorrenta oparty na bibliotekach EFL i
rb-libtorrent.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--skip-build \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO debian/changelog
%attr(755,root,root) %{_bindir}/epour
%{py_sitescriptdir}/epour-%{version}-py*.egg-info
%{py_sitescriptdir}/epour

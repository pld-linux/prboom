Summary:	PrBoom - a version of classic 3D shoot-em-up game
Summary(pl):	PrBoom - wersja klasycznej strzelaniny 3D
Name:		prboom
Version:	2.3.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/prboom/%{name}-%{version}.tar.gz
# Source0-md5:	e18224379c9e19b12ad13c38b6d87904
Patch0:		%{name}-datadir.patch
URL:		http://prboom.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	SDL_net-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	smpeg-devel
Obsoletes:	lsdldoom
Obsoletes:	lxdoom
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PrBoom is a version of the 3D shoot'em'up Doom, originally by Id
software. It is based on Boom, a version of Doom adapted by TeamTNT
(http://www.teamtnt.com/) for DOS. PrBoom uses the SDL library,
meaning it can run on a variety of different systems, including
Windows, X11, Linux/SVGALib.

%description -l pl
PrBoom jest wersj± strzelaniny 3D Doom, napisanej przez Id Software.
Jest bazowana na Boom, wersji Doom zaadaptowanej przez TeamTNT
(http://www.teamtnt.com/) pod DOS. PrBoom u¿ywa biblioteki SDL, co
oznacza, ¿e mo¿e dzia³aæ na wielu systemach, w tym Windows, X11,
Linux/SVGALib.

%prep
%setup -q
%patch -p1

%build
cp -f /usr/share/automake/config.* autotools
%{__autoconf}
%configure \
	--disable-cpu-opt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gamesdir=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc/{*.txt,README*}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[56]/*
%{_datadir}/games/doom

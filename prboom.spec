Summary:	PrBoom - a version of classic 3D shoot-em-up game
Summary(pl.UTF-8):	PrBoom - wersja klasycznej strzelaniny 3D
Name:		prboom
Version:	2.5.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/prboom/%{name}-%{version}.tar.gz
# Source0-md5:	a8a15f61fa2626ab98051ab2703378c4
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://prboom.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
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

%description -l pl.UTF-8
PrBoom jest wersją strzelaniny 3D Doom, napisanej przez Id Software.
Jest bazowana na Boom, wersji Doom zaadaptowanej przez TeamTNT
(http://www.teamtnt.com/) pod DOS. PrBoom używa biblioteki SDL, co
oznacza, że może działać na wielu systemach, w tym Windows, X11,
Linux/SVGALib.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* autotools
%{__aclocal} -I autotools
%{__autoconf}
%{__automake}
%configure \
	--disable-cpu-opt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gamesdir=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc/{*.txt,README*}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[56]/*
%{_datadir}/games/doom
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop

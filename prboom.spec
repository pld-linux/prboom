Summary:	PrBoom - a version of classic 3D shoot-em-up game
Summary(pl):	PrBoom - wersja klasycznej strzelaniny 3D
Name:		prboom
Version:	2.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://download.sourceforge.net/pub/sourceforge/prboom/%{name}-%{version}.tar.gz
URL:		http://prboom.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	SDL_net-devel >= 1.2.0
BuildRequires:	smpeg-devel
BuildRequires:	autoconf
Obsoletes:	lxdoom
Obsoletes:	lsdldoom
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
PrBoom is a version of the 3D shoot'em'up Doom, originally by Id
software. It is based on Boom, a version of Doom adapted by TeamTNT
(http://www.teamtnt.com/) for DOS. PrBoom uses the SDL library,
meaning it can run on a variety of different systems, including
Windows, X11, Linux/SVGALib.

%description -l pl
PrBoom jest wersj� strzelaniny 3D Doom, napisanej przez Id Software.
Jest bazowana na Boom, wersji Doom zaadaptowanej przez TeamTNT
(http://www.teamtnt.com/) pod DOS. PrBoom u�ywa biblioteki SDL, co
oznacza, �e mo�e dzia�a� na wielu systemach, w tym Windows, X11,
Linux/SVGALib.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--disable-cpu-opt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gamesdir=%{_bindir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO doc/{*.txt,README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[56]/*
%{_datadir}/games/doom

Summary:	Doom - classic 3D shoot-em-up game
Name:		prboom
Version:	2.1.2
Release:	3
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://download.sourceforge.net/pub/sourceforge/prboom/%{name}-%{version}-src.tar.gz
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.1.0
BuildRequires:	SDL_net-devel >= 1.1.0
BuildRequires:	smpeg-devel
URL:		http://prboom.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Doom is the classic 3D shoot-em-up game. It must have been one of the
best selling games ever; it totally outclassed any 3D world games that
preceded it, with amazing speed, flexibility, and outstanding
gameplay. The specs to the game were released, and thousands of extra
levels were written by fans of the game; even today new levels are
written for Doom faster then any one person could play them.

%prep
%setup -q

%build
%configure \
	--disable-cpu-opt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gamesdir=%{_bindir}

gzip -9nf NEWS README TODO doc/{*.txt,README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[56]/*
%{_datadir}/games/doom

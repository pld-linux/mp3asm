Summary:	A small tool to fix and manipulate mp3 files
Summary(pl):	Ma³e narzêdzie do naprawiania i obróbki plików mp3
Name:		mp3asm
Version:	0.01
Release:	1
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Copyright:	Oliver Fromme <olli@fromme.com
Source0:	%{name}-%{version}.tar.gz
URL:		http://dorifer.heim3.tu-clausthal.de/~olli/mpg123/%{name}.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3asm is a small but useful tool which can be used for the following:
finding errors in MPEG audio (.mp3) files, fixing broken mp3 files,
cutting and re-assembling mp3 files.

%description -l pl
mp3asm jest ma³ym ale u¿ytecznym narzêdziem które mo¿e byæ u¿yte do:
znajdowania b³êdów w plikach d¼wiêkowych MPEG (.mp3), naprawiania
uszkodzonych plików mp3, wycinania fragmentów plików i ich montowania.

%prep
%setup -q

%build
%{__make} CFLAGS="{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mp3asm $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*

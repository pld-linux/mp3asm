Summary:	A small tool to fix and manipulate MP3 files
Summary(pl.UTF-8):	Małe narzędzie do naprawiania i obróbki plików MP3
Name:		mp3asm
Version:	0.1.3
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3asm/%{name}-%{version}.tar.bz2
# Source0-md5:	97d31ba2d88c48449d1dfb5a51581db6
URL:		http://www.mp3asm.com/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3asm is a small but useful tool which can be used for the following:
finding errors in MPEG audio (.MP3) files, fixing broken MP3 files,
cutting and re-assembling MP3 files.

%description -l pl.UTF-8
mp3asm jest małym ale użytecznym narzędziem które może być użyte do:
znajdowania błędów w plikach dźwiękowych MPEG (.MP3), naprawiania
uszkodzonych plików MP3, wycinania fragmentów plików i ich montowania.

%prep
%setup -q -n %{name}-0.1

%build
%{__autoconf}
%configure

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/*

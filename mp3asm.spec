Summary:	A small tool to fix and manipulate mp3 files
Summary(pl):	Ma³e narzêdzie do naprawiania i obróbki plików mp3
Name:		mp3asm
Version:	0.1.3
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3asm/%{name}-%{version}.tar.bz2
# Source0-md5:	97d31ba2d88c48449d1dfb5a51581db6
URL:		http://www.mp3asm.com/
BuildRequires:	autoconf
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
%setup -q -n %{name}-0.1

%build
%{__autoconf}
%configure

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/*

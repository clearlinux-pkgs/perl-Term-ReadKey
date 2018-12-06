#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-ReadKey
Version  : 2.37
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/TermReadKey-2.37.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/TermReadKey-2.37.tar.gz
Summary  : 'Change terminal modes, and perform non-blocking reads.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Term-ReadKey-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Term::ReadKey 2.36 - Change terminal modes, and perform non-blocking reads.
2001-2016 Jonathan Stowe and others

%package dev
Summary: dev components for the perl-Term-ReadKey package.
Group: Development
Requires: perl-Term-ReadKey-lib = %{version}-%{release}
Provides: perl-Term-ReadKey-devel = %{version}-%{release}

%description dev
dev components for the perl-Term-ReadKey package.


%package lib
Summary: lib components for the perl-Term-ReadKey package.
Group: Libraries

%description lib
lib components for the perl-Term-ReadKey package.


%prep
%setup -q -n TermReadKey-2.37

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Term/ReadKey.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::ReadKey.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Term/ReadKey/ReadKey.so

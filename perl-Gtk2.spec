#
# Conditional build:
# _with_tests - perform "make test" (requires X server)
#
# TODO:                                                                         
# - check BRs                                                                   
#              
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gtk2
Summary:	Perl interface to the 2.x series of the Gimp Toolkit library
Summary(pl):	Perlowy interfejs do wersji 2.x biblioteki Gimp Toolkit
Name:		perl-%{pnam}
Version:	0.91
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	6c652d7d44e632d8e8d82ad0b72d9641
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(Glib::PkgConfig)
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2 module allows a perl developer to use the Gtk+ graphical
user interface library.

%description -l pl
Modu³ Gtk2 pozwala programistom perlowym na u¿ywanie biblioteki
interfejsu graficznego Gtk+.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes TODO
%{perl_vendorarch}/%{pnam}
%{perl_vendorarch}/%{pnam}.pm
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*

#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gtk2
Summary:	Perl interface to the 2.x series of the Gimp Toolkit library
Summary(pl):	Perlowy interfejs do wersji 2.x biblioteki Gimp Toolkit
Name:		perl-%{pnam}
Version:	1.012
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	d5616cedf105e9327d6ed62653cb408f
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl-Glib >= 1.012
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Gnome2 \
        $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pnam}/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes TODO
%{perl_vendorarch}/%{pnam}
%{perl_vendorarch}/%{pnam}.pm
%dir %{perl_vendorarch}/auto/Gnome2
%dir %{perl_vendorarch}/auto/Gtk2
%dir %{perl_vendorarch}/Gnome2
%attr(755,root,root) %{perl_vendorarch}/auto/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pnam}/*.bs
%{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/Gnome2
%{_mandir}/man3/*

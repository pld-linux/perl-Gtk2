#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gtk2
Summary:	Perl interface to the 2.x series of the Gimp Toolkit library
Summary(pl):	Perlowy interfejs do wersji 2.x biblioteki Gimp Toolkit
Name:		perl-%{pnam}
Version:	1.033
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	cdefdd73a2d3a9b74145e92bac9f5874
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.1
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.00
BuildRequires:	perl-Glib >= 1.033
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gtk+2 >= 2.0.0
Requires:	perl-Glib >= 1.033
Obsoletes:	perl-Gnome2-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2 module allows a perl developer to use the Gtk+ graphical
user interface library.

%description -l pl
Modu³ Gtk2 pozwala programistom perlowym na u¿ywanie biblioteki
interfejsu graficznego Gtk+.

%prep
%setup -q -n %{pnam}-%{version}

# "use Gtk2 '-init'" requires X display; fortunately Gtk2::Stock->lookup
# works without this
%{__perl} -pi -e "s/'-init'//" podifystockitems.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

# force C locale to avoid using localized strings in (en) manuals
LC_ALL=C \
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Gnome2 \
        $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pnam}/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/Gtk2.pm
%dir %{perl_vendorarch}/Gnome2
%dir %{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/auto/Gtk2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/*.so
%dir %{perl_vendorarch}/auto/Gnome2
%{_mandir}/man3/*

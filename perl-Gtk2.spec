# TODO:
# - perl-Gtk2 shouldn't depend on perl-devel (ExtUtils::MakeMaker). create -devel package?
# - review `Unrecognized argument in LIBS ignored: '-pthread'' (from buildlog)
#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
Summary:	Perl interface to the 2.x series of the Gimp Toolkit library
Summary(pl):	Interfejs perlowy do wersji 2.x biblioteki Gimp Toolkit
Name:		perl-Gtk2
Version:	1.101
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{version}.tar.gz
# Source0-md5:	35646a71945e598228957a43bc3b7efe
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-Glib >= 1.101
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.192
Requires:	gtk+2 >= 2.0.0
Requires:	perl-Glib >= 1.101
Obsoletes:	perl-Gnome2-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2 module allows a perl developer to use the GTK+ graphical user
interface library.

%description -l pl
Modu³ Gtk2 pozwala programistom perlowym na u¿ywanie biblioteki
interfejsu graficznego GTK+.

%prep
%setup -q -n %{pdir}-%{version}

# "use Gtk2 '-init'" requires X display; fortunately Gtk2::Stock->lookup
# works without this
%{__perl} -pi -e "s/'-init'//" podifystockitems.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}/{auto/Gnome2,Gnome2} \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Gtk2/Ex

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pdir}/{*,*/*,*/*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%{perl_vendorarch}/Gtk2.pm
%dir %{perl_vendorarch}/Gtk2
%{perl_vendorarch}/Gtk2/*.pm
%dir %{perl_vendorarch}/Gtk2/Gdk
%{perl_vendorarch}/Gtk2/Gdk/*.pm
%{perl_vendorarch}/Gtk2/Install
%dir %{perl_vendorarch}/Gnome2
%dir %{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/auto/Gtk2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/*.so
%dir %{perl_vendorarch}/auto/Gnome2
%dir %{perl_vendorlib}/Gtk2
%dir %{perl_vendorlib}/Gtk2/Ex
%{_mandir}/man3/*

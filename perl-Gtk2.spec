#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
Summary:	Perl interface to the 2.x series of the Gimp Toolkit library
Summary(pl.UTF-8):	Interfejs perlowy do wersji 2.x biblioteki Gimp Toolkit
Name:		perl-Gtk2
# note: versions 1.x[13579]y are unstable, if you want them, please use DEVEL branch
Version:	1.162
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{version}.tar.gz
# Source0-md5:	752b81dcdd0db326e2b0af7c702fc66f
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	pango-devel >= 1:1.18
BuildRequires:	perl-Cairo >= 1.00
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-Glib >= 1.162
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.192
Requires:	gtk+2 >= 2:2.12.0
Requires:	pango >= 1:1.18
Requires:	perl-Cairo >= 1.040
Requires:	perl-Glib >= 1.162
Obsoletes:	perl-Gnome2-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2 module allows a perl developer to use the GTK+ graphical user
interface library.

%description -l pl.UTF-8
Moduł Gtk2 pozwala programistom perlowym na używanie biblioteki
interfejsu graficznego GTK+.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Gtk2/Ex

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/{*,*/*,*/*/*}.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{perl_vendorarch}/Gtk2.pm
%dir %{perl_vendorarch}/Gtk2
%{perl_vendorarch}/Gtk2/*.pm
%dir %{perl_vendorarch}/Gtk2/Gdk
%{perl_vendorarch}/Gtk2/Gdk/*.pm
%{perl_vendorarch}/Gtk2/Install
%dir %{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/auto/Gtk2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/*.so
%dir %{perl_vendorlib}/Gtk2
%dir %{perl_vendorlib}/Gtk2/Ex
%{_mandir}/man3/Gtk2*.3pm*

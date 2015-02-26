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
Version:	1.2492
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{version}.tar.gz
# Source0-md5:	36ac652001392f67bf6b1539b67d5edc
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	pango-devel >= 1:1.18
BuildRequires:	perl-Cairo-devel >= 1.060
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-Glib-devel >= 1.280
BuildRequires:	perl-Pango-devel >= 1.220
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.192
Requires:	gtk+2 >= 2:2.12.0
Requires:	pango >= 1:1.18
Requires:	perl-Cairo >= 1.060
Requires:	perl-Glib >= 1.280
Requires:	perl-Pango >= 1.220
Obsoletes:	perl-Gnome2-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2 module allows a perl developer to use the GTK+ graphical user
interface library.

%description -l pl.UTF-8
Moduł Gtk2 pozwala programistom perlowym na używanie biblioteki
interfejsu graficznego GTK+.

%package devel
Summary:	Development files for Perl Gtk2 bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2 dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	perl-Glib-devel >= 1.280
Requires:	perl-Pango-devel >= 1.220

%description devel
Development files for Perl Gtk2 bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2 dla Perla.

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

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/{*,*/*,*/*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%{perl_vendorarch}/Gtk2.pm
%dir %{perl_vendorarch}/Gtk2
%{perl_vendorarch}/Gtk2/Helper.pm
%{perl_vendorarch}/Gtk2/Pango.pm
%{perl_vendorarch}/Gtk2/SimpleList.pm
%{perl_vendorarch}/Gtk2/SimpleMenu.pm
%{perl_vendorarch}/Gtk2/TestHelper.pm
%dir %{perl_vendorarch}/Gtk2/Gdk
%{perl_vendorarch}/Gtk2/Gdk/Keysyms.pm
%dir %{perl_vendorarch}/auto/Gtk2
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/Gtk2.so
%dir %{perl_vendorlib}/Gtk2
%dir %{perl_vendorlib}/Gtk2/Ex
%{_mandir}/man3/Gtk2.3pm*
%{_mandir}/man3/Gtk2::AboutDialog.3pm*
%{_mandir}/man3/Gtk2::AccelGroup.3pm*
%{_mandir}/man3/Gtk2::AccelLabel.3pm*
%{_mandir}/man3/Gtk2::AccelMap.3pm*
%{_mandir}/man3/Gtk2::Accelerator.3pm*
%{_mandir}/man3/Gtk2::Action.3pm*
%{_mandir}/man3/Gtk2::ActionGroup.3pm*
%{_mandir}/man3/Gtk2::Activatable.3pm*
%{_mandir}/man3/Gtk2::Adjustment.3pm*
%{_mandir}/man3/Gtk2::Alignment.3pm*
%{_mandir}/man3/Gtk2::Arrow.3pm*
%{_mandir}/man3/Gtk2::AspectFrame.3pm*
%{_mandir}/man3/Gtk2::Assistant.3pm*
%{_mandir}/man3/Gtk2::Bin.3pm*
%{_mandir}/man3/Gtk2::BindingSet.3pm*
%{_mandir}/man3/Gtk2::Box.3pm*
%{_mandir}/man3/Gtk2::Buildable.3pm*
%{_mandir}/man3/Gtk2::Buildable::ParseContext.3pm*
%{_mandir}/man3/Gtk2::Builder.3pm*
%{_mandir}/man3/Gtk2::Button.3pm*
%{_mandir}/man3/Gtk2::ButtonBox.3pm*
%{_mandir}/man3/Gtk2::Calendar.3pm*
%{_mandir}/man3/Gtk2::CellEditable.3pm*
%{_mandir}/man3/Gtk2::CellLayout.3pm*
%{_mandir}/man3/Gtk2::CellRenderer.3pm*
%{_mandir}/man3/Gtk2::CellRendererAccel.3pm*
%{_mandir}/man3/Gtk2::CellRendererCombo.3pm*
%{_mandir}/man3/Gtk2::CellRendererPixbuf.3pm*
%{_mandir}/man3/Gtk2::CellRendererProgress.3pm*
%{_mandir}/man3/Gtk2::CellRendererSpin.3pm*
%{_mandir}/man3/Gtk2::CellRendererSpinner.3pm*
%{_mandir}/man3/Gtk2::CellRendererText.3pm*
%{_mandir}/man3/Gtk2::CellRendererToggle.3pm*
%{_mandir}/man3/Gtk2::CellView.3pm*
%{_mandir}/man3/Gtk2::CheckButton.3pm*
%{_mandir}/man3/Gtk2::CheckMenuItem.3pm*
%{_mandir}/man3/Gtk2::Clipboard.3pm*
%{_mandir}/man3/Gtk2::ColorButton.3pm*
%{_mandir}/man3/Gtk2::ColorSelection.3pm*
%{_mandir}/man3/Gtk2::ColorSelectionDialog.3pm*
%{_mandir}/man3/Gtk2::Combo.3pm*
%{_mandir}/man3/Gtk2::ComboBox.3pm*
%{_mandir}/man3/Gtk2::ComboBoxEntry.3pm*
%{_mandir}/man3/Gtk2::Container.3pm*
%{_mandir}/man3/Gtk2::Curve.3pm*
%{_mandir}/man3/Gtk2::Dialog.3pm*
%{_mandir}/man3/Gtk2::Drag.3pm*
%{_mandir}/man3/Gtk2::DrawingArea.3pm*
%{_mandir}/man3/Gtk2::Editable.3pm*
%{_mandir}/man3/Gtk2::Entry.3pm*
%{_mandir}/man3/Gtk2::EntryBuffer.3pm*
%{_mandir}/man3/Gtk2::EntryCompletion.3pm*
%{_mandir}/man3/Gtk2::EventBox.3pm*
%{_mandir}/man3/Gtk2::Expander.3pm*
%{_mandir}/man3/Gtk2::FileChooser.3pm*
%{_mandir}/man3/Gtk2::FileChooserButton.3pm*
%{_mandir}/man3/Gtk2::FileChooserDialog.3pm*
%{_mandir}/man3/Gtk2::FileChooserWidget.3pm*
%{_mandir}/man3/Gtk2::FileFilter.3pm*
%{_mandir}/man3/Gtk2::FileSelection.3pm*
%{_mandir}/man3/Gtk2::Fixed.3pm*
%{_mandir}/man3/Gtk2::FontButton.3pm*
%{_mandir}/man3/Gtk2::FontSelection.3pm*
%{_mandir}/man3/Gtk2::FontSelectionDialog.3pm*
%{_mandir}/man3/Gtk2::Frame.3pm*
%{_mandir}/man3/Gtk2::GC.3pm*
%{_mandir}/man3/Gtk2::GammaCurve.3pm*
%{_mandir}/man3/Gtk2::Gdk*.3pm*
%{_mandir}/man3/Gtk2::HBox.3pm*
%{_mandir}/man3/Gtk2::HButtonBox.3pm*
%{_mandir}/man3/Gtk2::HPaned.3pm*
%{_mandir}/man3/Gtk2::HRuler.3pm*
%{_mandir}/man3/Gtk2::HSV.3pm*
%{_mandir}/man3/Gtk2::HScale.3pm*
%{_mandir}/man3/Gtk2::HScrollbar.3pm*
%{_mandir}/man3/Gtk2::HSeparator.3pm*
%{_mandir}/man3/Gtk2::HandleBox.3pm*
%{_mandir}/man3/Gtk2::Helper.3pm*
%{_mandir}/man3/Gtk2::IMContext.3pm*
%{_mandir}/man3/Gtk2::IMContextSimple.3pm*
%{_mandir}/man3/Gtk2::IMMulticontext.3pm*
%{_mandir}/man3/Gtk2::IconFactory.3pm*
%{_mandir}/man3/Gtk2::IconInfo.3pm*
%{_mandir}/man3/Gtk2::IconSet.3pm*
%{_mandir}/man3/Gtk2::IconSize.3pm*
%{_mandir}/man3/Gtk2::IconSource.3pm*
%{_mandir}/man3/Gtk2::IconTheme.3pm*
%{_mandir}/man3/Gtk2::IconView.3pm*
%{_mandir}/man3/Gtk2::Image.3pm*
%{_mandir}/man3/Gtk2::ImageMenuItem.3pm*
%{_mandir}/man3/Gtk2::InfoBar.3pm*
%{_mandir}/man3/Gtk2::InputDialog.3pm*
%{_mandir}/man3/Gtk2::Invisible.3pm*
%{_mandir}/man3/Gtk2::Item.3pm*
%{_mandir}/man3/Gtk2::ItemFactory.3pm*
%{_mandir}/man3/Gtk2::Label.3pm*
%{_mandir}/man3/Gtk2::Layout.3pm*
%{_mandir}/man3/Gtk2::LinkButton.3pm*
%{_mandir}/man3/Gtk2::List.3pm*
%{_mandir}/man3/Gtk2::ListItem.3pm*
%{_mandir}/man3/Gtk2::ListStore.3pm*
%{_mandir}/man3/Gtk2::Menu.3pm*
%{_mandir}/man3/Gtk2::MenuBar.3pm*
%{_mandir}/man3/Gtk2::MenuItem.3pm*
%{_mandir}/man3/Gtk2::MenuShell.3pm*
%{_mandir}/man3/Gtk2::MenuToolButton.3pm*
%{_mandir}/man3/Gtk2::MessageDialog.3pm*
%{_mandir}/man3/Gtk2::Misc.3pm*
%{_mandir}/man3/Gtk2::Notebook.3pm*
%{_mandir}/man3/Gtk2::Object.3pm*
%{_mandir}/man3/Gtk2::OffscreenWindow.3pm*
%{_mandir}/man3/Gtk2::OptionMenu.3pm*
%{_mandir}/man3/Gtk2::Orientable.3pm*
%{_mandir}/man3/Gtk2::PageSetup.3pm*
%{_mandir}/man3/Gtk2::Paned.3pm*
%{_mandir}/man3/Gtk2::Pango*.3pm*
%{_mandir}/man3/Gtk2::PaperSize.3pm*
%{_mandir}/man3/Gtk2::Plug.3pm*
%{_mandir}/man3/Gtk2::Print.3pm*
%{_mandir}/man3/Gtk2::PrintContext.3pm*
%{_mandir}/man3/Gtk2::PrintOperation.3pm*
%{_mandir}/man3/Gtk2::PrintOperationPreview.3pm*
%{_mandir}/man3/Gtk2::PrintSettings.3pm*
%{_mandir}/man3/Gtk2::ProgressBar.3pm*
%{_mandir}/man3/Gtk2::RadioAction.3pm*
%{_mandir}/man3/Gtk2::RadioButton.3pm*
%{_mandir}/man3/Gtk2::RadioMenuItem.3pm*
%{_mandir}/man3/Gtk2::RadioToolButton.3pm*
%{_mandir}/man3/Gtk2::Range.3pm*
%{_mandir}/man3/Gtk2::Rc.3pm*
%{_mandir}/man3/Gtk2::RcStyle.3pm*
%{_mandir}/man3/Gtk2::RecentAction.3pm*
%{_mandir}/man3/Gtk2::RecentChooser.3pm*
%{_mandir}/man3/Gtk2::RecentChooserDialog.3pm*
%{_mandir}/man3/Gtk2::RecentChooserMenu.3pm*
%{_mandir}/man3/Gtk2::RecentChooserWidget.3pm*
%{_mandir}/man3/Gtk2::RecentFilter.3pm*
%{_mandir}/man3/Gtk2::RecentInfo.3pm*
%{_mandir}/man3/Gtk2::RecentManager.3pm*
%{_mandir}/man3/Gtk2::Requisition.3pm*
%{_mandir}/man3/Gtk2::Ruler.3pm*
%{_mandir}/man3/Gtk2::Scale.3pm*
%{_mandir}/man3/Gtk2::ScaleButton.3pm*
%{_mandir}/man3/Gtk2::Scrollbar.3pm*
%{_mandir}/man3/Gtk2::ScrolledWindow.3pm*
%{_mandir}/man3/Gtk2::Selection.3pm*
%{_mandir}/man3/Gtk2::SelectionData.3pm*
%{_mandir}/man3/Gtk2::Separator.3pm*
%{_mandir}/man3/Gtk2::SeparatorMenuItem.3pm*
%{_mandir}/man3/Gtk2::SeparatorToolItem.3pm*
%{_mandir}/man3/Gtk2::SimpleList.3pm*
%{_mandir}/man3/Gtk2::SimpleMenu.3pm*
%{_mandir}/man3/Gtk2::SizeGroup.3pm*
%{_mandir}/man3/Gtk2::Socket.3pm*
%{_mandir}/man3/Gtk2::SpinButton.3pm*
%{_mandir}/man3/Gtk2::Spinner.3pm*
%{_mandir}/man3/Gtk2::StatusIcon.3pm*
%{_mandir}/man3/Gtk2::Statusbar.3pm*
%{_mandir}/man3/Gtk2::Stock.3pm*
%{_mandir}/man3/Gtk2::Style.3pm*
%{_mandir}/man3/Gtk2::Table.3pm*
%{_mandir}/man3/Gtk2::TargetEntry.3pm*
%{_mandir}/man3/Gtk2::TargetList.3pm*
%{_mandir}/man3/Gtk2::TearoffMenuItem.3pm*
%{_mandir}/man3/Gtk2::TextAttributes.3pm*
%{_mandir}/man3/Gtk2::TextBuffer.3pm*
%{_mandir}/man3/Gtk2::TextChildAnchor.3pm*
%{_mandir}/man3/Gtk2::TextIter.3pm*
%{_mandir}/man3/Gtk2::TextMark.3pm*
%{_mandir}/man3/Gtk2::TextTag.3pm*
%{_mandir}/man3/Gtk2::TextTagTable.3pm*
%{_mandir}/man3/Gtk2::TextView.3pm*
%{_mandir}/man3/Gtk2::ToggleAction.3pm*
%{_mandir}/man3/Gtk2::ToggleButton.3pm*
%{_mandir}/man3/Gtk2::ToggleToolButton.3pm*
%{_mandir}/man3/Gtk2::ToolButton.3pm*
%{_mandir}/man3/Gtk2::ToolItem.3pm*
%{_mandir}/man3/Gtk2::ToolItemGroup.3pm*
%{_mandir}/man3/Gtk2::ToolPalette.3pm*
%{_mandir}/man3/Gtk2::ToolShell.3pm*
%{_mandir}/man3/Gtk2::Toolbar.3pm*
%{_mandir}/man3/Gtk2::Tooltip.3pm*
%{_mandir}/man3/Gtk2::Tooltips.3pm*
%{_mandir}/man3/Gtk2::TreeDragDest.3pm*
%{_mandir}/man3/Gtk2::TreeDragSource.3pm*
%{_mandir}/man3/Gtk2::TreeIter.3pm*
%{_mandir}/man3/Gtk2::TreeModel.3pm*
%{_mandir}/man3/Gtk2::TreeModelFilter.3pm*
%{_mandir}/man3/Gtk2::TreeModelSort.3pm*
%{_mandir}/man3/Gtk2::TreePath.3pm*
%{_mandir}/man3/Gtk2::TreeRowReference.3pm*
%{_mandir}/man3/Gtk2::TreeSelection.3pm*
%{_mandir}/man3/Gtk2::TreeSortable*.3pm*
%{_mandir}/man3/Gtk2::TreeStore.3pm*
%{_mandir}/man3/Gtk2::TreeView.3pm*
%{_mandir}/man3/Gtk2::TreeViewColumn.3pm*
%{_mandir}/man3/Gtk2::UIManager.3pm*
%{_mandir}/man3/Gtk2::VBox.3pm*
%{_mandir}/man3/Gtk2::VButtonBox.3pm*
%{_mandir}/man3/Gtk2::VPaned.3pm*
%{_mandir}/man3/Gtk2::VRuler.3pm*
%{_mandir}/man3/Gtk2::VScale.3pm*
%{_mandir}/man3/Gtk2::VScrollbar.3pm*
%{_mandir}/man3/Gtk2::VSeparator.3pm*
%{_mandir}/man3/Gtk2::Viewport.3pm*
%{_mandir}/man3/Gtk2::VolumeButton.3pm*
%{_mandir}/man3/Gtk2::Widget.3pm*
%{_mandir}/man3/Gtk2::Window.3pm*
%{_mandir}/man3/Gtk2::WindowGroup.3pm*
%{_mandir}/man3/Gtk2::api.3pm*
%{_mandir}/man3/Gtk2::enums.3pm*
%{_mandir}/man3/Gtk2::index.3pm*
%{_mandir}/man3/Gtk2::main.3pm*
%{_mandir}/man3/Gtk2::version.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/CodeGen.pm
%{perl_vendorarch}/Gtk2/Install
%{_mandir}/man3/Gtk2::CodeGen.3pm*
%{_mandir}/man3/Gtk2::devel.3pm*

Name:    cinnamon-screensaver
Version: 5.2.0
Release: 3
Summary: Cinnamon Screensaver
License: GPLv2+ and LGPLv2+
URL:     https://github.com/linuxmint/%{name}
Source0: https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch: %{ix86}

BuildRequires: meson
BuildRequires: intltool
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: gobject-introspection-devel
BuildRequires: pam-devel
BuildRequires: python3-devel
BuildRequires: gtk3-devel
BuildRequires: libXext-devel
BuildRequires: desktop-file-utils

Requires: cinnamon-desktop%{?_isa} >= 5.2.0
Requires: cinnamon-translations >= 5.2.0
Requires: accountsservice-libs%{?_isa}
Requires: libgnomekbd%{?_isa}
Requires: python3-gobject%{?_isa}
Requires: python3-setproctitle%{?_isa}
Requires: python3-xapp
Requires: python3-xapps-overrides%{?_isa}
Requires: xapps%{?_isa}

# since we use it, and pam spams the log if a module is missing
Requires: gnome-keyring-pam%{?_isa}

Obsoletes: cinnamon-screensaver-unsupported < %{version}

%description
cinnamon-screensaver is a screen saver and locker.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install                                     \
  --delete-original                                      \
  --remove-only-show-in=Xfce                             \
  --dir %{buildroot}%{_datadir}/applications             \
  %{buildroot}%{_datadir}/applications/org.cinnamon.ScreenSaver.desktop

# Fix rpmlint errors
for file in %{buildroot}%{_datadir}/cinnamon-screensaver/{dbusdepot,util,widgets}/*.py; do
chmod a+x $file
done
for file in %{buildroot}%{_datadir}/cinnamon-screensaver/*.py; do
chmod a+x $file
done
chmod a-x %{buildroot}%{_datadir}/cinnamon-screensaver/{dbusdepot,util,widgets}/__init__.py
chmod a-x %{buildroot}%{_datadir}/cinnamon-screensaver/{__init__,config}.py
chmod a+x %{buildroot}%{_datadir}/cinnamon-screensaver/pamhelper/authClient.py

# Delete development files
rm %{buildroot}%{_libdir}/libcscreensaver.so
rm %{buildroot}%{_libdir}/pkgconfig/cscreensaver.pc
rm %{buildroot}%{_datadir}/gir-1.0/CScreensaver-1.0.gir

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README.md
%license COPYING COPYING.LIB
%config(noreplace) %{_sysconfdir}/pam.d/cinnamon-screensaver
%{_bindir}/cinnamon-screensaver*
%{_bindir}/cinnamon-unlock-desktop
%{_datadir}/applications/org.cinnamon.ScreenSaver.desktop
%{_datadir}/cinnamon-screensaver/
%{_datadir}/dbus-1/services/org.cinnamon.ScreenSaver.service
%{_datadir}/icons/hicolor/scalable/*/*
%{_libexecdir}/cinnamon-screensaver-pam-helper
%{_libexecdir}/cs-backup-locker
%{_libdir}/libcscreensaver.so.*
%{_libdir}/girepository-1.0/CScreensaver-1.0.typelib

%changelog
* Mon Jul 25 2022 wenlong ding <wenlong.ding@turbolinux.com.cn> - 5.2.0-3
- Add Requires: python3-xapp
* Mon May 27 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.0-2
- delete Requires: python3-xapp

* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.0-1
- Initial Packaging

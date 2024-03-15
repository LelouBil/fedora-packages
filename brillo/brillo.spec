%global forgeurl https://gitlab.com/cameronnemo/brillo
%global version 1.4.12
%global tag v%{version}
%forgemeta

Name:           brillo
Version:        %{version}
Release:        %autorelease
Summary:        Controls the brightness of backlight and LED devices on Linux
URL:            %{forgeurl}
Source:         %{forgesource}
License:        GPL-3.0-only AND 0BSD

BuildRequires:  gcc
BuildRequires:  bash
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  go-md2man
BuildRequires:  systemd-rpm-macros
BuildRequires:  valgrind

%description
brillo controls the brightness of backlight and LED devices on Linux.

Notable features include:

- Automatic best controller detection
- Smooth transitions and natural brightness adjustments
- Ability to save and restore brightness across boots
- Directly using sysfs to set brightness without relying on X
- Unprivileged access with no new setuid binaries
- Containment with AppArmor

%prep
%forgesetup

%build
%make_build

%install
%make_install install.man install.polkit

%check
env BRILLO_BIN=build/brillo sh test.sh

%files
%license LICENSE.0BSD
%license LICENSE.GPL-3.0-only
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/polkit-1/actions/com.gitlab.CameronNemo.brillo.policy
%{_udevrulesdir}/92-com.gitlab.CameronNemo.brillo.rules

%changelog
%autochangelog
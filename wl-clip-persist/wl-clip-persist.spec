%global forgeurl https://github.com/Linus789/wl-clip-persist
%global commit 6ba11a2aa295d780f0b2e8f005cf176601d153b0
%forgemeta
# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

%global crate wl-clip-persist

Name:           wl-clip-persist
Version:        0.3.1
Release:        %autorelease 
Summary:        Keep Wayland clipboard even after programs close

SourceLicense:  None
# FIXME: paste output of %%cargo_license_summary here
License:        MIT
# LICENSE.dependencies contains a full license breakdown

URL:            %{forgeurl} 
Source:         %{forgesource}
Patch0:         upgrade-fancy-regex.patch
BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  help2man
%global _description %{expand:
Keep Wayland clipboard even after programs close.}

%description %{_description}

%prep
%forgeautosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%{__mkdir} -p %{buildroot}%{_mandir}/man1
help2man -s 1 -n "%{summary}" -N target/release/%{name} -o %{buildroot}%{_mandir}/man1/%{name}.1


%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/wl-clip-persist

%changelog
%autochangelog
# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate tokio-pipe

Name:           rust-tokio-pipe
Version:        0.2.12
Release:        %autorelease
Summary:        Asynchronous pipe(2) library using tokio

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-pipe
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  python3
BuildRequires:  python-unversioned-command

%global _description %{expand:
Asynchronous pipe(2) library using tokio.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

#%if %{with check}
#%check
#%cargo_test
#%endif

%changelog
%autochangelog

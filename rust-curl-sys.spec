# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate curl-sys

Name:           rust-%{crate}
Version:        0.4.25
Release:        2%{?dist}
Summary:        Native bindings to the libcurl library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/curl-sys
Source:         %{crates_source}
# Initial patched metadata
# * No windows
# * libnghttp2-sys is only needed for bundled curl
Patch0:         curl-sys-fix-metadata.diff
Patch1:         curl-sys-remove-libnghttp2-sys.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Native bindings to the libcurl library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libcurl)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages
which use "http2" feature of "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+openssl-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-sys-devel %{_description}

This package contains library source intended for building other packages
which use "openssl-sys" feature of "%{crate}" crate.

%files       -n %{name}+openssl-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+spnego-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spnego-devel %{_description}

This package contains library source intended for building other packages
which use "spnego" feature of "%{crate}" crate.

%files       -n %{name}+spnego-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ssl-devel %{_description}

This package contains library source intended for building other packages
which use "ssl" feature of "%{crate}" crate.

%files       -n %{name}+ssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# No bundled deps
rm -vrf curl
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libcurl)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.4.25-1
- Update to 0.4.25

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.4.24-1
- Update to 0.4.24

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 12:41:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.19-1
- Update to 0.4.19

* Thu May 09 2019 Josh Stone <jistone@redhat.com> - 0.4.18-1
- Update to 0.4.18

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.17-1
- Update to 0.4.17

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Josh Stone <jistone@redhat.com> - 0.4.16-1
- Update to 0.4.16

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.15-2
- Run tests in infrastructure

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.4.15-1
- Update to 0.4.15
- Adapt to new packaging

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.13-2
- Adapt to new packaging

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 0.4.13-1
- Update to 0.4.13

* Thu Sep 20 2018 Josh Stone <jistone@redhat.com> - 0.4.12-1
- Update to 0.4.12

* Tue Sep 18 2018 Josh Stone <jistone@redhat.com> - 0.4.11-1
- Update to 0.4.11

* Fri Sep 14 2018 Josh Stone <jistone@redhat.com> - 0.4.10-1
- Update to 0.4.10

* Thu Sep 13 2018 Josh Stone <jistone@redhat.com> - 0.4.9-1
- Update to 0.4.9

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.4.8-1
- Update to 0.4.8

* Tue Jul 31 2018 Josh Stone <jistone@redhat.com> - 0.4.7-1
- Update to 0.4.7

* Sat Jul 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Mon Apr 16 2018 Josh Stone <jistone@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-2
- Rebuild for rust-packaging v5

* Sun Nov 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-1
- Initial package

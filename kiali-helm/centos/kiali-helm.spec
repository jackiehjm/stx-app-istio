# Build variables
%global helm_folder /usr/lib/helm

Summary: Kiali helm charts
Name: kiali-helm
Version: 1.45.0 
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: unknown

Source0: helm-charts-kiali-%{version}.tar.gz
Source1: repositories.yaml
Source2: index.yaml
Source3: Makefile

BuildArch:     noarch

BuildRequires: helm

%description
StarlingX Kiali Helm Charts

%prep
%setup -n helm-charts-kiali

%build
echo $PATH
make build-helm-charts

%install
install -d -m 755 ${RPM_BUILD_ROOT}%{helm_folder}
install -p -D -m 755 _output/charts/*.tgz ${RPM_BUILD_ROOT}%{helm_folder}


%files
%defattr(-,root,root,-)
%{helm_folder}/*

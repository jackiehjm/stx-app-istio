# Application tunables (maps to metadata)
%global app_name istio 
%global helm_repo stx-platform

# Install location
%global app_folder /usr/local/share/applications/helm

# Build variables
%global helm_folder /usr/lib/helm

Summary: StarlingX Istio Helm Charts
Name: stx-istio-helm
Version: 1.0
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: unknown

Source0: helm-charts-istio-%{version}.tar.gz

BuildArch: noarch

BuildRequires: helm
BuildRequires: chartmuseum
BuildRequires: istio-helm
BuildRequires: kiali-helm
BuildRequires: python-k8sapp-istio
BuildRequires: python-k8sapp-istio-wheels
Requires: kiali-helm

%description
StarlingX Istio Helm Charts

%package fluxcd
Summary: StarlingX Istio Application FluxCD Helm Charts
Group: base
License: Apache-2.0

%description fluxcd
StarlingX Istio Application FluxCD Helm Charts

%prep
%setup -n helm-charts-istio-%{version}

%build
# Create a chart tarball compliant with sysinv kube-app.py
%define app_staging %{_builddir}/staging
%define app_tarball_fluxcd %{app_name}-fluxcd-%{version}-%{tis_patch_ver}.tgz

# Setup staging
cd %{_builddir}/helm-charts-istio-%{version}
mkdir -p %{app_staging}
cp files/metadata.yaml %{app_staging}
cp -R fluxcd-manifests %{app_staging}/
mkdir -p %{app_staging}/charts
cp %{helm_folder}/*.tgz %{app_staging}/charts
cd %{app_staging}

# Populate metadata
sed -i 's/@APP_NAME@/%{app_name}/g' %{app_staging}/metadata.yaml
sed -i 's/@APP_VERSION@/%{version}-%{tis_patch_ver}/g' %{app_staging}/metadata.yaml
sed -i 's/@HELM_REPO@/%{helm_repo}/g' %{app_staging}/metadata.yaml

# Copy the plugins: installed in the buildroot
mkdir -p %{app_staging}/plugins
cp /plugins/%{app_name}/*.whl %{app_staging}/plugins

find . -type f ! -name '*.md5' -print0 | xargs -0 md5sum > checksum.md5
tar -zcf %{_builddir}/%{app_tarball_fluxcd} -C %{app_staging}/ .

# Cleanup staging
rm -fr %{app_staging}

%install
install -d -m 755 %{buildroot}/%{app_folder}
install -p -D -m 755 %{_builddir}/%{app_tarball_fluxcd} %{buildroot}/%{app_folder}

%files fluxcd
%defattr(-,root,root,-)
%{app_folder}/%{app_tarball_fluxcd}

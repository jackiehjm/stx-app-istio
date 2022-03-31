# Build variables
%global helm_folder /usr/lib/helm

Summary: Istio helm charts
Name: istio-helm
Version: 1.13.2
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: unknown

Source0: helm-charts-istio-%{version}.tar.gz
Source1: repositories.yaml
Source2: index.yaml
Source3: Makefile

BuildArch:     noarch

BuildRequires: helm
BuildRequires: chartmuseum

%description
StarlingX Istio Helm Charts

%prep
%setup -n helm-charts-istio

#%patch01 -p1

%build
# Host a server for the charts
chartmuseum --debug --port=8879 --context-path='/charts' --storage="local" --storage-local-rootdir="." &
sleep 2
helm repo add local http://localhost:8879/charts

# Create the tgz files
cp %{SOURCE3} manifests/charts
cd manifests/charts

sed -i -e '/appVersion/ s/:.*$/: %{version}/' istio-operator/Chart.yaml
sed -i -e '/version/ s/:.*$/: %{version}/' istio-operator/Chart.yaml

make istio-operator
# mv istio-operator-*.tgz istio-operator-%{version}.tgz
 
cd -

# terminate helm server (the last backgrounded task)
kill %1

%install
install -d -m 755 ${RPM_BUILD_ROOT}%{helm_folder}
install -p -D -m 755 manifests/charts/*.tgz ${RPM_BUILD_ROOT}%{helm_folder}

%files
%defattr(-,root,root,-)
%{helm_folder}/*

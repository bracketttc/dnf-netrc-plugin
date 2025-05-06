Name:           dnf-netrc-plugin
Version:        0.1.0
Release:        1%{?dist}
Summary:        DNF plugin for netrc authentication

BuildArch:      noarch
License:        MIT
URL:            https://github.com/bracketttc/dnf-netrc-plugin.git
Source0:        https://github.com/bracketttc/dnf-netrc-plugin/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-rpm-macros
Requires:       dnf

%description
DNF plugin to user .netrc credentials to authenticate to repositories.


%prep
%setup -q

%build

%install
install -D -m 644 -t %{buildroot}/%{python3_sitelib}/dnf-plugins netrc_plugin.py

%files
%license LICENSE
%{python3_sitelib}/dnf-plugins/netrc_plugin.py
%{python3_sitelib}/dnf-plugins/__pycache__/netrc_plugin.*.pyc


%changelog
* Mon May 05 2025 Timothy Brackett <brackett.tc@gmail.com> - 0.1.0-1
- Initial release

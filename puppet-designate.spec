# add guard for OSP packages not carried
%global rhosp 0
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-designate

Name:                   puppet-designate
Version:                15.6.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Designate
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-designate

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-stdlib
Requires:               puppet-dns
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 2.7.0

%if 0%{rhosp} == 0
Requires:               puppet-powerdns
%endif

%description
Installs and configures OpenStack Designate (DNS Services).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/designate/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/designate/



%files
%{_datadir}/openstack-puppet/modules/designate/


%changelog
* Wed Jun 16 2021 RDO <dev@lists.rdoproject.org> 15.6.0-1
- Update to 15.6.0

* Fri Oct 11 2019 RDO <dev@lists.rdoproject.org> 15.5.0-1
- Update to 15.5.0

* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0

* Thu Feb 02 2017 Alfredo Moralejo <amoralej@redhat.com> 9.5.0-1
- Update to 9.5.0



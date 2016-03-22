Name:           slurm-plugins-lua
Version:        1.0
Release:        1%{?dist}
Summary:        Slurm configuration for plugins

Group:          Applications/System
License:        Apache 2.0
URL:            https://github.com/djw8605/slurm-plugin-base
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       slurm
Requires:       lua
Requires:       lua-linuxsys

%description
Slurm configuration for plugins

%prep
%setup -q


%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/slurm
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/slurm/plugstack.conf.d
install src/plugstack.conf $RPM_BUILD_ROOT/%{_sysconfdir}/slurm/
install src/99-lua $RPM_BUILD_ROOT/%{_sysconfdir}/slurm/plugstack.conf.d/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sysconfdir}/slurm/*



%changelog
* Tue Mar 22 2016 Derek Weitzel <djw8605@gmail.com> - 1.0-1
- Initial creation of RPM


%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# Disabled tests 
# circular deps needs event-stream which needs this
%global enable_tests 0
%global module_name stream-combiner

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        0.2.1
Release:        4%{?dist}
Summary:        Turn a pipeline into a single stream 

License:        MIT
URL:            https://github.com/dominictarr/stream-combiner
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tape)
BuildRequires:  %{?scl_prefix}npm(event-stream)
%endif

%description
Turn a pipeline into a single stream. Combine returns a stream that writes
to the first stream and reads from the last stream. 

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
set -e; for t in test/*.js; do node $t; done
%endif

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 0.2.1-4
- Invoke find_provides_and_requires macro

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 0.2.1-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.2.1-1
- Initial packaging

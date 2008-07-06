Summary:	Library for writing IRC clients and servers
Name:		ruby-net-irc
Version:	0.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/39481/net-irc-%{version}.tgz
# Source0-md5:	24bc92d6825eba0a0f223e918df63e9f
URL:		http://rubyforge.org/projects/lowreal
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for writing IRC clients and servers.

%prep
%setup -q -n net-irc-%{version}

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%{ruby_rubylibdir}/net/irc
%{ruby_rubylibdir}/net/irc.rb

%define name    py2play
%define oname   Py2Play
%define version 0.1.9
%define release %mkrel 6

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Url:            http://oomadness.tuxfamily.org/en/py2play
Source0:        %{oname}-%{version}.tar.bz2
Group:          Development/Python
Summary:        A peer-to-peer network game engine
BuildRequires:  python-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A Peer To Peer network game engine.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/lib/python2*/site-packages/%{name}
/usr/lib/python2*/site-packages/*.egg-info



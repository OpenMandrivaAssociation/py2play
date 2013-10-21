%define oname   Py2Play

Name:           py2play
Version:        0.1.10
Release:        1
License:        GPL
Url:            http://oomadness.tuxfamily.org/en/py2play
Source0:        %{oname}-%{version}.tar.gz
Group:          Development/Python
Summary:        A peer-to-peer network game engine
BuildRequires:  python-devel
BuildArch:      noarch

%description
A Peer To Peer network game engine.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%clean

%files
%doc README
/usr/lib/python2*/site-packages/%{name}
/usr/lib/python2*/site-packages/*.egg-info


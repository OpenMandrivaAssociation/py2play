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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.9-6mdv2010.0
+ Revision: 441969
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.1.9-5mdv2009.1
+ Revision: 325848
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.1.9-4mdv2009.0
+ Revision: 259385
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.9-3mdv2009.0
+ Revision: 247250
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.9-1mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Dec 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.1.9-1mdv2007.0
+ Revision: 90197
- New version 0.1.9
  fix x86_64 build
  %%mkrel
- Import py2play


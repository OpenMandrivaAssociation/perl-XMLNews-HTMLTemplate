%define module 	XMLNews-HTMLTemplate
%define version 0.01
%define release 13

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{module}
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel 
Requires:	perl 
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	perl(XMLNews::Meta)
Buildarch:	noarch

%description
%{module} - module designed to create template-based HTML pages 
using news documents in XMLNews-Meta and XMLNews-Story format

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/XMLNews
%{_mandir}/*/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.01-11mdv2010.0
+ Revision: 430664
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-10mdv2009.0
+ Revision: 242253
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.01-8mdv2008.0
+ Revision: 64202
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-7mdv2008.0
+ Revision: 23514
- rebuild


* Fri May 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-6mdk
- Fix Build
- Fix BuildRequires
- use mkrel

* Tue Jun 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-5mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-4mdk
- rebuild for new auto{prov,req}


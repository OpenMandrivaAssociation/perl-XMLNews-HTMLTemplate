%define module 	XMLNews-HTMLTemplate
%define version 0.01
%define release %mkrel 11

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
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

%define upstream_name    Net-DNS-Resolver-Mock
%define upstream_version 1.20171219

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Mock a DNS Resolver object for testing
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::DNS::Packet)
BuildRequires: perl(Net::DNS::Question)
BuildRequires: perl(Net::DNS::Resolver)
BuildRequires: perl(Net::DNS::ZoneFile)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
A subclass of Net::DNS::Resolver which parses a zonefile for it's data
source. Primarily for use in testing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%make_install

%files
%doc LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

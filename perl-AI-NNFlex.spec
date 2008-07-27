#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	NNFlex
Summary:	AI::NNFlex - A base class for implementing neural networks
Summary(pl.UTF-8):	AI::NNFlex - klasa bazowa do implementowania sieci neuronowych
Name:		perl-AI-NNFlex
Version:	0.24
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CC/CCOLBOURN/ai-nnflex/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d192b7c209ccafbca88d6ac6048b677
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Matrix
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NNFlex is a base class for constructing your own neural network
modules. To implement a neural network, start with the documentation
for AI::NNFlex::Backprop, included in this distribution.

%description -l pl.UTF-8
AI::NNFlex to klasa bazowa do konstruowania własnych modułów sieci
neuronowych. Aby zaimplementować sieć neuronową, najlepiej zacząć od
dokumentacji AI::NNFlex::Backprop dołączonej do tego modułu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	MAN3PODS= \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README.txt TODO
%{perl_vendorlib}/AI/*.pm
%{perl_vendorlib}/AI/NNFlex
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

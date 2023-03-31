Name:		texlive-semproc
Version:	37568
Release:	2
Summary:	Seminar proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semproc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semproc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semproc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semproc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides functionality for typesetting seminar
proceedings based on KOMA-Script's scrreprt class and etoc. It
offers an alternative to \chapter that typesets the speaker and
if necessary the typist of the notes for the talk in question.
Moreover, the class provides two types of table of contents. A
global table of contents showing only the talks of the seminar
and the respective speakers and a local table of contents for
each talk showing the sections and subsections of the
respective talk.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/semproc
%{_texmfdistdir}/tex/latex/semproc
%doc %{_texmfdistdir}/doc/latex/semproc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

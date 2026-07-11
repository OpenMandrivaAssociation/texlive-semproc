%global tl_name semproc
%global tl_revision 37568

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Seminar proceedings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/semproc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semproc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semproc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semproc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides functionality for typesetting seminar proceedings
based on KOMA-Script's scrreprt class and etoc. It offers an alternative
to \chapter that typesets the speaker and if necessary the typist of the
notes for the talk in question. Moreover, the class provides two types
of table of contents. A global table of contents showing only the talks
of the seminar and the respective speakers and a local table of contents
for each talk showing the sections and subsections of the respective
talk.


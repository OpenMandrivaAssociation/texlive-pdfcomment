%global tl_name pdfcomment
%global tl_revision 79390

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0b
Release:	%{tl_revision}.1
Summary:	A user-friendly interface to pdf annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfcomment
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows to add text, line, square, circle, text markup
annotations and tooltips to a PDF. Support of PDF annotations by PDF
viewers may vary. The package is tagging compatible.


Name:		texlive-pdfcomment
Version:	49047
Release:	2
Summary:	A user-friendly interface to pdf annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfcomment
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For a long time pdfLaTeX has offered the command \pdfannot for
inserting arbitrary PDF annotations. However, the command is
presented in a form where additional knowledge of the
definition of the PDF format is indispensable. This package is
an answer to the - occasional - questions in newsgroups, about
how one could use the comment function of Adobe Reader. At
least for the writer of LaTeX code, the package offers a
convenient and user-friendly means of using \pdfannot to
provide comments in PDF files. Since version v1.1,
pdfcomment.sty also supports LaTeX - dvips - ps2pdf, LaTeX -
dvipdfmx, and XeLaTeX. Unfortunately, support of PDF
annotations by PDF viewers is sparse to nonexistent. The
reference viewer for the development of this package is Adobe
Reader.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfcomment/pdfcomment.sty
%doc %{_texmfdistdir}/doc/latex/pdfcomment/CHANGES
%doc %{_texmfdistdir}/doc/latex/pdfcomment/INSTALL
%doc %{_texmfdistdir}/doc/latex/pdfcomment/README.md
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example.tex
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvipdfmx.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvipdfmx.tex
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvips_ps2pdf.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvips_ps2pdf.tex
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_math_markup.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_math_markup.tex
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_xelatex.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/example_xelatex.tex
%doc %{_texmfdistdir}/doc/latex/pdfcomment/manifest.txt
%doc %{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment.tex
%doc %{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment_de.pdf
%doc %{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment_de.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

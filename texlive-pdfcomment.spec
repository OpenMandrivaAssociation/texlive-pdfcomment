# revision 22604
# category Package
# catalog-ctan /macros/latex/contrib/pdfcomment
# catalog-date 2011-05-24 10:48:56 +0200
# catalog-license lppl1.3
# catalog-version v2.2
Name:		texlive-pdfcomment
Version:	v2.2
Release:	1
Summary:	A user-friendly interface to pdf annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfcomment
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcomment.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfcomment/pdfcomment.sty
%doc %{_texmfdistdir}/doc/latex/pdfcomment/CHANGES
%doc %{_texmfdistdir}/doc/latex/pdfcomment/INSTALL
%doc %{_texmfdistdir}/doc/latex/pdfcomment/README
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

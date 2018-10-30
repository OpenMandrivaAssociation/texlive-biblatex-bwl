# revision 26556
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-biblatex-bwl
Version:	0.02
Release:	3
Summary:	TeXLive biblatex-bwl package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bwl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bwl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive biblatex-bwl package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-bwl/bwl-FU.bbx
%{_texmfdistdir}/tex/latex/biblatex-bwl/bwl-FU.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-bwl/Changes
%doc %{_texmfdistdir}/doc/latex/biblatex-bwl/doc/bwl-FU.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-bwl/doc/bwl-FU.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-bwl/doc/bwl-FU.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120809-1
+ Revision: 813407
- Import texlive-biblatex-bwl
- Import texlive-biblatex-bwl


%global tl_name biblatex-bwl
%global tl_revision 26556

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	BibLaTeX citations for FU Berlin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-bwl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bwl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bwl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a set of BibLaTeX implementations of bibliography
and citation styles for the Business Administration Department of the
Free University of Berlin.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-bwl
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-bwl
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-bwl/doc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bwl/Changes
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bwl/doc/bwl-FU.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bwl/doc/bwl-FU.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bwl/doc/bwl-FU.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-bwl/bwl-FU.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-bwl/bwl-FU.cbx

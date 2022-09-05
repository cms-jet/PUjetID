import collections
import ROOT
import os

#
# export PATH=/cvmfs/sft.cern.ch/lcg/external/texlive/2017/bin/x86_64-linux:$PATH
#
def main():

  eras = [
    "UL2018",
    "UL2017",
    "UL2016early",
    "UL2016late",
  ]

  CompilePlots(eras, "PUID_UL_Validation")

def CompilePlots(eras, outFileName):
  
  outFile = open(outFileName+".tex","w")

  makeHeader(outFile)
  makeTemplates(outFile)
  makeBeginDocument(outFile)
  makeMainContent(outFile,eras)
  makeEndDocument(outFile)
  outFile.close()

  os.system("pdflatex %s.tex"%(outFileName))
  os.system("pdflatex %s.tex"%(outFileName))
  os.system("rm -rvf *.aux *.lof *.log *.out *.toc *.nav *.snm")

def makeHeader(outFile):
  outFile.write("\\documentclass[aspectratio=169]{beamer} \n")
  outFile.write("\\setbeamertemplate{footline}[frame number] \n")
  outFile.write("\\setbeamertemplate{frametitle}{ \n")
  outFile.write(" \\vspace{0.05mm} \n")
  outFile.write(" \\insertframetitle \n")
  outFile.write("}\n")
  outFile.write("\\setbeamertemplate{navigation symbols}{}\n")
  outFile.write("\\setbeamersize{text margin left=1.5mm,text margin right=0.2mm} \n")
  outFile.write("\\setbeamerfont{frametitle}{size=\\normalsize}\n")
  outFile.write("\n")
  outFile.write("\\usepackage[absolute,overlay]{textpos}\n")
  outFile.write("\\usepackage{tabularx}\n")
  outFile.write("\\usepackage{graphicx}\n")
  outFile.write("\\usepackage{subcaption}\n")
  outFile.write("\\newcolumntype{C}{>{\centering\\arraybackslash}X}\n")
  outFile.write("\\usepackage{booktabs}\n")
  outFile.write("\\usepackage[labelformat=empty]{caption}\n")
  outFile.write("\\captionsetup{font=scriptsize,labelfont=scriptsize,justification=centering}\n")
  outFile.write("\\usepackage[absolute,overlay]{textpos}\n")
  outFile.write("\n")
  outFile.write("\\renewcommand{\\arraystretch}{0.01}\n")
  outFile.write("\n")
  outFile.write("\\AtBeginSection[]{\n")
  outFile.write(" \\begin{frame}\n")
  outFile.write(" \\vfill\n")
  outFile.write(" \\centering\n")
  outFile.write(" \\begin{beamercolorbox}[sep=8pt,center,shadow=true,rounded=true]{title}\n")
  outFile.write("   \\usebeamerfont{title}\\insertsectionhead\\par%\n")
  outFile.write(" \\end{beamercolorbox}\n")
  outFile.write(" \\vfill\n")
  outFile.write(" \\end{frame}\n")
  outFile.write("}\n")


def makeTemplates(outFile):
  outFile.write("\n\n\n\n")
  outFile.write("\\newcommand{\\PlotsJetPtEta}[3]\n")
  outFile.write("{\n")
  outFile.write("\\begin{frame}\n")
  outFile.write("\\frametitle{#3}\n")
  outFile.write("\\vskip 18pt\n")
  outFile.write("\\begin{figure}[b]\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_prePuId_probeJet_pt}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_passPuIdLoose_probeJet_pt}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_passPuIdMedium_probeJet_pt}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_passPuIdTight_probeJet_pt}\n")
  outFile.write("\\end{subfigure}\\\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_prePuId_probeJet_eta_fixbin}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_passPuIdLoose_probeJet_eta_fixbin}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_passPuIdMedium_probeJet_eta_fixbin}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\begin{subfigure}[t]{0.23\\textwidth}\n")
  outFile.write("\\includegraphics[width=\\textwidth]{#2/h_#1_passPuIdTight_probeJet_eta_fixbin}\n")
  outFile.write("\\end{subfigure}\n")
  outFile.write("\\end{figure}\n")
  outFile.write("\\begin{textblock}{5}(1.8,1.7)\n")
  outFile.write("NoPUID\n")
  outFile.write("\\end{textblock}\n")
  outFile.write("\\begin{textblock}{5}(5.5,1.7)\n")
  outFile.write("PU Loose\n")
  outFile.write("\\end{textblock}\n")
  outFile.write("\\begin{textblock}{5}(9.0,1.7)\n")
  outFile.write("PU Medium\n")
  outFile.write("\\end{textblock}\n")
  outFile.write("\\begin{textblock}{5}(13.0,1.7)\n")
  outFile.write("PU Tight\n")
  outFile.write("\\end{textblock}\n")
  outFile.write("\\end{frame}\n")
  outFile.write("}\n")
  outFile.write("\n\n\n")

def makeBeginDocument(outFile):
  outFile.write("\\begin{document}\n")
  outFile.write("\\begin{frame}{Overview}\n")
  outFile.write("\\tableofcontents[hideallsubsections]\n")
  outFile.write("\\end{frame}\n")

def makeMainContent(outFile,eras):
  for era in eras:
    outFile.write("\\section{%s}\n"%(era))
    outFile.write("\\PlotsJetPtEta{%s}{../plots_pujetid_datamc_noSF}{%s:No Scale Factors}\n"%(era,era))
    outFile.write("\\PlotsJetPtEta{%s}{../plots_pujetid_datamc_effSF}{%s:Eff Scale Factors}\n"%(era,era))

def makeEndDocument(outFile):
  outFile.write("\\end{document}\n")

if __name__ == "__main__":
  main()

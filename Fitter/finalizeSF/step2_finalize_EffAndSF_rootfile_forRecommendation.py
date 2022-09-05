import os
import ROOT
import math
import collections
ROOT.gROOT.SetBatch(True)

def ClearErrors(h2):
    nbinsX = h2.GetNbinsX()
    nbinsY = h2.GetNbinsY()
    for iBinX in range(1,nbinsX+1):
        for iBinY in range(1,nbinsY+1):
            valNominal = h2.SetBinError(iBinX,iBinY,0.)
    return h2

eras=[
    "UL2018",
    "UL2017",
    "UL2016NonAPV",
    "UL2016APV"
]

wps = [
    "L",
    "M",
    "T"
]

# inFilePath="../../Validation/data/PUID_SFAndEff_ULNanoV9_v1p4_NLO.root"
inFilePath="../results_final_EffAndSf_ULNanoV9_v1p4/PUID_SFAndEff_ULNanoV9_v1p4_NLO.root"
inFile = ROOT.TFile(inFilePath,"OPEN") 

histograms = []
#
# MC Efficiency Map
#
for era in eras:
    for wp in wps:
        print(era+"|"+wp)
        h2_eff = inFile.Get("h2_eff_mc"+era+"_"+wp)
        histograms.append(h2_eff)
#
# SF Efficiency Map
#
for era in eras:
    for wp in wps:
        print(era+"|"+wp)
        h2_sf = inFile.Get("h2_eff_sf"+era+"_"+wp)
        h2_sf  = ClearErrors(h2_sf)
        histograms.append(h2_sf)
#
# SF Efficiency Uncertainty Map
#
for era in eras:
    for wp in wps:
        print(era+"|"+wp)
        h2_sf_systuncertainty = inFile.Get("h2_eff_sf"+era+"_"+wp+"_Systuncty")
        histograms.append(h2_sf_systuncertainty)
  
#
#
#
outFileName = "PUID_106XTraining_ULRun2_EffSFandUncties_v1"
outFile = ROOT.TFile("./"+outFileName+".root","RECREATE")
for histo in histograms:
    histo.Write()
outFile.Close()

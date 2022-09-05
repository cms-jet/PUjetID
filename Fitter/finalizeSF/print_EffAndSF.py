from prettytable import PrettyTable
import ROOT
import uproot

def PrintEffAndSFTable(fileName, h2Name, h2UncName=None, printError=False):
  print ("\n")
  print ("FILE="+fileName)
  print ("HISTO="+h2Name)
  if h2UncName != None:
    print ("HISTOUNC="+h2UncName)

  file = ROOT.TFile(fileName,"OPEN") 
  h2    = file.Get(h2Name)
  h2Unc = None
  if h2UncName != None:
    h2Unc = file.Get(h2UncName)

  nBinsX = h2.GetNbinsX()
  nBinsY = h2.GetNbinsY()

  table  = PrettyTable()
  names_column = [""]
  #
  # get column names (pt bins)
  #
  for iBinX in xrange(1,nBinsX+1):
    binX_Lo = h2.GetXaxis().GetBinLowEdge(iBinX)
    binX_Up = h2.GetXaxis().GetBinUpEdge(iBinX)
    columnName = "[%.1f,%.1f)"%(binX_Lo,binX_Up)
    names_column.append(columnName)
  table.field_names = names_column
  #
  # get info per row (eta bins)
  #
  for iBinY in xrange(1,nBinsY+1):
    binY_Lo = h2.GetYaxis().GetBinLowEdge(iBinY)
    binY_Up = h2.GetYaxis().GetBinUpEdge(iBinY)
    rowName = "[%.3f,%.3f)"%(binY_Lo,binY_Up)
    row = [rowName]
    for iBinX in xrange(1,nBinsX+1):
      sf  = h2.GetBinContent(iBinX,iBinY)
      if printError:
        unc = h2Unc.GetBinContent(iBinX,iBinY)
        if sf != 0:
          entryStr = "%.4f +/- %.4f (%.2f%%)" %(sf,unc,(unc/sf)*100.)
        else:
          entryStr = "%.4f +/- %.4f (%.2f%%)" %(sf,(0.))
      else:
        entryStr = "%.4f" %(sf)
      row.append(entryStr)
    table.add_row(row)
  #
  # print table
  #
  print(table)
  print("\n")

inFile="../Validation/data/PUID_SFAndEff_ULNanoV9_v1p4_NLO.root"

era = "UL2018"
wps = ["L","M","T"]

for wp in wps:
  PrintEffAndSFTable(inFile,"h2_eff_mc"+era+"_"+wp)
  PrintEffAndSFTable(inFile,"h2_eff_sf"+era+"_"+wp, "h2_eff_sf"+era+"_"+wp+"_Systuncty", True)
  PrintEffAndSFTable(inFile,"h2_eff_sf"+era+"_"+wp, "h2_eff_sf"+era+"_"+wp+"_Systuncty_Fit", True)
  PrintEffAndSFTable(inFile,"h2_eff_sf"+era+"_"+wp, "h2_eff_sf"+era+"_"+wp+"_Systuncty_Gen", True)
  PrintEffAndSFTable(inFile,"h2_eff_sf"+era+"_"+wp, "h2_eff_sf"+era+"_"+wp+"_Systuncty_JES", True)

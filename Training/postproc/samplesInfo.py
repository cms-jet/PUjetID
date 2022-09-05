EOSURL      = "root://eoscms.cern.ch/"
prod_tag    = "DiLepSkim_JMENanoV9_v1p4"
path_inDir  = "/eos/cms/store/group/phys_jetmet/nbinnorj/JetPUIdTrain_"+prod_tag+"/CRABOUTPUT/"
path_outDir = "/eos/cms/store/group/phys_jetmet/nbinnorj/JetPUIdTrain_"+prod_tag+"/MERGED/"

samplesInfoDict = dict()

#
# Define cross-sections and path for all eras
#
eraListForMC = [
  "UL18",
]
#
# Cross-sections in picobarns
#
for era in eraListForMC:
  samplesInfoDict["MC"+era+"_DY_MG"] = {
    "path": [
      "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/JetPUIdTrain_MC"+era+"JMENanoAODv9_"+prod_tag+"*/*/*/tree_*.root"
    ],
    # "xsec": 5347.0,
    # xs_NNLO: https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
    "xsec": 6077.22,
  }
  samplesInfoDict["MC"+era+"_DY_AMCATNLO"] = {
    "path": [
      "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/JetPUIdTrain_MC"+era+"JMENanoAODv9_"+prod_tag+"*/*/*/tree_*.root"
    ],
    #xs_NNLO: https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
    "xsec": 6077.22,
  }
  samplesInfoDict["MC"+era+"_TTTo2L2Nu"] = {
    "path": [
      "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/JetPUIdTrain_MC"+era+"JMENanoAODv9_"+prod_tag+"*/*/*/tree_*.root"
    ],
    # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO#Top_quark_pair_cross_sections_at  
    # BR(W->lv) from PDG(2018)
    # pb: xs_NNLO(ttbar) * (3*BR(W->lv)) * (3*BR(W->lv)) =  831.76*(3*0.1086)*(3*0.1086)
    "xsec": 88.29, 
  }
#
# UL2017 Lumi: 41479.68 picobarns
# https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#SummaryTable
#
samplesInfoDict["DataUL17_DoubleMuon"] = { 
  "path" : [
    "DoubleMuon/JetPUIdTrain_Run2017B-DataUL17JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2017C-DataUL17JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2017D-DataUL17JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2017E-DataUL17JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2017F-DataUL17JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
  ],
  "xsec":1.0,
}
#
# UL2018 Lumi: 59832.47 picobarns
# https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#SummaryTable
#
samplesInfoDict["DataUL18_DoubleMuon"] = { 
  "path" : [
    "DoubleMuon/JetPUIdTrain_Run2018A-DataUL18JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2018B-DataUL18JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2018C-DataUL18JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
    "DoubleMuon/JetPUIdTrain_Run2018D-DataUL18JMENanoAODv9_"+prod_tag+"/*/*/tree_*.root",
  ],
  "xsec":1.0,
}



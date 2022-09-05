def GetSampleList(file):
  samplelist = file.readlines()
  samplelist = [x.strip() for x in samplelist] 
  samplelist = [x for x in samplelist if x] # Choose lines that are not empty
  samplelist = [x for x in samplelist if not(x.startswith("#"))] # Choose lines that do not start with #
  return samplelist

def TrimPrimaryNameForMC(dataset):
  name = dataset.split('/')[1]
  name = name.replace("_13TeV","")
  name = name.replace("_TuneCP5","")
  name = name.replace("pythia","py")
  name = name.replace("herwig","hw")
  name = name.replace("madgraph","mg")
  name = name.replace("powheg","phg")
  name = name.replace("amcatnlo","mcNLO")
  name = name.replace("powhegMiNNLO","pwhg")
  name = name.replace("-photos","")
  name = name.replace("FXFX","")
  name = name.replace("_MatchEWPDG20","")
  return name

def TrimSecondaryNameForMC(dataset):
  name = dataset.split('/')[2]

  if "JMENano" in name:
    name = name.replace("RunIISummer20UL16NanoAODAPVv9-","MCUL16APVJMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11","") #REMOVE GT. CHECK ITS UPDATED
    #
    name = name.replace("RunIISummer20UL16NanoAODv9-","MCUL16JMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("20UL16JMENano_106X_mcRun2_asymptotic_v17","") #REMOVE GT. CHECK ITS UPDATED
    #
    name = name.replace("RunIISummer20UL17NanoAODv9-","MCUL17JMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("20UL17JMENano_106X_mc2017_realistic_v9","") #REMOVE GT. CHECK ITS UPDATED
    #
    name = name.replace("RunIISummer20UL18NanoAODv9-","MCUL18JMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1","") #REMOVE GT. CHECK ITS UPDATED
  else:
    name = name.replace("RunIISummer20UL16NanoAODAPVv9-","MCUL16APVJMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("106X_mcRun2_asymptotic_preVFP_v11","") #REMOVE GT. CHECK ITS UPDATED
    #
    name = name.replace("RunIISummer20UL16NanoAODv9-","MCUL16JMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("106X_mcRun2_asymptotic_v17","") #REMOVE GT. CHECK ITS UPDATED
    #
    name = name.replace("RunIISummer20UL17NanoAODv9-","MCUL17JMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("106X_mc2017_realistic_v9","") #REMOVE GT. CHECK ITS UPDATED
    #
    name = name.replace("RunIISummer20UL18NanoAODv9-","MCUL18JMENanoV9")#RENAME CAMPAIGN. CHECK ITS UPDATED
    name = name.replace("106X_upgrade2018_realistic_v16_L1v1","") #REMOVE GT. CHECK ITS UPDATED

  name = name.replace("-v1","")# 
  name = name.replace("-v2","")# 
  name = name.replace("-v3","")#
  name = name.replace("-v4","")# Remove any version indication.There should only be one valid version for MC samples
  return name

def TrimSecondaryNameForData(dataset):
  name = dataset.split('/')[2]
  #
  if "JMENano" in name:
    name = name.replace("HIPM_UL2016_MiniAODv2_JMENanoAODv9","DataUL16APVJMENanoV9") #CHECK
    name = name.replace("UL2016_MiniAODv2_JMENanoAODv9","DataUL16JMENanoV9") #CHECK
    name = name.replace("UL2017_MiniAODv2_JMENanoAODv9","DataUL17JMENanoV9") #CHECK
    name = name.replace("UL2018_MiniAODv2_JMENanoAODv9","DataUL18JMENanoV9") #CHECK
  #
  else:
    name = name.replace("HIPM_UL2016_MiniAODv2_NanoAODv9","DataUL16APVNanoV9") #CHECK
    name = name.replace("UL2016_MiniAODv2_NanoAODv9","DataUL16NanoV9") #CHECK
    name = name.replace("UL2017_MiniAODv2_NanoAODv9","DataUL17NanoV9") #CHECK
    name = name.replace("UL2018_MiniAODv2_NanoAODv9","DataUL18NanoV9") #CHECK
  #
  name = name.replace("-v1","")# 
  name = name.replace("-v2","")# 
  name = name.replace("-v3","")#
  name = name.replace("-v4","")# Remove any version indication.
  return name

def GetDataStream(name):
  if   "DoubleEG" in name:   return "DoubleEG"
  elif "DoubleMuon" in name: return "DoubleMuon"
  elif "EGamma" in name:     return "EGamma"

def IsSampleData(dataset):
  name = dataset.split('/')[2]
  isData = False
  if   "Run2016" in name:isData = True
  elif "Run2017" in name:isData = True
  elif "Run2018" in name:isData = True
  return isData

def GetDataULRun(dataset):
  name  = dataset.split('/')[2]
  runName = None
  if   "Run2016B-ver1_HIPM_UL2016" in name: runName = "UL2016APV"
  elif "Run2016B-ver2_HIPM_UL2016" in name: runName = "UL2016APV"
  elif "Run2016C-HIPM_UL2016" in name: runName = "UL2016APV"
  elif "Run2016D-HIPM_UL2016" in name: runName = "UL2016APV"
  elif "Run2016E-HIPM_UL2016" in name: runName = "UL2016APV"
  elif "Run2016F-HIPM_UL2016" in name: runName = "UL2016APV"
  #
  elif "Run2016F-UL2016" in name: runName = "UL2016"
  elif "Run2016G-UL2016" in name: runName = "UL2016"
  elif "Run2016H-UL2016" in name: runName = "UL2016"
  #
  elif "Run2017B-UL2017" in name: runName = "UL2017"
  elif "Run2017C-UL2017" in name: runName = "UL2017"
  elif "Run2017D-UL2017" in name: runName = "UL2017"
  elif "Run2017E-UL2017" in name: runName = "UL2017"
  elif "Run2017F-UL2017" in name: runName = "UL2017"
  #
  elif "Run2018A-UL2018" in name: runName = "UL2018"
  elif "Run2018B-UL2018" in name: runName = "UL2018"
  elif "Run2018C-UL2018" in name: runName = "UL2018"
  elif "Run2018D-UL2018" in name: runName = "UL2018"
  #
  return runName

def GetMCULEra(dataset):
  name  = dataset.split('/')[2]
  eraName = None
  if   "UL16NanoAODAPV" in name: eraName = "UL2016APV"
  elif "UL16NanoAOD"    in name: eraName = "UL2016"
  elif "UL17NanoAOD"    in name: eraName = "UL2017"
  elif "UL18NanoAOD"    in name: eraName = "UL2018"
  #
  return eraName
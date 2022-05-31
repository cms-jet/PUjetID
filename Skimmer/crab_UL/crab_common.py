############################################################
# Part 1
# - Setup common crab job configurations
#
############################################################
from CRABClient.UserUtilities import config
crab_config = config()

#
# Set production version number
#
version="DiLeptonSkim_ULNanoV9_v1p4"
# version="DiLeptonSkim_JMENanoV9_v1p1"

#
# Set request name prefx
#
reqNamePrefix="JetPUId"
#
# Change this PATH where the crab directories are stored
# Example: crab_config.General.workArea = '/afs/cern.ch/work/n/nbinnorj/private/crab_projects/'
#
crab_config.General.workArea        = '/afs/cern.ch/work/n/nbinnorj/private/crab_projects/'
crab_config.General.transferOutputs = True
crab_config.General.transferLogs    = False
#
crab_config.JobType.pluginName = 'Analysis'
crab_config.JobType.psetName   = 'PSet.py'
crab_config.JobType.scriptExe  = 'crab_script.sh'
#
crab_config.JobType.inputFiles = [
'../script/branches_in.txt',
'../script/branches_out.txt',
'../RunSkimmerCrab.py',
'../RunSkimmerHelper.py',
'../../../PhysicsTools/NanoAODTools/scripts/haddnano.py'
]
#
crab_config.JobType.sendPythonFolder  = True
crab_config.JobType.outputFiles = ['tree.root']
#
crab_config.Data.splitting    = 'FileBased'
crab_config.Data.unitsPerJob  = 1
crab_config.Data.publication  = False
crab_config.Data.allowNonValidInputDataset = True
crab_config.JobType.allowUndistributedCMSSW = True
#
# Specify the outLFNDirBase and your storage site
#
#
# JetMET CMS EOS space at CERN
#
crab_config.Data.outLFNDirBase  = '/store/group/phys_jetmet/nbinnorj/'+reqNamePrefix+'_'+version+'/CRABOUTPUT/'
crab_config.Site.storageSite    = 'T2_CH_CERN'
#
# User CERNBox 
#
# crab_config.Data.outLFNDirBase  = '/store/user/nbinnorj/JetPUId_'+version+'/CRABOUTPUT/'
# crab_config.Site.storageSite    = 'T2_CH_CERNBOX'
#
crab_config.Data.ignoreLocality = True
whitelist_sites=[
'T2_CH_*',
'T2_US_*',
'T2_UK_*',
'T2_DE_*',
'T2_FR_*',
]
crab_config.Site.whitelist = whitelist_sites
# crab_config.Data.ignoreLocality   = False
# whitelist_sites=['T2_CH_CERN']
# crab_config.Site.whitelist = whitelist_sites

############################################################
# Part 2
# -  Loop over list of samples. Send to Grid
#
############################################################
import sys
import helpers
from CRABAPI.RawCommand import crabCommand

runTime_data = 360
runTime_mc   = 480

#
# Read in txt file with list of samples
#
f = open(sys.argv[1]) 
samplelist =  helpers.GetSampleList(f)

#
# Print out the list of samples
#
print("Will send crab jobs for the following samples:")
for dataset in samplelist:
  print(dataset)
print("\n\n")

#
# For each sample, set crab job configuration and then send to the Grid
#
for i, dataset in enumerate(samplelist):
  print("%d/%d:Sending CRAB job: %s" % (i+1,len(samplelist), dataset))
  #
  # Specify input dataset
  #
  crab_config.Data.inputDataset = dataset
  #
  # Check if Data or MC
  #
  isData = helpers.IsSampleData(dataset)
  if isData:
    #
    # If data, get run name from dataset name and 
    # set it as argument for era flag
    #
    dataRunName = helpers.GetDataULRun(dataset)
    dataStreamName = helpers.GetDataStream(dataset)
    crab_config.JobType.scriptArgs = [
      "era="+dataRunName,
      "isMC=0",
      'dataStream='+dataStreamName
    ]
    crab_config.JobType.maxJobRuntimeMin = runTime_data
    #
    # Have to make unique requestName.
    # Sample naming convention is a bit dumb and makes this more difficult.
    #
    primaryName   = dataset.split('/')[1]
    secondaryName = helpers.TrimSecondaryNameForData(dataset)
  else:
    #
    # If MC, get MC era from dataset name and set it as argument for era flag.
    # Check also if it is a signal MC or not
    #
    mcEraName = helpers.GetMCULEra(dataset)
    crab_config.JobType.scriptArgs = [
    	"era="+mcEraName,
      "isMC=1",
      'dataStream=MC',
    ]
    crab_config.JobType.maxJobRuntimeMin = runTime_mc 
    #
    # Have to make unique requestName. 
    #
    primaryName   = helpers.TrimPrimaryNameForMC(dataset)
    secondaryName = helpers.TrimSecondaryNameForMC(dataset)

  print(crab_config.JobType.scriptArgs)
  print(crab_config.JobType.maxJobRuntimeMin)

  requestName = primaryName + "_" + secondaryName
  requestName = reqNamePrefix + "_" + requestName + "_" + version
  crab_config.General.requestName = requestName
  
  outputDatasetTag = reqNamePrefix + "_" + secondaryName + "_" + version 
  crab_config.Data.outputDatasetTag = outputDatasetTag 
  
  print("requestName: "+requestName)
  print("outputDatasetTag: "+outputDatasetTag)
  crabCommand('submit', config = crab_config)
  print("")

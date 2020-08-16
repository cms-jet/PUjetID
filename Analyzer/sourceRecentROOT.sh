#!/bin/bash
if [ ! -z $CMSSW_BASE ]; then 
  echo "Unset CMSSW runtime environment"
  eval `scram unsetenv -sh`
fi
#
echo "Setup ROOT 6.22.00"
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.22.00/x86_64-centos7-gcc48-opt/bin/thisroot.sh
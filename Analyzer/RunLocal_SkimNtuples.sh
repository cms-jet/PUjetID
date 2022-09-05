#!/bin/bash
NCORES=4

SAMPLES=(
DataUL18A_DoubleMuon
DataUL18B_DoubleMuon
DataUL18C_DoubleMuon
DataUL18D_DoubleMuon
MCUL18_DY_MG
MCUL18_DY_AMCNLO
DataUL17B_DoubleMuon
DataUL17C_DoubleMuon
DataUL17D_DoubleMuon
DataUL17E_DoubleMuon
DataUL17F_DoubleMuon
MCUL17_DY_MG
MCUL17_DY_AMCNLO
DataUL16NonAPVF_DoubleMuon
DataUL16NonAPVG_DoubleMuon
DataUL16NonAPVH_DoubleMuon
MCUL16NonAPV_DY_MG
MCUL16NonAPV_DY_AMCNLO
DataUL16APVB_DoubleMuon
DataUL16APVC_DoubleMuon
DataUL16APVD_DoubleMuon
DataUL16APVE_DoubleMuon
DataUL16APVF_DoubleMuon
MCUL16APV_DY_MG
MCUL16APV_DY_AMCNLO
)

#
# Make skimmed ntuples
#
for SAMPLE in ${SAMPLES[@]}
do
  python SkimNtuples.py --sample $SAMPLE --cores $NCORES
done

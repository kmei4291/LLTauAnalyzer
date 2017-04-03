#!/bin/bash
scramv1 project CMSSW CMSSW_9_0_0
cd CMSSW_9_0_0/src
eval `scramv1 runtime -sh`

git cms-init

git cms-merge-topic cms-tsg-storm:for83Xsamples

scram b -j 10

cd HLTrigger

git clone git@github.com:isobelojalvo/LLTauAnalyzer.git

cd LLTauAnalyzer/test

##example hlt configuration getter to work with single tau trigger 83x samples
hltGetConfiguration /dev/CMSSW_9_0_1/HLT \
--globaltag 90X_upgrade2017_TSG_Hcal_V2 \
--path HLTriggerFirstPath,HLT_VLooseIsoPFTau140_Trk50_eta2p1_v5,HLTriggerFinalPath \
--input root://eoscms.cern.ch//eos/cms/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/130000/064423AD-EB10-E711-988F-0025904B26A8.root \
--mc --process MYHLT --full --offline \
--l1-emulator FullSimHcalTP \
--unprescale --max-events 10 \
--output none > hlt-singleTau.py

cd $CMSSW_BASE/src

scram b -j 10


BTagValidation (needs updating!)
==============

Boosted b-tag validation analysis 

To set up:

Follow the directions to clone cms-btv-pog/RecoBTag-PerformanceMeasurements at https://github.com/cms-btv-pog/RecoBTag-PerformanceMeasurements

After setting up the PerformanceMeasurements package:

cd CMSSW_7_X_X/src      
(Replace X's with the release number you are using)

git clone git://github.com/cms-btv-pog/RecoBTag-BTagValidation.git RecoBTag/BTagValidation

scram b -j8

cd RecoBTag/BTagValidation/test/

cmsRun btagvalidation_cfg.py
  
  
  To run systematics:
  src/BTagValidation.cc has b fragmentation, c fragmentation, ntracks, c->D fragmentation, K0/Lambda, and pileup up and down systematics implemented. For b fragmentation, in test/btagvalidation_cfg.py, doBFrag=True and you need to run once with doBFragUp=True and once with doBFragDown=True. For c fragmentation, doCFrag=True. For c->D fragmentation, doCDFrag=True. For K0/Lambda, doK0L=True.
  
  For ntracks reweighting, you have to run test/dataMCntracks/jetwt.py over a file that already contains the QCD and data distributions, in order to get a root file that will reweight the QCD ntracks distribution to look like the data ntracks distribution. That file is fed to test/btagvalidation_cfg.py as FileNtracksWt and you must set doNtracksReweighting=True.
  
  For pileup up and down, you reset File_PUDistData in test/btagvalidation_cfg.py to be (?) or (?).
  


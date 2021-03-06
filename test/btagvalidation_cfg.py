import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('python')

options.register('outFilename', 'bTagValPlots.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
    )
options.register('reportEvery', 1000,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=1000)"
    )
options.register('DEBUG', True,
   VarParsing.multiplicity.singleton,
   VarParsing.varType.bool,
   "Display debugging statements"
   )
options.register('DEBUGlevel', 0,
   VarParsing.multiplicity.singleton,
   VarParsing.varType.int,
   "Debugging statements level."
   )
options.register('triggerSelection', '',
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    "Trigger selection"
    )
options.register('triggerLogicIsOR', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Trigger logic: True = OR, False = AND'
    )
options.register('useJetProbaTree', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use jet probability tree"
    )
options.register('applyFatJetMuonTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply muon tagging to fat jets (require 1 muon in fatjet)"
    )
options.register('applyFatJetMuonTaggingV2', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply muon tagging to fat jets (require at least 1 muon in a subjet)"
    )
options.register('applyFatJetBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b tagging to fat jets"
    )
options.register('fatJetDoubleTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Require fat jets to be double-tagged"
    )
options.register('fatJetDoubleBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Require fat jets to be double-b-tagged"
    )
options.register('fatJetDoubleSVBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Require fat jets to be double-SV-b-tagged"
    )
options.register('usePrunedSubjets', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Process pruned subjets"
    )
options.register('useSoftDropSubjets', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Process soft drop subjets"
    )
options.register('applySubJetMuonTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply muon tagging to subjets"
    )
options.register('applySubJetBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b tagging to subjets"
    )
options.register('dynamicMuonSubJetDR', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use dynamic muon-subjet dR requirement"
    )
options.register('useFlavorCategories', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use flavor categories for MC distributions"
    )
options.register('useRelaxedMuonID', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use relaxed muon ID"
    )
options.register('muonPtMin', 7.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum Muon Pt"
    )
options.register('fatJetAbsEtaMax', 2.4,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum abs(eta)"
    )
options.register('fatJetPtMin', 425.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum fat jet Pt"
    )
options.register('fatJetPtMax', 1.E6,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum fat jet Pt"
    )
options.register('removeProblemJet', True,
   VarParsing.multiplicity.singleton,
   VarParsing.varType.bool,
   "Remove problematic jets from low pT MC bins"
   )
options.register('usePrunedMass', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use pruned mass cut"
    )
options.register('useSoftDropMass', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use softdrop mass cut"
    )
options.register('fatJetGroomedMassMin', 0.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum fat jet softdrop/pruned mass"
    )
options.register('fatJetGroomedMassMax', 1.E6,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum fat jet softdrop/pruned mass"
    )
options.register('fatJetTau21Min', 0.0, #added by rizki
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "tau2/tau1 jet substructure min cut for fat jets"
    )
options.register('fatJetTau21Max', 0.5, #added by rizki
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "tau2/tau1 jet substructure max cut for fat jets"
    )
options.register('fatJetBDiscrCut', 0.244,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "B discriminator cut for fat jets"
    )
options.register('fatJetDoubleSVBDiscrMin', -0.20,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Double SV b discriminator cut for fat jets"
    )
options.register('fatJetDoubleSVBDiscrMax', 1.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Double SV b discriminator cut for fat jets"
    )
options.register('subJetBDiscrMin', 0.605,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "B discriminator min for subjets"
    )
options.register('subJetBDiscrMax', 1.000,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "B discriminator max for subjets"
    )
options.register('SFbShift', 0.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Shift in SFb in units of sigmas"
    )
options.register('SFlShift', 0.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Shift in SFl in units of sigmas"
    )
options.register('MuonJetPtRatio', 0.5,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "pT(muon)/pT(Jet) for Muon Tagging"
    )
options.register('DiMuonJetPtRatio', 0.6,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "pT(muon1+muon2)/pT(Jet) for Double Muon Tagging"
    )
options.register('doPUReweightingOfficial', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do pileup reweighting"
    )
options.register('FilePUDistData', '/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/RunII2016Rereco_25ns_PUXsec69000nb.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File for data/MC weights for PU reweight (official)"
    )
options.register('doPUReweightingNPV', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do pileup reweighting"
    )
options.register('doFatJetPtReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do fat jet pt reweighting'
    )
options.register('doNtracksReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do ntracks reweighting'
    )
options.register('doBFrag', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do b fragmentation reweighting'
    )
options.register('doBFragUp', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do b fragmentation reweighting up'
    )
options.register('doBFragDown', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do b fragmentation reweighting down'
    )
options.register('doCDFrag', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do c->D fragmentation reweighting'
    )
options.register('doCFrag', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do c fragmentation reweighting'
    )
options.register('doK0L', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do K0 and lambda reweighting'
    )
options.register('doSubJetPtReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do subjet pt reweighting'
    )
options.register('doSubJetPtBalanceReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do subjet pt balance reweighting'
    )
options.register('doMassSoftDropReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do soft drop reweighting'
    )
options.register('doJetNTracksReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do jetNTracks reweighting'
    )
options.register('doSV1EnergyRatioReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do SV1 energy ratio reweighting'
    )
options.register('doIPSig1stAboveBReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do IP sig 1st Track above bottom reweighting'
    )
options.register('doZratioReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Do Zatio reweighting'
    )
options.register('applySFs', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b-tagging SFs"
    )
options.register('btagCSVFile', 'CSVv2_4invfb.csv',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "CSV file containing b-tagging SFs"
    )
options.register('btagOperatingPoint', 0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "B-tagging opertaint point for CSVv2. Set to 'loose' by default"
    )
options.register('btagMeasurementType', "comb",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Measurement type: combined or ttbar"
    )
options.register('btagSFType', "central",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b-tagging SFs"
    )
options.register('FileFatJetPtWt', "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/dataMC_weight_calc/FatJet_pt_all_data_mc_weight_Mu_350.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File with data/MC weights for fat jet pT reweighting"
    )
options.register('FileNtracksWt', "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/dataMC_weight_calc/FatJet_track_multi_data_mc_weight_Mu_350.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File with data/MC weights for fat jet ntracks reweighting"
    )
options.register('FileSubJetPtWt', "/afs/cern.ch/work/a/asady/rizki_test/CMSSW_7_6_3/src/RecoBTag/BTagValidation/test/rizki_test/BTagValidation/test/SoftDropSubJetPt_data_mc_DoubleMuonTagged_QCDMuEnriched_76XMiniAODv2.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File with data/MC weights for subjet pT reweighting"
    )
options.register('FileSV1EnergyRatioWt', "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Mar21-2016_reproduceCommPlotsForPreApproval/CMSSW_7_6_3/src/RecoBTag/BTagValidation/test/rizki_signalMC_GluGLu/SV1EnergyRatio_Hbb_QCDbb_pt425_Double_JetTight_weight.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File with data/MC weights for SV1EnergyRatio reweighting"
    )
options.register('FileIPSig1stAboveBWt', "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Feb06-2016_SubjetPtReweight/CMSSW_7_6_3/src/RecoBTag/BTagValidation/test/rizki_signalMC_GluGLu/IPSig1stAboveB_Hbb_QCDbb_pt425_weight.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File with data/MC weights for IPSig1stAboveB reweighting"
    )
options.register('FileZratioWt', "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Mar21-2016_reproduceCommPlotsForPreApproval/CMSSW_7_6_3/src/RecoBTag/BTagValidation/test/rizki_signalMC_GluGLu/ZratioRatio_Hbb_QCDbb_pt425_Double_JetTight_weight.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File with data/MC weights for Zratio reweighting"
    )
options.register('newJECPayloadNames',  
    "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/JECfiles/Summer16_23Sep2016V3_MC_L1FastJet_AK8PFchs.txt,/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/JECfiles/Summer16_23Sep2016V3_MC_L2Relative_AK8PFchs.txt,/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/JECfiles/Summer16_23Sep2016V3_MC_L3Absolute_AK8PFchs.txt", 
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    "New JEC payload names"
    ),
options.register('jecUncPayloadName', 
    "/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/JECfiles/Summer16_23Sep2016V3_MC_Uncertainty_AK8PFchs.txt",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string, 
    "JEC uncertainty payload name"
    ),
options.register('doNewJEC', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply new JECs"
    )
options.register('doJECUncert', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do JEC uncertainty"
    )
options.register('FileBFrag', "/afs/cern.ch/work/a/asady/rizki_test/CMSSW_7_6_3/src/RecoBTag/BTagValidation/test/PtRelFall12/",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "File path for doBFrag systematics"
    )

options.parseArguments()

if options.usePrunedSubjets and options.useSoftDropSubjets:
  print "Warning: both pruned and soft drop subjets selected. Only pruned subjets will be processed."
  print "!!!Select either pruned subjets with 'usePrunedSubjets' or soft drop subjets with 'useSoftDropSubjets'."
elif not options.usePrunedSubjets and not options.useSoftDropSubjets:
  print "!!!Warning: no subjets will be processed.!!!"
  print "!!!Select either pruned subjets with 'usePrunedSubjets' or soft drop subjets with 'useSoftDropSubjets'."

# print options

process = cms.Process("BTagVal")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO'),
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) ) # Keep as such

process.source = cms.Source("EmptySource")

## Output file
#ext=""
#if options.usePrunedSubjets: 
#  ext="_WithPrunedSubjets"
#elif options.useSoftDropSubjets: 
#  ext="_withSoftDropSubjets"
#outFilename = options.outFilename+ext+".root"

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outFilename)
    )

from inputFiles_cfi import *
from RecoBTag.PerformanceMeasurements.bTagAnalyzerCommon_cff import *
#print bTagAnalyzerCommon.TriggerPathNames 

process.btagval = cms.EDAnalyzer('BTagValidation',
    DEBUG    = cms.bool(options.DEBUG),
    DEBUGlevel    = cms.int32(options.DEBUGlevel),
    MaxEvents              = cms.int32(options.maxEvents),
    ReportEvery            = cms.int32(options.reportEvery),
    UseJetProbaTree        = cms.bool(options.useJetProbaTree),
    InputTTreeEvtInfo      = cms.string('btaganaFatJets/ttree'),
    InputTTree             = cms.string('btaganaFatJets/ttree'),
    InputFiles             = cms.vstring(FileNames),
    #InputFiles             = cms.vstring(FileNames_QCD_Pt_800to1000),
    UseFlavorCategories    = cms.bool(options.useFlavorCategories),
    UseRelaxedMuonID       = cms.bool(options.useRelaxedMuonID),
    ApplyFatJetMuonTagging = cms.bool(options.applyFatJetMuonTagging),
    ApplyFatJetMuonTaggingV2 = cms.bool(options.applyFatJetMuonTaggingV2),
    ApplyFatJetBTagging    = cms.bool(options.applyFatJetBTagging),
    FatJetDoubleTagging    = cms.bool(options.fatJetDoubleTagging),
    FatJetDoubleBTagging   = cms.bool(options.fatJetDoubleBTagging),
    FatJetDoubleSVBTagging = cms.bool(options.fatJetDoubleSVBTagging),
    UsePrunedSubjets       = cms.bool(options.usePrunedSubjets),
    UseSoftDropSubjets     = cms.bool(options.useSoftDropSubjets),
    ApplySubJetMuonTagging = cms.bool(options.applySubJetMuonTagging),
    ApplySubJetBTagging    = cms.bool(options.applySubJetBTagging),
    DynamicMuonSubJetDR    = cms.bool(options.dynamicMuonSubJetDR),
    FatJetBDiscrCut        = cms.double(options.fatJetBDiscrCut),
    FatJetDoubleSVBDiscrMin= cms.double(options.fatJetDoubleSVBDiscrMin), 
    FatJetDoubleSVBDiscrMax= cms.double(options.fatJetDoubleSVBDiscrMax), 
    SubJetBDiscrMin        = cms.double(options.subJetBDiscrMin),
    SubJetBDiscrMax        = cms.double(options.subJetBDiscrMax),
    MuonPtMin            = cms.double(options.muonPtMin),
    FatJetPtMin            = cms.double(options.fatJetPtMin),
    FatJetPtMax            = cms.double(options.fatJetPtMax),
    RemoveProblemJet    = cms.bool(options.removeProblemJet),
    UsePrunedMass       = cms.bool(options.usePrunedMass),
    UseSoftDropMass     = cms.bool(options.useSoftDropMass),
    FatJetGroomedMassMin  = cms.double(options.fatJetGroomedMassMin),
    FatJetGroomedMassMax  = cms.double(options.fatJetGroomedMassMax),
    File_PVWt              = cms.string(''),
    Hist_PVWt              = cms.string(''),
    File_PUDistMC          = cms.string('/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/Jan12_SFCommPlots_NoTreeBTagVal/CMSSW_8_0_23/src/RecoBTag/BTagValidation/test/PUDistMC_Summer2016_25ns_Moriond17MC_PoissonOOTPU.root'), 
    Hist_PUDistMC          = cms.string('pileup'),
#     File_PUDistData        = cms.string('/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/July27-2016_SFMeasurement/CMSSW_8_0_12/src/RecoBTag/BTagValidation/test/RunII2016_25ns_PUSpring16V2_Xsec69200nb.root'), #some lumi sections were missing?
#     File_PUDistData        = cms.string('/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/July27-2016_SFMeasurement/CMSSW_8_0_12/src/RecoBTag/BTagValidation/test/RunII2016_25ns_PUSpring16V1_Xsec69200nb.root'), #devdatta's file
#     File_PUDistData        = cms.string('/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/July27-2016_SFMeasurement/CMSSW_8_0_12/src/RecoBTag/BTagValidation/test/RunII2016_25ns_PUSpring16V3_Xsec69200nb.root'), #reproduce again, the missing lumis are not missing anymore?
#     File_PUDistData        = cms.string('/afs/cern.ch/user/r/rsyarif/workHere/HbbTagVal/July27-2016_SFMeasurement/CMSSW_8_0_12/src/RecoBTag/BTagValidation/test/RunII2016_25ns_PUSpring16V1_Xsec62000nb.root'), #use different minbias xsec.
    File_PUDistData        = cms.string(options.FilePUDistData),
    Hist_PUDistData        = cms.string('pileup'),
    File_FatJetPtWt        = cms.string(options.FileFatJetPtWt),
    Hist_FatJetPtWt        = cms.string('FatJet_pt_all_weight_data_mc'),
    File_NtracksWt         = cms.string(options.FileNtracksWt),                             
    Hist_NtracksWt         = cms.string('FatJet_track_multi_weight_data_mc'),
    File_SubJetPtWt        = cms.string(options.FileSubJetPtWt), 
    Hist_SubJetPtWt        = cms.string('jetptweight_mc_data'),
    File_SubJetPtBalanceWt = cms.string('subjetptbalance_Hbb_QCDbb_pt425_weight.root'), #added by rizki for Hbb tagger signal vs proxy studies. File for subjet pt balance reweighting.
    Hist_SubJetPtBalanceWt = cms.string('subjetptbalanceweight_mc_data'), #added by rizki for Hbb tagger signal vs proxy studies. File for subjet pt balance reweighting.
    File_MassSoftDropWt = cms.string('massSoftDrop_Hbb_QCDbb_pt425_weight.root'), #added by rizki for Hbb tagger signal vs proxy studies. File for mass reweighting.
    Hist_MassSoftDropWt = cms.string('massSoftDropweight_mc_data'), #added by rizki for Hbb tagger signal vs proxy studies. File for mass reweighting.
    File_JetNTracksWt = cms.string('jetNTracks_Hbb_QCDbb_pt425_weight.root'), #added by rizki for Hbb tagger signal vs proxy studies. File for jetNTracks reweighting.
    Hist_JetNTracksWt = cms.string('jetNTracksweight_mc_data'), #added by rizki for Hbb tagger signal vs proxy studies. File for jetNTracks reweighting.
    File_SV1EnergyRatioWt = cms.string(options.FileSV1EnergyRatioWt), #added by rizki for Hbb tagger signal vs proxy studies. File for SV1 energy ratio reweighting.
    Hist_SV1EnergyRatioWt = cms.string('SV1EnergyRatioweight_mc_data'), #added by rizki for Hbb tagger signal vs proxy studies. File for SV1 energy ratio reweighting.
    File_IPSig1stAboveBWt = cms.string(options.FileIPSig1stAboveBWt), #added by rizki for Hbb tagger signal vs proxy studies. File for IPSig1stAboveB reweighting.
    Hist_IPSig1stAboveBWt = cms.string('IPSig1stAboveBweight_mc_data'), #added by rizki for Hbb tagger signal vs proxy studies. File for IPSig1stAboveB reweighting.
    File_ZratioWt = cms.string(options.FileZratioWt), #added by rizki for Hbb tagger signal vs proxy studies. File for Zratio reweighting.
    Hist_ZratioWt = cms.string('Zratioweight_mc_data'), #added by rizki for Hbb tagger signal vs proxy studies. File for Zratio reweighting.
    FatJetTau21Min         = cms.double(options.fatJetTau21Min), #added by rizki
    FatJetTau21Max         = cms.double(options.fatJetTau21Max), #added by rizki
    FatJetAbsEtaMax        = cms.double(options.fatJetAbsEtaMax), #added by rizki
    SFbShift               = cms.double(options.SFbShift),
    SFlShift               = cms.double(options.SFlShift),
    MuonJetPtRatio               = cms.double(options.MuonJetPtRatio),
    DiMuonJetPtRatio               = cms.double(options.DiMuonJetPtRatio),
    DoPUReweightingOfficial= cms.bool(options.doPUReweightingOfficial),
    DoPUReweightingNPV     = cms.bool(options.doPUReweightingNPV),
    DoFatJetPtReweighting  = cms.bool(options.doFatJetPtReweighting),
    DoNtracksReweighting  = cms.bool(options.doNtracksReweighting),
    DoBFrag = cms.bool(options.doBFrag),
    DoBFragUp = cms.bool(options.doBFragUp),
    DoBFragDown = cms.bool(options.doBFragDown),                                 
    DoCDFrag = cms.bool(options.doCDFrag),
    DoCFrag = cms.bool(options.doCFrag),
    DoK0L = cms.bool(options.doK0L),                                 
    DoSubJetPtReweighting  = cms.bool(options.doSubJetPtReweighting),
    DoSubJetPtBalanceReweighting  = cms.bool(options.doSubJetPtBalanceReweighting),
    DoMassSoftDropReweighting  = cms.bool(options.doMassSoftDropReweighting),
    DoJetNTracksReweighting  = cms.bool(options.doJetNTracksReweighting),
    DoSV1EnergyRatioReweighting  = cms.bool(options.doSV1EnergyRatioReweighting),
    DoIPSig1stAboveBReweighting  = cms.bool(options.doIPSig1stAboveBReweighting),
    DoZratioReweighting  = cms.bool(options.doZratioReweighting),
    TriggerSelection       = cms.vstring( # OR of all listed triggers applied, empty list --> no trigger selection applied
      options.triggerSelection
      ),
    TriggerPathNames       = bTagAnalyzerCommon.TriggerPathNames,
    triggerLogicIsOR      = cms.bool(options.triggerLogicIsOR),
    ApplySFs               = cms.bool(options.applySFs),
    btagCSVFile            = cms.string(options.btagCSVFile),
    btagOperatingPoint     = cms.int32(options.btagOperatingPoint),
    btagMeasurementType    = cms.string(options.btagMeasurementType),
    btagSFType             = cms.string(options.btagSFType), 
    newJECPayloadNames     = cms.vstring(options.newJECPayloadNames), 
    jecUncPayloadName      = cms.string(options.jecUncPayloadName), 
    doNewJEC               = cms.bool(options.doNewJEC),
    doJECUncert            = cms.bool(options.doJECUncert),  
    File_BFrag				= cms.string(options.FileBFrag), 
)

#process.btagvalsubjetmu = process.btagval.clone(
    #ApplySubJetMuonTagging = cms.bool(not options.applySubJetMuonTagging),
#)

#process.btagvalsubjetbtag = process.btagval.clone(
    #ApplySubJetMuonTagging = cms.bool(not options.applySubJetMuonTagging),
    #ApplySubJetBTagging = cms.bool(True),
#)

process.p = cms.Path(process.btagval)
#process.p = cms.Path(process.btagval + process.btagvalsubjetmu + process.btagvalsubjetbtag)

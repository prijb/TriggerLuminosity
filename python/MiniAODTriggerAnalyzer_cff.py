import FWCore.ParameterSet.Config as cms

unpackedPatTrigger = cms.EDProducer(
    "PATTriggerObjectStandAloneUnpacker",
    patTriggerObjectsStandAlone = cms.InputTag('slimmedPatTrigger'),
    triggerResults              = cms.InputTag('TriggerResults::HLT'),
    unpackFilterLabels = cms.bool(True)
)

# Order is important !!!
seeds = [
    'L1_DoubleMu_12_5',
    'L1_DoubleMu_15_7',
    'L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7',
    'L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18',
    'L1_DoubleMu4_SQ_OS_dR_Max1p2',
    'L1_DoubleMu4p5_SQ_OS_dR_Max1p2',
]

# Order is important !!!
paths=[
    'DST_HLTMuon_Run3_PFScoutingPixelTracking_v20',
    'DST_Run3_DoubleMu3_PFScoutingPixelTracking_v20',
    'DST_Run3_EG16_EG12_PFScoutingPixelTracking_v20',
    'DST_Run3_EG30_PFScoutingPixelTracking_v20',
    'DST_Run3_JetHT_PFScoutingPixelTracking_v20',
]

miniAODTriggerAnalyzer = cms.EDAnalyzer(
    "MiniAODTriggerAnalyzer",
    HLTProcess = cms.string('HLT'),
    HLTPaths = cms.vstring(paths),
    L1Seeds = cms.vstring(seeds),
    cfg = cms.PSet(
        stageL1Trigger = cms.uint32(2),
        l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
        l1tExtBlkInputTag = cms.InputTag('gtStage2Digis')
    ),
    bits = cms.InputTag("TriggerResults","","HLT"),
    prescales = cms.InputTag("patTrigger"),
    objects = cms.InputTag("unpackedPatTrigger"),
    Verbose = cms.int32(1),
    OnlyLowestUnprescaledHltPath = cms.bool(True),
    ModuloPrescale = cms.int32(100), # Only analyse 1/N events (for speed) if trigger rate permits
)

miniAODTriggerSequence = cms.Sequence(
    unpackedPatTrigger+
    miniAODTriggerAnalyzer
)

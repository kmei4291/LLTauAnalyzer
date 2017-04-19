# /users/hardenbr/displaced_jet_for80X/displacedJet_for80X/V8 (CMSSW_8_0_3)

import FWCore.ParameterSet.Config as cms

fragment = cms.ProcessFragment( "HLT" )

fragment.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/hardenbr/displaced_jet_for80X/displacedJet_for80X/V8')
)

fragment.streams = cms.PSet(  ATEST = cms.vstring( 'TEST' ) )
fragment.datasets = cms.PSet(  TEST = cms.vstring(  ) )

fragment.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
fragment.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
fragment.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
fragment.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
fragment.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
fragment.hltCaloStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::CaloSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1360, 1366 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
fragment.hltGmtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GMTSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1402 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
fragment.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    Verbosity = cms.untracked.int32( 0 ),
    EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
fragment.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
fragment.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
fragment.hltL1sHTT160IorHTT200IorHTT220IorHTT255IorHTT300IorHTT320 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_HTT160 OR L1_HTT200 OR L1_HTT220 OR L1_HTT255 OR L1_HTT300 OR L1_HTT320" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
fragment.hltPreHT200DisplacedDijet40DisplacedTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltPixelTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DcsStatusLabel = cms.untracked.InputTag( "hltScalersRawToDigi" ),
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "pixel" )
)
fragment.hltStripTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DcsStatusLabel = cms.untracked.InputTag( "hltScalersRawToDigi" ),
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "sistrip" )
)
fragment.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
fragment.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2 ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeNconst = cms.double( 28.5 ),
      ampErrorCalculation = cms.bool( False ),
      kPoorRecoFlagEB = cms.bool( True ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      useLumiInfoRunHeader = cms.bool( False ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      prefitMaxChiSqEB = cms.double( 15.0 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      timealgo = cms.string( "None" ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      EEtimeNconst = cms.double( 31.8 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      doPrefitEE = cms.bool( True ),
      doPrefitEB = cms.bool( True )
    )
)
fragment.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
fragment.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
fragment.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    FilterDataQuality = cms.bool( True ),
    silent = cms.untracked.bool( True ),
    HcalFirstFED = cms.untracked.int32( 700 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ElectronicsMap = cms.string( "" ),
    UnpackCalib = cms.untracked.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    UnpackerMode = cms.untracked.int32( 0 ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    UnpackZDC = cms.untracked.bool( True ),
    firstSample = cms.int32( 0 )
)
fragment.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    pedestalSubtractionType = cms.int32( 1 ),
    respCorrM3 = cms.double( 0.95 ),
    timeSlewParsType = cms.int32( 3 ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 3 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( True ),
    Subdetector = cms.string( "HBHE" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    pulseShapeParameters = cms.PSet( 
      MinimumChargeThreshold = cms.double( 20.0 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 0 ),
      LinearThreshold = cms.vdouble(  ),
      LinearCut = cms.vdouble(  ),
      LeftSlopeThreshold = cms.vdouble(  ),
      LeftSlopeCut = cms.vdouble(  ),
      RightSlopeCut = cms.vdouble(  ),
      RightSlopeSmallThreshold = cms.vdouble(  ),
      RightSlopeSmallCut = cms.vdouble(  ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      UseDualFit = cms.bool( False ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      R45MinusOneRange = cms.double( 0.2 ),
      RMS8MaxThreshold = cms.vdouble(  ),
      RMS8MaxCut = cms.vdouble(  ),
      RightSlopeThreshold = cms.vdouble(  )
    ),
    timingshapedcutsParameters = cms.PSet( 
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
    ),
    ts4Min = cms.double( 5.0 ),
    ts3chi2 = cms.double( 5.0 ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet( 
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      )
    ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet( 
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    )
)
fragment.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    pedestalSubtractionType = cms.int32( 1 ),
    respCorrM3 = cms.double( 0.95 ),
    timeSlewParsType = cms.int32( 3 ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 2 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet( 
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble( -10.0 ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMinWindowTime = cms.vdouble( -12.0 )
    ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 1 ),
    digistat = cms.PSet( 
      HFdigiflagFirstSample = cms.int32( 1 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 3 ),
      HFdigiflagExpectedPeak = cms.int32( 2 ),
      HFdigiflagCoef = cms.vdouble( 0.93, -0.012667, -0.38275 )
    ),
    hfTimingTrustParameters = cms.PSet( 
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    PETstat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_R_29 = cms.vdouble( 0.8 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble( 0.8 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_R = cms.vdouble( 0.98 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    correctForPhaseContainment = cms.bool( False ),
    correctForTimeslew = cms.bool( False ),
    setNoiseFlags = cms.bool( True ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HF" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 2 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    pulseShapeParameters = cms.PSet(  ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts4Min = cms.double( 5.0 ),
    ts3chi2 = cms.double( 5.0 ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
fragment.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    pedestalSubtractionType = cms.int32( 1 ),
    respCorrM3 = cms.double( 0.95 ),
    timeSlewParsType = cms.int32( 3 ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    pulseShapeParameters = cms.PSet(  ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts4Min = cms.double( 5.0 ),
    ts3chi2 = cms.double( 5.0 ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
fragment.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HcalPhase = cms.int32( 0 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    UseRejectedHitsOnly = cms.bool( False ),
    EBThreshold = cms.double( 0.07 ),
    HEDGrid = cms.vdouble(  ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
fragment.hltAK4CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    useMassDropTagger = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    subtractorName = cms.string( "" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    yMin = cms.double( -1.0 ),
    useFiltering = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    nFilt = cms.int32( -1 ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    DzTrVtxMax = cms.double( 0.0 ),
    UseOnlyOnePV = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    trimPtFracMin = cms.double( -1.0 ),
    dRMax = cms.double( -1.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False )
)
fragment.hltAK4CaloJetsIDPassed = cms.EDProducer( "HLTCaloJetIDProducer",
    min_N90 = cms.int32( -2 ),
    min_N90hits = cms.int32( 2 ),
    min_EMF = cms.double( 1.0E-6 ),
    jetsInput = cms.InputTag( "hltAK4CaloJets" ),
    JetIDParams = cms.PSet( 
      useRecHits = cms.bool( True ),
      hbheRecHitsColl = cms.InputTag( "hltHbhereco" ),
      hoRecHitsColl = cms.InputTag( "hltHoreco" ),
      hfRecHitsColl = cms.InputTag( "hltHfreco" ),
      ebRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      eeRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
    ),
    max_EMF = cms.double( 999.0 )
)
fragment.hltFixedGridRhoFastjetAllCalo = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
fragment.hltAK4CaloFastJetCorrector = cms.EDProducer( "L1FastjetCorrectorProducer",
    srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L1FastJet" )
)
fragment.hltAK4CaloRelativeCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L2Relative" )
)
fragment.hltAK4CaloAbsoluteCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L3Absolute" )
)
fragment.hltAK4CaloCorrector = cms.EDProducer( "ChainedJetCorrectorProducer",
    correctors = cms.VInputTag( 'hltAK4CaloFastJetCorrector','hltAK4CaloRelativeCorrector','hltAK4CaloAbsoluteCorrector' )
)
fragment.hltAK4CaloJetsCorrected = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltAK4CaloJets" ),
    correctors = cms.VInputTag( 'hltAK4CaloCorrector' )
)
fragment.hltAK4CaloJetsCorrectedIDPassed = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltAK4CaloJetsIDPassed" ),
    correctors = cms.VInputTag( 'hltAK4CaloCorrector' )
)
fragment.hltHtMht = cms.EDProducer( "HLTHtMhtProducer",
    usePt = cms.bool( False ),
    minPtJetHt = cms.double( 40.0 ),
    maxEtaJetMht = cms.double( 5.0 ),
    minNJetMht = cms.int32( 0 ),
    jetsLabel = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    maxEtaJetHt = cms.double( 3.0 ),
    minPtJetMht = cms.double( 30.0 ),
    minNJetHt = cms.int32( 0 ),
    pfCandidatesLabel = cms.InputTag( "" ),
    excludePFMuons = cms.bool( False )
)
fragment.hltHT200 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltHtMht' ),
    meffSlope = cms.vdouble( 1.0 ),
    minMeff = cms.vdouble( 0.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMht' ),
    minHt = cms.vdouble( 200.0 )
)
fragment.hltEmFraction0p01To0p99CaloJetSelector = cms.EDFilter( "CaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrectedIDPassed" ),
    cut = cms.string( "abs(eta)< 2 && n90 >= 3 && emEnergyFraction > 0.01 && emEnergyFraction < 0.99" )
)
fragment.hltDoubleCentralCaloJetpt40 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltEmFraction0p01To0p99CaloJetSelector" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
fragment.hltCentralCaloJetptLowPtCollectionProducer = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltDoubleCentralCaloJetpt40" )
)
fragment.hltSelectorJets20L1FastJet = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    etMin = cms.double( 20.0 )
)
fragment.hltSelectorCentralJets20L1FastJeta = cms.EDFilter( "EtaRangeCaloJetSelector",
    src = cms.InputTag( "hltSelectorJets20L1FastJet" ),
    etaMin = cms.double( -2.4 ),
    etaMax = cms.double( 2.4 )
)
fragment.hltSelector4CentralJetsL1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets20L1FastJeta" )
)
fragment.hltSiPixelDigisRegForBTag = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet( 
      inputs = cms.VInputTag( 'hltSelectorCentralJets20L1FastJeta' ),
      deltaPhi = cms.vdouble( 0.5 ),
      maxZ = cms.vdouble( 24.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    Timing = cms.untracked.bool( False ),
    CablingMapLabel = cms.string( "" ),
    UserErrorList = cms.vint32(  )
)
fragment.hltSiPixelClustersRegForBTag = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigisRegForBTag" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
fragment.hltSiPixelClustersRegForBTagCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
    onDemand = cms.bool( False )
)
fragment.hltSiPixelRecHitsRegForBTag = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
fragment.hltPixelLayerPairsRegForBTag = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltPixelLayerTripletsRegForBTag = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltFastPrimaryVertex = cms.EDProducer( "FastPrimaryVertexWithWeightsProducer",
    maxJetEta_EC = cms.double( 2.6 ),
    peakSizeY_q = cms.double( 1.0 ),
    PixelCellHeightOverWidth = cms.double( 1.8 ),
    weight_dPhi_EC = cms.double( 0.064516129 ),
    zClusterWidth_step1 = cms.double( 2.0 ),
    zClusterWidth_step2 = cms.double( 0.65 ),
    zClusterWidth_step3 = cms.double( 0.3 ),
    weight_dPhi = cms.double( 0.13888888 ),
    minJetEta_EC = cms.double( 1.3 ),
    ptWeighting = cms.bool( True ),
    maxZ = cms.double( 19.0 ),
    njets = cms.int32( 999 ),
    maxSizeX = cms.double( 2.1 ),
    ptWeighting_slope = cms.double( 0.05 ),
    weight_SizeX1 = cms.double( 0.88 ),
    clusters = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
    weightCut_step2 = cms.double( 0.05 ),
    weightCut_step3 = cms.double( 0.1 ),
    maxSizeY_q = cms.double( 2.0 ),
    endCap = cms.bool( True ),
    weight_rho_up = cms.double( 22.0 ),
    jets = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
    minSizeY_q = cms.double( -0.6 ),
    EC_weight = cms.double( 0.008 ),
    weight_charge_up = cms.double( 190000.0 ),
    maxDeltaPhi = cms.double( 0.21 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    weight_charge_down = cms.double( 11000.0 ),
    ptWeighting_offset = cms.double( -1.0 ),
    weight_charge_peak = cms.double( 22000.0 ),
    minJetPt = cms.double( 0.0 ),
    maxDeltaPhi_EC = cms.double( 0.14 ),
    zClusterSearchArea_step3 = cms.double( 0.55 ),
    barrel = cms.bool( True ),
    maxJetEta = cms.double( 2.6 ),
    pixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
    zClusterSearchArea_step2 = cms.double( 3.0 )
)
fragment.hltFastPVPixelVertexFilter = cms.EDFilter( "VertexSelector",
    filter = cms.bool( True ),
    src = cms.InputTag( "hltFastPrimaryVertex" ),
    cut = cms.string( "!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2" )
)
fragment.hltFastPVPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.0 ),
      tipMax = cms.double( 999.0 )
    ),
    passLabel = cms.string( "" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        originHalfLength = cms.double( 1.5 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        deltaPhiRegion = cms.double( 0.3 ),
        deltaEtaRegion = cms.double( 0.5 ),
        JetSrc = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
        originZPos = cms.double( 0.0 ),
        JetMaxN = cms.int32( 10 ),
        JetMinPt = cms.double( 20.0 ),
        JetMaxEta = cms.double( 2.6 ),
        vertexSrc = cms.InputTag( "hltFastPrimaryVertex" ),
        howToUseMeasurementTracker = cms.string( "Never" ),
        useMultipleScattering = cms.bool( False ),
        useFakeVertices = cms.bool( False )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersRegForBTagCache" )
        )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTripletsRegForBTag" )
    )
)
fragment.hltFastPVJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
    tracks = cms.InputTag( "hltFastPVPixelTracks" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltFastPVJetVertexChecker = cms.EDFilter( "JetVertexChecker",
    minPt = cms.double( 0.0 ),
    pvErr_x = cms.double( 0.0015 ),
    maxETA = cms.double( 2.4 ),
    maxTrackPt = cms.double( 20.0 ),
    maxNJetsToCheck = cms.int32( 2 ),
    minPtRatio = cms.double( 0.1 ),
    pvErr_y = cms.double( 0.0015 ),
    doFilter = cms.bool( False ),
    pvErr_z = cms.double( 1.5 ),
    jetTracks = cms.InputTag( "hltFastPVJetTracksAssociator" ),
    maxChi2 = cms.double( 20.0 ),
    newMethod = cms.bool( True ),
    maxNjetsOutput = cms.int32( 2 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
)
fragment.hltFastPVPixelTracksRecover = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.0 ),
      tipMax = cms.double( 999.0 )
    ),
    passLabel = cms.string( "" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        originHalfLength = cms.double( 20.0 ),
        deltaPhiRegion = cms.double( 0.5 ),
        deltaEtaRegion = cms.double( 0.5 ),
        JetSrc = cms.InputTag( "hltFastPVJetVertexChecker" ),
        vertexSrc = cms.InputTag( "hltFastPVJetVertexChecker" ),
        originZPos = cms.double( 0.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        JetMaxN = cms.int32( 10 ),
        deltaPhi = cms.double( -1.0 ),
        deltaEta = cms.double( -1.0 ),
        JetMinPt = cms.double( 20.0 ),
        JetMaxEta = cms.double( 2.5 ),
        howToUseMeasurementTracker = cms.string( "Never" ),
        useMultipleScattering = cms.bool( False ),
        useFakeVertices = cms.bool( False )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersRegForBTagCache" )
        )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTripletsRegForBTag" )
    )
)
fragment.hltFastPVPixelTracksMerger = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltFastPVPixelTracks','hltFastPVPixelTracksRecover' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltFastPVPixelTracks','hltFastPVPixelTracksRecover' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltFastPVPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForBTag" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltFastPVPixelTracksMerger" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 10.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.07 )
)
fragment.hltFastPVPixelVerticesFilter = cms.EDFilter( "VertexSelector",
    filter = cms.bool( True ),
    src = cms.InputTag( "hltFastPVPixelVertices" ),
    cut = cms.string( "!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2" )
)
fragment.hltFastPVPixelVertexSelector = cms.EDFilter( "VertexSelector",
    filter = cms.bool( True ),
    src = cms.InputTag( "hltFastPVPixelVertices" ),
    cut = cms.string( "!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2" )
)
fragment.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
fragment.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      useCMMeanMap = cms.bool( False )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    onDemand = cms.bool( True )
)
fragment.hltSiStripClustersRegForBTag = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltSiPixelClustersRegForBTag" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" )
)
fragment.hltSelectorJets30L1FastJet = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrectedIDPassed" ),
    etMin = cms.double( 30.0 )
)
fragment.hltSelectorCentralJets30L1FastJeta = cms.EDFilter( "EtaRangeCaloJetSelector",
    src = cms.InputTag( "hltSelectorJets30L1FastJet" ),
    etaMin = cms.double( -2.4 ),
    etaMax = cms.double( 2.4 )
)
fragment.hltSelector8CentralJetsL1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 8 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets30L1FastJeta" )
)
fragment.hltIter0PFlowPixelSeedsFromPixelTracksForBTag = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( True ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltFastPVPixelVertices" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltFastPVPixelTracksMerger" ),
    originRadius = cms.double( 0.1 )
)
fragment.hltIter0PFlowCkfTrackCandidatesForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0PFlowPixelSeedsFromPixelTracksForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersRegForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter0PFlowCtfWithMaterialTracksForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersRegForBTag" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter0PFlowTrackSelectionHighPurityForBTag = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracksForBTag" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltFastPVPixelVertices" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducer" ),
    tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerLowPt = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPLowPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL3DisplacedDijet100FullTracksTrackIPProducerLowPt' )
)
fragment.hltTwoPromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterLowPt = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 2 ),
    JetTags = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTagProducerFromIPLowPt" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducer" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 2.5 )
)
fragment.hltDisplacedHLTCaloJetCollectionProducerLowPt = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltTwoPromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterLowPt" )
)
fragment.hltIter1ClustersRefRemovalForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter1MaskedMeasurementTrackerEventForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter1ClustersRefRemovalForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersRegForBTag" )
)
fragment.hltIter1PixelLayerTripletsForBTag = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.0036 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalForBTag" ),
      hitErrorRPhi = cms.double( 0.0051 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.006 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ClustersRefRemovalForBTag" ),
      hitErrorRPhi = cms.double( 0.0027 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter1PFlowPixelSeedsForBTag = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.05 ),
        vertexSrc = cms.InputTag( "hltFastPVPixelVertices" ),
        searchOpt = cms.bool( True ),
        ptMin = cms.double( 0.5 ),
        mode = cms.string( "VerticesFixed" ),
        maxNRegions = cms.int32( 10 ),
        maxNVertices = cms.int32( 1 ),
        deltaPhi = cms.double( 0.5 ),
        deltaEta = cms.double( 0.5 ),
        zErrorBeamSpot = cms.double( 15.0 ),
        nSigmaZBeamSpot = cms.double( 3.0 ),
        zErrorVetex = cms.double( 0.1 ),
        vertexCollection = cms.InputTag( "hltFastPVPixelVertices" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        input = cms.InputTag( "hltSelector8CentralJetsL1FastJet" ),
        measurementTrackerName = cms.InputTag( "hltIter1MaskedMeasurementTrackerEventForBTag" ),
        whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
        useMultipleScattering = cms.bool( False ),
        useFakeVertices = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersRegForBTag" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.037 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltIter1PixelLayerTripletsForBTag" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsTripletOnlyCreator" ) )
)
fragment.hltIter1PFlowCkfTrackCandidatesForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter1PFlowPixelSeedsForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEventForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter1PFlowCtfWithMaterialTracksForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter1PFlowCkfTrackCandidatesForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEventForBTag" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter1PFlowTrackSelectionHighPurityLooseForBTag = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.9, 3.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.8, 3.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracksForBTag" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltFastPVPixelVertices" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.9, 3.0 ),
    d0_par1 = cms.vdouble( 0.85, 3.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter1PFlowTrackSelectionHighPurityTightForBTag = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 0.4 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 1.0, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 1.0, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracksForBTag" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltFastPVPixelVertices" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 1.0, 4.0 ),
    d0_par1 = cms.vdouble( 1.0, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter1PFlowTrackSelectionHighPurityForBTag = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1PFlowTrackSelectionHighPurityLooseForBTag','hltIter1PFlowTrackSelectionHighPurityTightForBTag' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1PFlowTrackSelectionHighPurityLooseForBTag','hltIter1PFlowTrackSelectionHighPurityTightForBTag' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter1MergedForBTag = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurityForBTag','hltIter1PFlowTrackSelectionHighPurityForBTag' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurityForBTag','hltIter1PFlowTrackSelectionHighPurityForBTag' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter2ClustersRefRemovalForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltIter1PFlowTrackSelectionHighPurityForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter1ClustersRefRemovalForBTag" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter2MaskedMeasurementTrackerEventForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2ClustersRefRemovalForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersRegForBTag" )
)
fragment.hltIter2PixelLayerPairsForBTag = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.0036 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalForBTag" ),
      hitErrorRPhi = cms.double( 0.0051 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHitsRegForBTag" ),
      hitErrorRZ = cms.double( 0.006 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ClustersRefRemovalForBTag" ),
      hitErrorRPhi = cms.double( 0.0027 )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter2PFlowPixelSeedsForBTag = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.025 ),
        searchOpt = cms.bool( True ),
        ptMin = cms.double( 1.2 ),
        mode = cms.string( "VerticesFixed" ),
        maxNRegions = cms.int32( 10 ),
        maxNVertices = cms.int32( 1 ),
        deltaPhi = cms.double( 0.5 ),
        deltaEta = cms.double( 0.5 ),
        zErrorBeamSpot = cms.double( 15.0 ),
        nSigmaZBeamSpot = cms.double( 3.0 ),
        zErrorVetex = cms.double( 0.05 ),
        vertexCollection = cms.InputTag( "hltFastPVPixelVertices" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        input = cms.InputTag( "hltSelector8CentralJetsL1FastJet" ),
        measurementTrackerName = cms.InputTag( "hltIter2MaskedMeasurementTrackerEventForBTag" ),
        whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
        useMultipleScattering = cms.bool( False ),
        useFakeVertices = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersRegForBTag" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 100000 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltIter2PixelLayerPairsForBTag" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreatorIT" ) )
)
fragment.hltIter2PFlowCkfTrackCandidatesForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2PFlowPixelSeedsForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEventForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter2PFlowCtfWithMaterialTracksForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2PFlowCkfTrackCandidatesForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEventForBTag" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter2PFlowTrackSelectionHighPurityForBTag = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracksForBTag" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltFastPVPixelVertices" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter2MergedForBTag = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1MergedForBTag','hltIter2PFlowTrackSelectionHighPurityForBTag' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1MergedForBTag','hltIter2PFlowTrackSelectionHighPurityForBTag' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexLowPt = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPt" ),
    tracks = cms.InputTag( "hltIter2MergedForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerLowPt = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 0.5 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexLowPt" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPLowPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL4PromptDisplacedDijetFullTracksTrackIPProducerLowPt' )
)
fragment.hltL4PromptDisplacedDijetFullTracksHLTCaloJetTagFilterLowPt = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 2 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPLowPt" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPt" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 2.5 )
)
fragment.hltIter02DisplacedHLTCaloJetCollectionProducerLowPt = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksHLTCaloJetTagFilterLowPt" )
)
fragment.hltDisplacedhltTrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltFastPVPixelVertices" )
)
fragment.hltDisplacedhltIter4ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2PFlowTrackSelectionHighPurityForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2ClustersRefRemovalForBTag" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltDisplacedhltIter4MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersRegForBTag" )
)
fragment.hltDisplacedhltIter4PixelLessLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TIB1+TIB2+MTIB3',
      'TIB1+TIB2+MTID1_pos',
      'TIB1+TIB2+MTID1_neg',
      'TID1_pos+TID2_pos+TID3_pos',
      'TID1_neg+TID2_neg+TID3_neg',
      'TID1_pos+TID2_pos+MTID3_pos',
      'TID1_neg+TID2_neg+MTID3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
      useRingSlector = cms.bool( True ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 2 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    MTID = cms.PSet( 
      skipClusters = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 3 ),
      maxRing = cms.int32( 3 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
      useRingSlector = cms.bool( True ),
      minRing = cms.int32( 3 ),
      maxRing = cms.int32( 3 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    MTIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    TID = cms.PSet( 
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 2 ),
      skipClusters = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltDisplacedhltIter4ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    )
)
fragment.hltDisplacedhltIter4PFlowPixelLessSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 1.0 ),
        vertexSrc = cms.InputTag( "hltDisplacedhltTrimmedPixelVertices" ),
        searchOpt = cms.bool( True ),
        ptMin = cms.double( 0.8 ),
        mode = cms.string( "VerticesFixed" ),
        maxNRegions = cms.int32( 100 ),
        maxNVertices = cms.int32( 10 ),
        deltaPhi = cms.double( 0.5 ),
        deltaEta = cms.double( 0.5 ),
        vertexCollection = cms.InputTag( "hltDisplacedhltTrimmedPixelVertices" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        input = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
        zErrorBeamSpot = cms.double( 15.0 ),
        nSigmaZBeamSpot = cms.double( 3.0 ),
        zErrorVetex = cms.double( 12.0 ),
        measurementTrackerName = cms.InputTag( "hltDisplacedhltIter4MaskedMeasurementTrackerEvent" ),
        whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
        useMultipleScattering = cms.bool( False ),
        useFakeVertices = cms.bool( False )
      ),
      RegionPsetFomBeamSpotBlockFixedZ = cms.PSet( 
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        RegionPSet = cms.PSet( 
          precise = cms.bool( True ),
          originHalfLength = cms.double( 21.2 ),
          originRadius = cms.double( 0.2 ),
          ptMin = cms.double( 0.9 ),
          beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
        )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( True ),
      FilterPixelHits = cms.bool( False ),
      FilterStripHits = cms.bool( False ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" )
    ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersRegForBTag" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersRegForBTag" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardMultiHitGenerator" ),
      GeneratorPSet = cms.PSet( 
        ComponentName = cms.string( "MultiHitGeneratorFromChi2" ),
        useFixedPreFiltering = cms.bool( False ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        extraHitRZtolerance = cms.double( 0.0 ),
        extraZKDBox = cms.double( 0.2 ),
        extraRKDBox = cms.double( 0.2 ),
        extraPhiKDBox = cms.double( 0.005 ),
        fnSigmaRZ = cms.double( 2.0 ),
        refitHits = cms.bool( True ),
        ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
        maxChi2 = cms.double( 5.0 ),
        chi2VsPtCut = cms.bool( True ),
        pt_interv = cms.vdouble( 0.4, 0.7, 1.0, 2.0 ),
        chi2_cuts = cms.vdouble( 3.0, 4.0, 5.0, 5.0 ),
        debug = cms.bool( False ),
        detIdsToDebug = cms.vint32( 0, 0, 0 ),
        maxElement = cms.uint32( 100000 ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
      ),
      SeedingLayers = cms.InputTag( "hltDisplacedhltIter4PixelLessLayerTriplets" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsTripletOnlyCreator" ) )
)
fragment.hltDisplacedhltIter4PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltDisplacedhltIter4PFlowPixelLessSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDisplacedhltIter4MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltDisplacedhltIter4PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltDisplacedhltIter4PFlowCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDisplacedhltIter4MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltDisplacedhltIter4PFlowTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 0.25 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 1.0, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 1.0, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 0 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltDisplacedhltIter4PFlowCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltDisplacedhltTrimmedPixelVertices" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 1.0, 4.0 ),
    d0_par1 = cms.vdouble( 1.0, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
fragment.hltIter4MergedWithIter012DisplacedJets = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2MergedForBTag','hltDisplacedhltIter4PFlowTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2MergedForBTag','hltDisplacedhltIter4PFlowTrackSelectionHighPurity' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerLowPt" ),
    tracks = cms.InputTag( "hltIter4MergedWithIter012DisplacedJets" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerLowPt = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 9999999.0 ),
    minimumNumberOfHits = cms.int32( 6 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltDisplacedhltTrimmedPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 5.0 )
)
fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPLowPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltTrackCounting2D1st" ),
    tagInfos = cms.VInputTag( 'hltL4TaggedDisplacedDijetFullTracksTrackIPProducerLowPt' )
)
fragment.hltL4DisplacedDijetFullTracksHLTCaloJetTagFilterLowPt = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 2 ),
    JetTags = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTagProducerFromIPLowPt" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerLowPt" ),
    MinTag = cms.double( 5.0 ),
    MaxTag = cms.double( 999999.0 )
)
fragment.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
fragment.hltPreHT250DisplacedDijet40DisplacedTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltHT250 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltHtMht' ),
    meffSlope = cms.vdouble( 1.0 ),
    minMeff = cms.vdouble( 0.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMht' ),
    minHt = cms.vdouble( 250.0 )
)
fragment.hltPreHT350DisplacedDijet40Inclusive = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltHT350 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltHtMht' ),
    meffSlope = cms.vdouble( 1.0 ),
    minMeff = cms.vdouble( 0.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMht' ),
    minHt = cms.vdouble( 350.0 )
)
fragment.hltPreHT400DisplacedDijet40Inclusive = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltHT400 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltHtMht' ),
    meffSlope = cms.vdouble( 1.0 ),
    minMeff = cms.vdouble( 0.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMht' ),
    minHt = cms.vdouble( 400.0 )
)
fragment.hltL1sTripleJet927664VBFIorHTT300 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_TripleJet_92_76_64_VBF  OR L1_HTT300" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
fragment.hltPreVBFDisplacedJet40DisplacedTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltVBFFilterDisplacedJetsTight = cms.EDFilter( "HLTCaloJetVBFFilter",
    saveTags = cms.bool( True ),
    minDeltaEta = cms.double( 3.0 ),
    leadingJetOnly = cms.bool( False ),
    maxEta = cms.double( 5.0 ),
    inputTag = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    etaOpposite = cms.bool( True ),
    triggerType = cms.int32( 85 ),
    minInvMass = cms.double( 500.0 ),
    minPtHigh = cms.double( 20.0 ),
    minPtLow = cms.double( 20.0 )
)
fragment.hltSingleCentralCaloJetpt40 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltEmFraction0p01To0p99CaloJetSelector" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
fragment.hltSingleCentralCaloJetpt40CollectionProducer = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltSingleCentralCaloJetpt40" )
)
fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSingleCentralCaloJetpt40CollectionProducer" ),
    tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerFromVBF = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPFromVBF = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL3DisplacedDijet100FullTracksTrackIPProducerFromVBF' )
)
fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterFromVBF = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltSingleCentralCaloJetpt40CollectionProducer" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterFromVBF" )
)
fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexFromVBF = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerFromVBF" ),
    tracks = cms.InputTag( "hltIter2MergedForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerFromVBF = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 0.5 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexFromVBF" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPFromVBF = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducerLong" ),
    tagInfos = cms.VInputTag( 'hltL4PromptDisplacedDijetFullTracksTrackIPProducerFromVBF' )
)
fragment.hltL4PromptDisplacedDijetFullTracksHLTCaloJetTagFilterFromVBF = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerFromVBF" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksHLTCaloJetTagFilterFromVBF" )
)
fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF" ),
    tracks = cms.InputTag( "hltIter4MergedWithIter012DisplacedJets" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 9999999.0 ),
    minimumNumberOfHits = cms.int32( 6 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltDisplacedhltTrimmedPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 5.0 )
)
fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltTrackCounting2D2ndLong" ),
    tagInfos = cms.VInputTag( 'hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF' )
)
fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBF = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF" ),
    MinTag = cms.double( 7.0 ),
    MaxTag = cms.double( 999999.0 )
)
fragment.hltTripleJet50 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 50.0 ),
    MinN = cms.int32( 3 ),
    MaxEta = cms.double( 5.2 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
fragment.hltDoubleJet65 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 65.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 5.2 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
fragment.hltSingleJet80 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 80.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.2 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 86 )
)
fragment.hltPreVBFDisplacedJet40DisplacedTrack2TrackIP2DSig5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBF2DIP5p0 = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF" ),
    MinTag = cms.double( 5.0 ),
    MaxTag = cms.double( 999999.0 )
)
fragment.hltPreVBFDisplacedJet40TightIDDisplacedTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBFTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF" ),
    MinTag = cms.double( 9.0 ),
    MaxTag = cms.double( 999999.0 )
)
fragment.hltPreVBFDisplacedJet40Hadronic = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltVBFFilterDisplacedJets = cms.EDFilter( "HLTCaloJetVBFFilter",
    saveTags = cms.bool( True ),
    minDeltaEta = cms.double( 3.0 ),
    leadingJetOnly = cms.bool( False ),
    maxEta = cms.double( 5.0 ),
    inputTag = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    etaOpposite = cms.bool( True ),
    triggerType = cms.int32( 85 ),
    minInvMass = cms.double( 400.0 ),
    minPtHigh = cms.double( 20.0 ),
    minPtLow = cms.double( 20.0 )
)
fragment.hltHighHadFractionCaloJetSelector = cms.EDFilter( "CaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    cut = cms.string( "abs(eta) < 2 && (( energyFractionHadronic > 0.85 && ( n90 < 12 && n60 < 6 && towersArea < 0.20 )) || energyFractionHadronic > .98)" )
)
fragment.hltCentralHadronCaloJetpt40 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltHighHadFractionCaloJetSelector" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
fragment.hltCentralHadronCaloJetpt40CollectionProducer = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltCentralHadronCaloJetpt40" )
)
fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJets = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducer" ),
    tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJets = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJets" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJets = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJets' )
)
fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJets = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJets" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducer" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltDisplacedHLTHadronJetCollectionProducer = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJets" )
)
fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJets = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducer" ),
    tracks = cms.InputTag( "hltIter2MergedForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJets = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 0.5 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJets" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJets = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJets' )
)
fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilter = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJets" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducer" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltPreVBFDisplacedJet40Hadronic2PromptTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilter2PromptTracks = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJets" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducer" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 2.5 )
)
fragment.hltPreVBFDisplacedJet40TightIDHadronic = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltHighHadFractionCaloJetSelectorTightID = cms.EDFilter( "CaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    cut = cms.string( "abs(eta) < 2 && (( energyFractionHadronic > 0.88 && ( n90 < 10 && n60 < 5 && towersArea < 0.18 )) || energyFractionHadronic > .98)" )
)
fragment.hltCentralHadronCaloJetpt40TightID = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltHighHadFractionCaloJetSelectorTightID" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
fragment.hltCentralHadronCaloJetpt40CollectionProducerTightID = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltCentralHadronCaloJetpt40TightID" )
)
fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsTightID = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducerTightID" ),
    tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsTightID = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsTightID" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsTightID = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsTightID' )
)
fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsTightID" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducerTightID" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltDisplacedHLTHadronJetCollectionProducerTightID = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsTightID" )
)
fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsTightID = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducerTightID" ),
    tracks = cms.InputTag( "hltIter2MergedForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsTightID = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 0.5 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsTightID" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsTightID = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsTightID' )
)
fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsTightID" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducerTightID" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltPreVBFDisplacedJet40VTightIDHadronic = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltHighHadFractionCaloJetSelectorVTightID = cms.EDFilter( "CaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    cut = cms.string( "abs(eta) < 2 && (( energyFractionHadronic > 0.90 && ( n90 < 8 && n60 < 5 && towersArea < 0.18 )) || energyFractionHadronic > .99)" )
)
fragment.hltCentralHadronCaloJetpt40VTightID = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltHighHadFractionCaloJetSelectorVTightID" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
fragment.hltCentralHadronCaloJetpt40CollectionProducerVTightID = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltCentralHadronCaloJetpt40VTightID" )
)
fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsVTightID = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducerVTightID" ),
    tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsVTightID = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsVTightID" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVTightID = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsVTightID' )
)
fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsVTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVTightID" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducerVTightID" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltDisplacedHLTHadronJetCollectionProducerVTightID = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsVTightID" )
)
fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsVTightID = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducerVTightID" ),
    tracks = cms.InputTag( "hltIter2MergedForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsVTightID = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 0.5 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsVTightID" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVTightID = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsVTightID' )
)
fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterVTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVTightID" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducerVTightID" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltPreVBFDisplacedJet40VVTightIDHadronic = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltHighHadFractionCaloJetSelectorVVTightID = cms.EDFilter( "CaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    cut = cms.string( "abs(eta) < 2 && (( energyFractionHadronic > 0.93 && ( n90 < 8 && n60 < 5 && towersArea < 0.18 )) || energyFractionHadronic > .99)" )
)
fragment.hltCentralHadronCaloJetpt40VVTightID = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltHighHadFractionCaloJetSelectorVVTightID" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
fragment.hltCentralHadronCaloJetpt40CollectionProducerVVTightID = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltCentralHadronCaloJetpt40VVTightID" )
)
fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsVVTightID = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducerVVTightID" ),
    tracks = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurityForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsVVTightID = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsVVTightID" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVVTightID = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsVVTightID' )
)
fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsVVTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVVTightID" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltCentralHadronCaloJetpt40CollectionProducerVVTightID" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltDisplacedHLTHadronJetCollectionProducerVVTightID = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 85 ),
    HLTObject = cms.InputTag( "hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsVVTightID" )
)
fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsVVTightID = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducerVVTightID" ),
    tracks = cms.InputTag( "hltIter2MergedForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsVVTightID = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.1 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 0.5 ),
    primaryVertex = cms.InputTag( "hltFastPVPixelVertices" ),
    maximumLongitudinalImpactParameter = cms.double( 0.1 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsVVTightID" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVVTightID = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPDisplacedDijethltPromptTrackCountingESProducer" ),
    tagInfos = cms.VInputTag( 'hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsVVTightID' )
)
fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterVVTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVVTightID" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltDisplacedHLTHadronJetCollectionProducerVVTightID" ),
    MinTag = cms.double( -999999.0 ),
    MaxTag = cms.double( 1.5 )
)
fragment.hltPreVBFDisplacedJet40VTightIDDisplacedTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBFVTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF" ),
    MinTag = cms.double( 22.0 ),
    MaxTag = cms.double( 999999.0 )
)
fragment.hltPreVBFDisplacedJet40VVTightIDDisplacedTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBFVVTightID = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF" ),
    TriggerType = cms.int32( 85 ),
    Jets = cms.InputTag( "hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF" ),
    MinTag = cms.double( 25.0 ),
    MaxTag = cms.double( 999999.0 )
)

fragment.HLTL1UnpackerSequence = cms.Sequence( fragment.hltGtStage2Digis + fragment.hltCaloStage2Digis + fragment.hltGmtStage2Digis + fragment.hltGtStage2ObjectMap )
fragment.HLTBeamSpot = cms.Sequence( fragment.hltScalersRawToDigi + fragment.hltOnlineBeamSpot )
fragment.HLTBeginSequence = cms.Sequence( fragment.hltTriggerType + fragment.HLTL1UnpackerSequence + fragment.HLTBeamSpot )
fragment.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( fragment.hltEcalDigis + fragment.hltEcalUncalibRecHit + fragment.hltEcalDetIdToBeRecovered + fragment.hltEcalRecHit )
fragment.HLTDoLocalHcalSequence = cms.Sequence( fragment.hltHcalDigis + fragment.hltHbhereco + fragment.hltHfreco + fragment.hltHoreco )
fragment.HLTDoCaloSequence = cms.Sequence( fragment.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + fragment.HLTDoLocalHcalSequence + fragment.hltTowerMakerForAll )
fragment.HLTAK4CaloJetsReconstructionSequence = cms.Sequence( fragment.HLTDoCaloSequence + fragment.hltAK4CaloJets + fragment.hltAK4CaloJetsIDPassed )
fragment.HLTAK4CaloCorrectorProducersSequence = cms.Sequence( fragment.hltAK4CaloFastJetCorrector + fragment.hltAK4CaloRelativeCorrector + fragment.hltAK4CaloAbsoluteCorrector + fragment.hltAK4CaloCorrector )
fragment.HLTAK4CaloJetsCorrectionSequence = cms.Sequence( fragment.hltFixedGridRhoFastjetAllCalo + fragment.HLTAK4CaloCorrectorProducersSequence + fragment.hltAK4CaloJetsCorrected + fragment.hltAK4CaloJetsCorrectedIDPassed )
fragment.HLTAK4CaloJetsSequence = cms.Sequence( fragment.HLTAK4CaloJetsReconstructionSequence + fragment.HLTAK4CaloJetsCorrectionSequence )
fragment.HLTDoLocalPixelSequenceRegForBTag = cms.Sequence( fragment.hltSiPixelDigisRegForBTag + fragment.hltSiPixelClustersRegForBTag + fragment.hltSiPixelClustersRegForBTagCache + fragment.hltSiPixelRecHitsRegForBTag + fragment.hltPixelLayerPairsRegForBTag + fragment.hltPixelLayerTripletsRegForBTag )
fragment.HLTFastRecopixelvertexingSequence = cms.Sequence( fragment.hltFastPrimaryVertex + fragment.hltFastPVPixelVertexFilter + fragment.hltFastPVPixelTracks + fragment.hltFastPVJetTracksAssociator + fragment.hltFastPVJetVertexChecker + fragment.hltFastPVPixelTracksRecover + fragment.hltFastPVPixelTracksMerger + fragment.hltFastPVPixelVertices + fragment.hltFastPVPixelVerticesFilter )
fragment.HLTFastPrimaryVertexSequence = cms.Sequence( fragment.hltSelectorJets20L1FastJet + fragment.hltSelectorCentralJets20L1FastJeta + fragment.hltSelector4CentralJetsL1FastJet + fragment.HLTDoLocalPixelSequenceRegForBTag + fragment.HLTFastRecopixelvertexingSequence )
fragment.HLTDoLocalStripSequenceRegForBTag = cms.Sequence( fragment.hltSiStripExcludedFEDListProducer + fragment.hltSiStripRawToClustersFacility + fragment.hltSiStripClustersRegForBTag )
fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets = cms.Sequence( fragment.HLTFastPrimaryVertexSequence + fragment.hltFastPVPixelVertexSelector + fragment.HLTDoLocalPixelSequenceRegForBTag + fragment.HLTDoLocalStripSequenceRegForBTag + fragment.hltSelectorJets30L1FastJet + fragment.hltSelectorCentralJets30L1FastJeta + fragment.hltSelector8CentralJetsL1FastJet )
fragment.HLTIterativeTrackingForBTagIteration0 = cms.Sequence( fragment.hltIter0PFlowPixelSeedsFromPixelTracksForBTag + fragment.hltIter0PFlowCkfTrackCandidatesForBTag + fragment.hltIter0PFlowCtfWithMaterialTracksForBTag + fragment.hltIter0PFlowTrackSelectionHighPurityForBTag )
fragment.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt = cms.Sequence( fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt + fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerLowPt + fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPLowPt + fragment.hltTwoPromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterLowPt )
fragment.HLTIterativeTrackingForBTagIteration1 = cms.Sequence( fragment.hltIter1ClustersRefRemovalForBTag + fragment.hltIter1MaskedMeasurementTrackerEventForBTag + fragment.hltIter1PixelLayerTripletsForBTag + fragment.hltIter1PFlowPixelSeedsForBTag + fragment.hltIter1PFlowCkfTrackCandidatesForBTag + fragment.hltIter1PFlowCtfWithMaterialTracksForBTag + fragment.hltIter1PFlowTrackSelectionHighPurityLooseForBTag + fragment.hltIter1PFlowTrackSelectionHighPurityTightForBTag + fragment.hltIter1PFlowTrackSelectionHighPurityForBTag )
fragment.HLTIterativeTrackingForBTagIteration2 = cms.Sequence( fragment.hltIter2ClustersRefRemovalForBTag + fragment.hltIter2MaskedMeasurementTrackerEventForBTag + fragment.hltIter2PixelLayerPairsForBTag + fragment.hltIter2PFlowPixelSeedsForBTag + fragment.hltIter2PFlowCkfTrackCandidatesForBTag + fragment.hltIter2PFlowCtfWithMaterialTracksForBTag + fragment.hltIter2PFlowTrackSelectionHighPurityForBTag )
fragment.HLTIterativeTrackingForBTagIter12 = cms.Sequence( fragment.HLTIterativeTrackingForBTagIteration1 + fragment.hltIter1MergedForBTag + fragment.HLTIterativeTrackingForBTagIteration2 + fragment.hltIter2MergedForBTag )
fragment.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexLowPt + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerLowPt + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPLowPt + fragment.hltL4PromptDisplacedDijetFullTracksHLTCaloJetTagFilterLowPt )
fragment.HLTIterativeTrackingIteration4DisplacedJets = cms.Sequence( fragment.hltDisplacedhltTrimmedPixelVertices + fragment.hltDisplacedhltIter4ClustersRefRemoval + fragment.hltDisplacedhltIter4MaskedMeasurementTrackerEvent + fragment.hltDisplacedhltIter4PixelLessLayerTriplets + fragment.hltDisplacedhltIter4PFlowPixelLessSeeds + fragment.hltDisplacedhltIter4PFlowCkfTrackCandidates + fragment.hltDisplacedhltIter4PFlowCtfWithMaterialTracks + fragment.hltDisplacedhltIter4PFlowTrackSelectionHighPurity + fragment.hltIter4MergedWithIter012DisplacedJets )
fragment.HLTDisplacedTrackRequirementDisplacedJetsLowPt = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexLowPt + fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerLowPt + fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPLowPt + fragment.hltL4DisplacedDijetFullTracksHLTCaloJetTagFilterLowPt )
fragment.HLTEndSequence = cms.Sequence( fragment.hltBoolEnd )
fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF = cms.Sequence( fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF + fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerFromVBF + fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterFromVBF )
fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexFromVBF + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerFromVBF + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltL4PromptDisplacedDijetFullTracksHLTCaloJetTagFilterFromVBF )
fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBF = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF + fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF + fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBF )
fragment.HLTTripleJet50Jet65Jet80Sequence = cms.Sequence( fragment.hltTripleJet50 + fragment.hltDoubleJet65 + fragment.hltSingleJet80 )
fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBF2DIP5p0 = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF + fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF + fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBF2DIP5p0 )
fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFTightID = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF + fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF + fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBFTightID )
fragment.HLT2PromptTrackRequirementIter0HadronJets = cms.Sequence( fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJets + fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJets + fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJets + fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJets )
fragment.HLTPromptTrackRequirementIter12HadronJets = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJets + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJets + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJets + fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilter )
fragment.HLTPromptTrackRequirementIter12HadronJets2PromptTracks = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJets + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJets + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJets + fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilter2PromptTracks )
fragment.HLT2PromptTrackRequirementIter0HadronJetsTightID = cms.Sequence( fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsTightID + fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsTightID + fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsTightID + fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsTightID )
fragment.HLTPromptTrackRequirementIter12HadronJetsTightID = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsTightID + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsTightID + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsTightID + fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterTightID )
fragment.HLT2PromptTrackRequirementIter0HadronJetsVTightID = cms.Sequence( fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsVTightID + fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsVTightID + fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVTightID + fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsVTightID )
fragment.HLTPromptTrackRequirementIter12HadronJetsVTightID = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsVTightID + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsVTightID + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVTightID + fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterVTightID )
fragment.HLT2PromptTrackRequirementIter0HadronJetsVVTightID = cms.Sequence( fragment.hltL3DisplacedDijetFullTracksJetTracksAssociatorAtVertexForHadronJetsVVTightID + fragment.hltL3DisplacedDijet100FullTracksTrackIPProducerForHadronJetsVVTightID + fragment.hltL3DisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVVTightID + fragment.hltOnePromptHLTL3DisplacedDijetFullTracksHLTCaloJetTagFilterForHadronJetsVVTightID )
fragment.HLTPromptTrackRequirementIter12HadronJetsVVTightID = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetPromptTracksAssociatorAtVertexForHadronJetsVVTightID + fragment.hltL4PromptDisplacedDijetFullTracksTrackIPProducerForHadronJetsVVTightID + fragment.hltL4PromptDisplacedDijetFullTracksJetTagProducerFromIPForHadronJetsVVTightID + fragment.hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterVVTightID )
fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFVTightID = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF + fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF + fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBFVTightID )
fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFVVTightID = cms.Sequence( fragment.hltL4DisplacedDijetFullTracksJetTracksAssociatorAtVertexFromVBF + fragment.hltL4TaggedDisplacedDijetFullTracksTrackIPProducerFromVBF + fragment.hltL4DisplacedDijetFullTracksJetTagProducerFromIPFromVBF + fragment.hltL4DisplacedDijetFullTracksTightHLTCaloJetTagFilterFromVBFVVTightID )

fragment.HLTriggerFirstPath = cms.Path( fragment.hltGetConditions + fragment.hltGetRaw + fragment.hltBoolFalse )
fragment.HLT_HT200_DisplacedDijet40_DisplacedTrack_v1 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sHTT160IorHTT200IorHTT220IorHTT255IorHTT300IorHTT320 + fragment.hltPreHT200DisplacedDijet40DisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltHtMht + fragment.hltHT200 + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltDoubleCentralCaloJetpt40 + fragment.hltCentralCaloJetptLowPtCollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt + fragment.hltDisplacedHLTCaloJetCollectionProducerLowPt + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerLowPt + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTrackRequirementDisplacedJetsLowPt + fragment.HLTEndSequence )
fragment.HLT_HT250_DisplacedDijet40_DisplacedTrack_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sHTT160IorHTT200IorHTT220IorHTT255IorHTT300IorHTT320 + fragment.hltPreHT250DisplacedDijet40DisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltHtMht + fragment.hltHT250 + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltDoubleCentralCaloJetpt40 + fragment.hltCentralCaloJetptLowPtCollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt + fragment.hltDisplacedHLTCaloJetCollectionProducerLowPt + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerLowPt + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTrackRequirementDisplacedJetsLowPt + fragment.HLTEndSequence )
fragment.HLT_HT350_DisplacedDijet40_Inclusive_v1 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sHTT160IorHTT200IorHTT220IorHTT255IorHTT300IorHTT320 + fragment.hltPreHT350DisplacedDijet40Inclusive + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltHtMht + fragment.hltHT350 + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltDoubleCentralCaloJetpt40 + fragment.hltCentralCaloJetptLowPtCollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt + fragment.hltDisplacedHLTCaloJetCollectionProducerLowPt + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt + fragment.HLTEndSequence )
fragment.HLT_HT400_DisplacedDijet40_Inclusive_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sHTT160IorHTT200IorHTT220IorHTT255IorHTT300IorHTT320 + fragment.hltPreHT400DisplacedDijet40Inclusive + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltHtMht + fragment.hltHT400 + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltDoubleCentralCaloJetpt40 + fragment.hltCentralCaloJetptLowPtCollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsLowPt + fragment.hltDisplacedHLTCaloJetCollectionProducerLowPt + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsLowPt + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40DisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBF + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40DisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBF + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40DisplacedTrack2TrackIP2DSig5 + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBF2DIP5p0 + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40DisplacedTrack2TrackIP2DSig5 + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBF2DIP5p0 + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40TightIDDisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40TightIDDisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_Hadronic_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40Hadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelector + fragment.hltCentralHadronCaloJetpt40 + fragment.hltCentralHadronCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJets + fragment.hltDisplacedHLTHadronJetCollectionProducer + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJets + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_Hadronic_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40Hadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelector + fragment.hltCentralHadronCaloJetpt40 + fragment.hltCentralHadronCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJets + fragment.hltDisplacedHLTHadronJetCollectionProducer + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJets + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40Hadronic2PromptTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelector + fragment.hltCentralHadronCaloJetpt40 + fragment.hltCentralHadronCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJets + fragment.hltDisplacedHLTHadronJetCollectionProducer + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJets2PromptTracks + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40Hadronic2PromptTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelector + fragment.hltCentralHadronCaloJetpt40 + fragment.hltCentralHadronCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJets + fragment.hltDisplacedHLTHadronJetCollectionProducer + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJets2PromptTracks + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_TightID_Hadronic_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40TightIDHadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelectorTightID + fragment.hltCentralHadronCaloJetpt40TightID + fragment.hltCentralHadronCaloJetpt40CollectionProducerTightID + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJetsTightID + fragment.hltDisplacedHLTHadronJetCollectionProducerTightID + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJetsTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_TightID_Hadronic_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40TightIDHadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelectorTightID + fragment.hltCentralHadronCaloJetpt40TightID + fragment.hltCentralHadronCaloJetpt40CollectionProducerTightID + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJetsTightID + fragment.hltDisplacedHLTHadronJetCollectionProducerTightID + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJetsTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VTightID_Hadronic_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VTightIDHadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelectorVTightID + fragment.hltCentralHadronCaloJetpt40VTightID + fragment.hltCentralHadronCaloJetpt40CollectionProducerVTightID + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJetsVTightID + fragment.hltDisplacedHLTHadronJetCollectionProducerVTightID + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJetsVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VTightID_Hadronic_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VTightIDHadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelectorVTightID + fragment.hltCentralHadronCaloJetpt40VTightID + fragment.hltCentralHadronCaloJetpt40CollectionProducerVTightID + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJetsVTightID + fragment.hltDisplacedHLTHadronJetCollectionProducerVTightID + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJetsVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VVTightIDHadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelectorVVTightID + fragment.hltCentralHadronCaloJetpt40VVTightID + fragment.hltCentralHadronCaloJetpt40CollectionProducerVVTightID + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJetsVVTightID + fragment.hltDisplacedHLTHadronJetCollectionProducerVVTightID + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJetsVVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VVTightIDHadronic + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJets + fragment.hltHighHadFractionCaloJetSelectorVVTightID + fragment.hltCentralHadronCaloJetpt40VVTightID + fragment.hltCentralHadronCaloJetpt40CollectionProducerVVTightID + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0HadronJetsVVTightID + fragment.hltDisplacedHLTHadronJetCollectionProducerVVTightID + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLTPromptTrackRequirementIter12HadronJetsVVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VTightIDDisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VTightIDDisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v2 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VVTightIDDisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFVVTightID + fragment.HLTEndSequence )
fragment.HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v3 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sTripleJet927664VBFIorHTT300 + fragment.hltPreVBFDisplacedJet40VVTightIDDisplacedTrack + fragment.hltPixelTrackerHVOn + fragment.hltStripTrackerHVOn + fragment.HLTAK4CaloJetsSequence + fragment.HLTTripleJet50Jet65Jet80Sequence + fragment.hltVBFFilterDisplacedJetsTight + fragment.hltEmFraction0p01To0p99CaloJetSelector + fragment.hltSingleCentralCaloJetpt40 + fragment.hltSingleCentralCaloJetpt40CollectionProducer + fragment.HLTBTagPixelAndStripSetupForInclusiveDisplacedJets + fragment.HLTIterativeTrackingForBTagIteration0 + fragment.HLT2PromptTrackRequirementIter0DisplacedJetsFromVBF + fragment.hltDisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingForBTagIter12 + fragment.HLT2PromptTrackRequirementIter12DisplacedJetsFromVBF + fragment.hltIter02DisplacedHLTCaloJetCollectionProducerFromVBF + fragment.HLTIterativeTrackingIteration4DisplacedJets + fragment.HLTDisplacedTightTrackRequirementDisplacedJetsFromVBFVVTightID + fragment.HLTEndSequence )


fragment.HLTSchedule = cms.Schedule( *(fragment.HLTriggerFirstPath, fragment.HLT_HT200_DisplacedDijet40_DisplacedTrack_v1, fragment.HLT_HT250_DisplacedDijet40_DisplacedTrack_v2, fragment.HLT_HT350_DisplacedDijet40_Inclusive_v1, fragment.HLT_HT400_DisplacedDijet40_Inclusive_v2, fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_v2, fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_v3, fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v2, fragment.HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v3, fragment.HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v2, fragment.HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v3, fragment.HLT_VBF_DisplacedJet40_Hadronic_v2, fragment.HLT_VBF_DisplacedJet40_Hadronic_v3, fragment.HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack_v2, fragment.HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack_v3, fragment.HLT_VBF_DisplacedJet40_TightID_Hadronic_v2, fragment.HLT_VBF_DisplacedJet40_TightID_Hadronic_v3, fragment.HLT_VBF_DisplacedJet40_VTightID_Hadronic_v2, fragment.HLT_VBF_DisplacedJet40_VTightID_Hadronic_v3, fragment.HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v2, fragment.HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v3, fragment.HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v2, fragment.HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v3, fragment.HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v2, fragment.HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v3 ))


# dummyfy hltGetConditions in cff's
if 'hltGetConditions' in fragment.__dict__ and 'HLTriggerFirstPath' in fragment.__dict__ :
    fragment.hltDummyConditions = cms.EDFilter( "HLTBool",
        result = cms.bool( True )
    )
    fragment.HLTriggerFirstPath.replace(fragment.hltGetConditions,fragment.hltDummyConditions)

# add specific customizations
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
fragment = customizeHLTforAll(fragment,"GRun")

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
fragment = customizeHLTforCMSSW(fragment,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(fragment)


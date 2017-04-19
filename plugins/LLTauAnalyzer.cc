// -*- C++ -*-
//
// Package:    HLTrigger/LLTauAnalyzer
// Class:      LLTauAnalyzer
// 
/**\class LLTauAnalyzer LLTauAnalyzer.cc HLTrigger/LLTauAnalyzer/plugins/LLTauAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Isabel Ojalvo
//         Created:  Fri, 31 Mar 2017 13:45:32 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/TauReco/interface/PFTau.h"
#include "DataFormats/TauReco/interface/PFTauDiscriminator.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "TTree.h"
#include "TLorentzVector.h"

#include <iostream>
#include <vector>
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.
using std::cout;
using std::endl;
using std::string;
using std::vector;

class LLTauAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit LLTauAnalyzer(const edm::ParameterSet&);
      ~LLTauAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;


	  edm::EDGetTokenT<edm::TriggerResults> trgresultsToken_;
      //edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> trigobjectToken_; //originally in LLTauAnalyzer
	  //edm::EDGetTokenT<std::vector<reco::GenParticle>> trigobjectToken_; //Used in RECO for getting the generated particle collection
	  edm::EDGetTokenT<std::vector<reco::GenParticle>> prunedGenParticleToken_;
	  edm::EDGetTokenT<std::vector<pat::Tau>> pfTauToken_;

	  //Define variables for TTree
	  TTree* tree;

	  //Variables for generated particle attributes
	  std::vector<Float_t> genPt_;
	  std::vector<Float_t> genEta_;
	  std::vector<Float_t> genPhi_;
	  std::vector<Int_t> genPId_;
	  std::vector<Float_t> genmVis_;

	  //Variables for HLT Trigger booleans (using integers because of pyROOT
	  Int_t boolTrigPass_;

	  //Variables for particle flow tau objects
	  std::vector<Float_t> tauPt_;
	  std::vector<Float_t> tauEta_;
	  std::vector<Float_t> tauPhi_;
	  std::vector<Float_t> taumVis_;
	  std::vector<Float_t> tauDMF_;
	  std::vector<Float_t> tauIso_;

	  //Variables for determining whether the particle passes certain cuts
	  std::vector<Int_t> boolTauPtCut_;
	  std::vector<Int_t> boolTauEtaCut_;
	  std::vector<Int_t> boolTauDMFCut_;
	  std::vector<Int_t> boolTauIsoCut_;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//HLTriggerReults
LLTauAnalyzer::LLTauAnalyzer(const edm::ParameterSet& cfg):
  trgresultsToken_(consumes<edm::TriggerResults>(cfg.getParameter<edm::InputTag>("HLTriggerResults"))),
  prunedGenParticleToken_(consumes<std::vector<reco::GenParticle>>(cfg.getParameter<edm::InputTag>("GenParticles"))),
  pfTauToken_(consumes<std::vector<pat::Tau>>(cfg.getParameter<edm::InputTag>("pfTauCollection")))
{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   
   //define ntuple

   tree = fs->make<TTree>("Ntuple","Ntuple");

   //Branches for generated particle attributes:
   tree->Branch("genPt",&genPt_);
   tree->Branch("genEta",&genEta_);
   tree->Branch("genPhi",&genPhi_);
   tree->Branch("genPId",&genPId_);
   tree->Branch("genmVis",&genmVis_);

   //Branches to store whether the event passes the HLT Trigger:
   tree->Branch("boolTrigPass",&boolTrigPass_,"boolTrigPass_/I");
   
   //Branches to store attributes of the pf tau objects:
   tree->Branch("tauPt",&tauPt_);
   tree->Branch("tauEta",&tauEta_);
   tree->Branch("tauPhi",&tauPhi_);
   tree->Branch("taumVis",&taumVis_);
   tree->Branch("tauDMF",&tauDMF_);
   tree->Branch("tauIso",&tauIso_);

   //Branches to store whether the taus pass the implemented cuts:
   tree->Branch("boolTauPtCut",&boolTauPtCut_);
   tree->Branch("boolTauEtaCut",&boolTauEtaCut_);
   tree->Branch("boolTauDMFCut",&boolTauDMFCut_);
   tree->Branch("boolTauIsoCut",&boolTauIsoCut_);
}


LLTauAnalyzer::~LLTauAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
LLTauAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   //Clear all variables
   genPt_.clear(); genEta_.clear(); genPhi_.clear(); genPId_.clear(); genmVis_.clear();

   boolTrigPass_ = 0;
   
   tauPt_.clear(); tauEta_.clear(); tauPhi_.clear(); taumVis_.clear(); tauDMF_.clear(); tauIso_.clear();

   boolTauPtCut_.clear(); boolTauEtaCut_.clear(); boolTauDMFCut_.clear(); boolTauIsoCut_.clear();

   //Accessing trigger bits (same as AOD):
   edm::Handle<edm::TriggerResults> trigResults;
   iEvent.getByToken(trgresultsToken_, trigResults);
   if( !trigResults.failedToGet() ) {
     int N_Triggers = trigResults->size();
     const edm::TriggerNames & trigName = iEvent.triggerNames(*trigResults);
     //std::cout<<"N_Triggers: "<<N_Triggers<<std::endl;
     for( int i_Trig = 0; i_Trig < N_Triggers; ++i_Trig ) {
       TString TrigPath =trigName.triggerName(i_Trig);
       if (trigResults.product()->accept(i_Trig)) {
	     //cout << "passed path: " << TrigPath<<endl;
		 //
		 //Determine whether you event passes your trigger requirement here

		   if (!TrigPath.CompareTo("MC_LooseIsoPFTau20_v5")) {
			boolTrigPass_ = 1;
	       }
       }
       //else
       //cout<<"failed path: " << TrigPath<<endl;	 
     }
   }

   else
     cout<<"Failed to get the trigger results!!"<<endl;

   //Accessing the trigger objects
   
   //First, save all the generated particle information

   //edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects; // Here in tthe original LLTauAnalyzer script - unused
   edm::Handle<std::vector<reco::GenParticle>> prunedGenObjects;
   iEvent.getByToken(prunedGenParticleToken_, prunedGenObjects);
   //const edm::TriggerNames &names = iEvent.triggerNames(*trigResults);

   for (reco::GenParticle particle : *prunedGenObjects) {
      genPt_.push_back(particle.pt());
	  genEta_.push_back(particle.eta());
	  genPhi_.push_back(particle.phi());
	  genPId_.push_back(particle.pdgId());
	  genmVis_.push_back(particle.mass());
   //for (pat::TriggerObjectStandAlone obj : *triggerObjects) {
   //  obj.unpackPathNames(names);
   //  for (unsigned h = 0; h < obj.filterLabels().size(); ++h){
   //    string myfillabl=obj.filterLabels()[h];
   //    cout << "trigger object name, pt, eta, phi: "
//	    << myfillabl<<", " << obj.pt()<<", "<<obj.eta()<<", "<<obj.phi() << endl;
     }

   //Add all the tau attributes to the tree
   edm::Handle<std::vector<pat::Tau>> slimmedTauObjects;
   iEvent.getByToken(pfTauToken_, slimmedTauObjects);
   for (pat::Tau tau : *slimmedTauObjects) {
     tauPt_.push_back(tau.pt());
	 tauEta_.push_back(tau.eta());
	 tauPhi_.push_back(tau.phi());
	 taumVis_.push_back(tau.mass());
	 tauDMF_.push_back(tau.tauID("decayModeFinding"));
	 tauIso_.push_back(tau.tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits"));

   //Implement cuts
   
   //Tau pT has to be greater than 20.0 GeV (Tau POG requirement)
     if(tau.pt() > 20.0) boolTauPtCut_.push_back(1);
	 else boolTauPtCut_.push_back(0);

   //Tau eta cut - must be in barrel/endcap region?
     if(std::abs(tau.eta()) < 2.4) boolTauEtaCut_.push_back(1);
	 else boolTauEtaCut_.push_back(0);

   //Tau Decay Mode Finding cut
     if(tau.tauID("decayModeFinding") > 0.5) boolTauDMFCut_.push_back(1);
	 else boolTauDMFCut_.push_back(0);

   //Tau Isolation cut
     if(tau.tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits") > 0.5) boolTauIsoCut_.push_back(1);
	 else boolTauIsoCut_.push_back(0);
	 //std::cout<<tau.pt()<<" "<<tau.phi()<<" "<<tau.eta()<<" "<<tau.mass()<<std::endl;
	 //std::cout<<tau.tauID("decayModeFinding")<<std::endl;
   }

   tree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
LLTauAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LLTauAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LLTauAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(LLTauAnalyzer);

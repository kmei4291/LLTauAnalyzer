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
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

#include <iostream>
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
      edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> trigobjectToken_;
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
  trigobjectToken_(consumes<pat::TriggerObjectStandAloneCollection>(cfg.getParameter<edm::InputTag>("TriggerObjectToken")))
{
   //now do what ever initialization is needed
   usesResource("TFileService");

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
   //Accessing trigger bits (same as AOD):
   edm::Handle<edm::TriggerResults> trigResults;
   iEvent.getByToken(trgresultsToken_, trigResults);
   if( !trigResults.failedToGet() ) {
     int N_Triggers = trigResults->size();
     const edm::TriggerNames & trigName = iEvent.triggerNames(*trigResults);
     std::cout<<"N_Triggers: "<<N_Triggers<<std::endl;
     for( int i_Trig = 0; i_Trig < N_Triggers; ++i_Trig ) {
       TString TrigPath =trigName.triggerName(i_Trig);
       if (trigResults.product()->accept(i_Trig)) {
	 cout << "passed path: " << TrigPath<<endl;
       }
       //else
       //cout<<"failed path: " << TrigPath<<endl;	 
     }
   }
   else
     cout<<"Failed to get the trigger results!!"<<endl;

   //Accessing the trigger objects
   /*
   edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
   iEvent.getByToken(trigobjectToken_, triggerObjects);
   const edm::TriggerNames &names = iEvent.triggerNames(*trigResults);
   for (pat::TriggerObjectStandAlone obj : *triggerObjects) {
     obj.unpackPathNames(names);
     for (unsigned h = 0; h < obj.filterLabels().size(); ++h){
       string myfillabl=obj.filterLabels()[h];
       cout << "trigger object name, pt, eta, phi: "
	    << myfillabl<<", " << obj.pt()<<", "<<obj.eta()<<", "<<obj.phi() << endl;
     }
   }
   */
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

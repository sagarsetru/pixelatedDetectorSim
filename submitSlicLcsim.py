#every single script has these four lines

from DIRAC.Core.Base import Script
Script.parseCommandLine()

#create ilcdirac instance
from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
dirac = DiracILC(True,"some_job_repository.rep")

#job definition
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
#job = UserJob()
from ILCDIRAC.Interfaces.API.NewInterface.Applications import SLIC
from ILCDIRAC.Interfaces.API.NewInterface.Applications import LCSIM


#jobParams = [('slicTest8_mu+_theta90.mac','diracTest8_mu+_theta90.slcio',50),('slicTest7_mu+_theta_5-175.mac','diracTest_mu+_theta_5-175.slcio',50),('slicTest3_e+.mac','diracTest3_e+.slcio',10),('slicTest2_pi+.mac','diractTest2_pi+.slcio',10)]
#jobParams = [('slicTest10_mu+_100gev_theta70_testNewGeom.mac','diracTest10_mu+_100gev_theta70_testNewGeom.slcio',10),('slicTest10_mu+_100gev_theta90_testNewGeom.mac','diracTest10_mu+_100gev_theta90_testNewGeom.slcio',10)]
jobParams = [('/users/detector/ssetru/SiDSim/detectors/detector_vtx_matbudghalf_nonsensitivelayer/slicmacros/slicTest8_mu+_100gev_theta60.mac','diracTest_100gev_theta60_vtx_matbudghalf_nonsensitivelayer.slcio',100),('/users/detector/ssetru/SiDSim/detectors/detector_vtx_matbudghalf_nonsensitivelayer/slicmacros/slicTest8_mu+_10gev_theta60.mac','diracTest_10gev_theta60_vtx_matbudghalf_nonsensitivelayer.slcio',100)]
#slicMacros = ['slicTest8_mu+_theta90.mac','slicTest7_mu+_theta_5-175.mac','slicTest3_e+.mac','slicTest2_pi+.mac']
#fileOutputs = ['diracTest2Loop1.slcio','diracTest2Loop2.slcio','diracTest2Loop3.slcio','diractTest2Loop4.slcio']
#slicNumEvents = [100,100,10,10]

for macro,output,nEvts in jobParams:
    job = UserJob()
    job.setName("ssetru_dirac_test1")
    job.setJobGroup("tests")
    job.setCPUTime(86400)
    #below ten mb, specified local path
    #larger input files are put into a grid storage unit, specified with grid path
    #job.setInputSandbox(["newDetector.zip"])
    job.setInputSandbox(["alias.properties"])
    #'/afs/cern.ch/user/s/ssetru/www/newDetector.zip'
    #job.setInputSandbox.append('/afs/cern.ch/user/s/ssetru/www/newDetector.zip') 
    #has log files, also may want to specify *.xml, generally short term data
    job.setOutputSandbox(["*.log","*.mac","*.xml"])
    #stored forever, in grid storage until you delete, path specified goes after your user directory in dirac
    job.setOutputData(output,"test_vtx_matbudghalf_nonsensitivelayer", "CERN-SRM")




    #for index in xrange(0,len(slicNumEvents)):

    slic = SLIC()
    slic.setVersion('v3r0p3')
    #can loop over stdhep files, takes precedence over what is in macro
    #slic.setInputFile("some_file.stdhep")
    #need not loop over macro
    #slic.setInputFile("newDetector.zip")
    slic.setSteeringFile(macro)
    slic.setNumberOfEvents(nEvts)
    #also overwrites macro
    #two options
    #1) specify lcdd filename (newDetector.lcdd) local or grid
    #2) specify detector name (like below). looks up detector in org.lcsim detector page and downloads the tarball
    slic.setDetectorModel('detector_vtx_matbudghalf_nonsensitivelayer.zip')
    #same rules as for InputFile EXCEPT NOT automatically added to output data (sandbox too small usually)
    slic.setOutputFile('slicOut.slcio')
    res = job.append(slic)



    lcsim = LCSIM()
    lcsim.getInputFromApp(slic)
    lcsim.setVersion('2.5')
    lcsim.setSteeringFile("/users/detector/ssetru/SiDSim/detectors/detector_vtx_matbudghalf_nonsensitivelayer/sid_dbd_prePandora_noOverlay2.xml")
    lcsim.setAliasProperties('alias.properties')
    #lcsim.setTrackingStrategy("/afs/cern.ch/user/s/ssetru/examples/autogen_ttbar_sidloi3.xml")
    lcsim.setTrackingStrategy("/users/detector/ssetru/SiDSim/detectors/detector_vtx_matbudghalf_nonsensitivelayer/strategies_vtx_matbudghalf_nonsensitivelayer.xml")
    #lcsim.setAliasProperties('alias.properties')
    lcsim.setOutputFile(output)
    #lcsim_prepandora.willRunSLICPandora()
    res = job.append(lcsim)
    #print index
    #print slicMacros[index]
    #print slicNumEvents[index]
    #print fileOutputs[index]

    print job.submit(dirac)
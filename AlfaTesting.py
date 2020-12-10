import sys
import flask

sys.path.insert(0,'VNF Subsystem/')
sys.path.insert(0,'Internal Router/')
sys.path.insert(0,'Access Subsystem/')
sys.path.insert(0,'Internal Manager/')
sys.path.insert(0,'VNF Information Base/')
sys.path.insert(0,'Monitoring Subsystem/')

sys.path.insert(0,'VNF Subsystem/Ve-Em-vnf/')
sys.path.insert(0,'Access Subsystem/Ve-Vnfm-em')
sys.path.insert(0,'Monitoring Subsystem/Monitoring Agents/')

import AsModels
import VibModels
import VsModels
import IrModels

import VibManager
import AsAuthAgent
import AsOpAgent
import VsAgent
import MsManager
import IrAgent
import ImAgent

import VnfDriverTemplate
import VnfmDriverTemplate
import MonitoringAgentTemplate

import CooDriver
import CooRunningAgent

##############################################################################################################################################################

'''
#-->> MANAGEMENT TESTING ROUTINE #1 - INTERNAL MANAGER ACTING OVER THE VIB MODULE (CREDENTIAL TABLE) <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#INSERTING AN TESTING CREDENTIAL
vibCredentialInstance = VibModels.VibCredentialInstance().fromData("USER02", "VNF01", "BatataFrita", None)
irManagement = IrModels.IrManagement().fromData("VIB", "post_vib_credentials", vibCredentialInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL CREDENTIAL TABLE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_credentials", None)
credentialTable = imAgent.requestOperation(irManagement)
print(credentialTable, "\n")

#GETTING THE RECENTLY INSERTED CREDENTIAL
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_c_credentialId", ("USER02", "VNF01"))
vibCredentialInstance = imAgent.requestOperation(irManagement)
print(vibCredentialInstance, "\n")

#VALID UPDATE IN THE NON-KEY VALUES OF THE CREDENTIAL
vibCredentialInstance.authData = "MandiocaFrita"
vibCredentialInstance.authResource = "BatataFrita"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_c_credentialId", vibCredentialInstance)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF UPDATE OCCURED SUCCESSFULY
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_c_credentialId", ("USER02", "VNF01"))
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE INSERTED SUBSCRIPTION
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_c_credentialId", ("USER02", "VNF01"))
print(imAgent.requestOperation(irManagement), "\n")
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #2 - INTERNAL MANAGER ACTING OVER THE VIB MODULE (SUBSCRIPTION TABLE) <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#INSERTING AN TESTING SUBSCRIPTION
vnfIndicatorNotificationsFilter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["VNF01"], []), [], ["CooRunningAgent"])
vibSubscriptionInstance = VibModels.VibSubscriptionInstance().fromData("1234567890", vnfIndicatorNotificationsFilter, "http://127.0.0.1:5000/response", {"self":"127.0.0.1"})
irManagement = IrModels.IrManagement().fromData("VIB", "post_vib_subscriptions", vibSubscriptionInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL SUBSCRIPTION TABLE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_subscriptions", None)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED SUBSCRIPTION
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_s_subscriptionId", "1234567890")
vibSubscriptionInstance = imAgent.requestOperation(irManagement)
print(vibSubscriptionInstance, "\n")

#INVALID UPDATE IN THE NON-KEY VALUES OF THE SUBSCRIPTION
#vibSubscriptionInstance.visFilter.vnfInstanceSubscriptionFilter.vnfInstanceIds.append("VNF02")
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_s_subscriptionId", vibSubscriptionInstance)
print(imAgent.requestOperation(irManagement), "\n")

#VALID UPDATE IN THE NON-KEY VALUES OF THE SUBSCRIPTION
#vibSubscriptionInstance.visFilter.filter.vnfInstanceIds.remove("VNF02")
vibSubscriptionInstance.visCallback = "http://127.0.0.1:5001/response"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_s_subscriptionId", vibSubscriptionInstance)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF UPDATE OCCURED SUCCESSFULY
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_s_subscriptionId", "1234567890")
vibSubscriptionInstance = imAgent.requestOperation(irManagement)
print(vibSubscriptionInstance, "\n")

#DELETING THE INSERTED SUBSCRIPTION
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_s_subscriptionId", "1234567890")
print(imAgent.requestOperation(irManagement))
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #3 - INTERNAL MANAGER ACTING OVER THE VIB MODULE (MANAGEMENT AGENT TABLE) <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#INSERTING AN TESTING SUBSCRIPTION
vibMaInstance = VibModels.VibMaInstance().fromData("DummyAgent", "DummyAgentSource", "Click-On-OSv")
irManagement = IrModels.IrManagement().fromData("VIB", "post_vib_m_agents", vibMaInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL SUBSCRIPTION TABLE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_m_agents", None)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED SUBSCRIPTION
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_ma_agentId", "DummyAgent")
vibMaInstance = imAgent.requestOperation(irManagement)
print(vibMaInstance, "\n")

#VALID UPDATE IN THE NON-KEY VALUES OF THE SUBSCRIPTION
vibMaInstance.maSource = "DummyAgentSourceMod"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_ma_agentId", vibMaInstance)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF UPDATE OCCURED SUCCESSFULY
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_ma_agentId", "DummyAgent")
vibSubscriptionInstance = imAgent.requestOperation(irManagement)
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE INSERTED SUBSCRIPTION
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_ma_agentId", "DummyAgent")
print(imAgent.requestOperation(irManagement))
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #4 - INTERNAL MANAGER ACTING OVER THE VIB MODULE (VNF INSTANCE TABLE) <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#INSERTING AN TESTING VNF INSTANCE
vibVnfInstance = VibModels.VibVnfInstance().fromData("VNF02", "127.0.0.1", "Click-On-OSv", [], None)
irManagement = IrModels.IrManagement().fromData("VIB", "post_vib_instances", vibVnfInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL VNF INSTANCE TABLE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_instances", None)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED VNF INSTANCE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_i_instanceId", "VNF02")
vibVnfInstance = imAgent.requestOperation(irManagement)
print(vibVnfInstance, "\n")

#INVALID UPDATE IN THE NON-KEY VALUES OF THE VNF INSTANCE
vibVnfInstance.vnfPlatform = "Inavlid"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_i_instanceId", vibVnfInstance)
print(imAgent.requestOperation(irManagement), "\n")

#VALID UPDATE IN THE NON-KEY VALUES OF THE INSTANCE
vibVnfInstance.vnfPlatform = "Click-On-OSv"
vibVnfInstance.vnfAuth = "Some auth data"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_i_instanceId", vibVnfInstance)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF UPDATE OCCURED SUCCESSFULY
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_i_instanceId", "VNF02")
print(imAgent.requestOperation(irManagement), "\n")

#INVALID DELETING OPERATION
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_i_instanceId", "VNF01")
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE INSERTED VNF INSTANCE
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_i_instanceId", "VNF02")
print(imAgent.requestOperation(irManagement), "\n")
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #5 - INTERNAL MANAGER ACTING OVER THE VIB MODULE (PLATFORM TABLE) <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#INSERTING AN TESTING PLATFORM INSTANCE
vibPlatformInstance = VibModels.VibPlatformInstance().fromData("Coven-On-OSv", "COO2Driver")
irManagement = IrModels.IrManagement().fromData("VIB", "post_vib_platforms", vibPlatformInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL PLATFORM INSTANCE TABLE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_platforms", None)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED PLATFORM INSTANCE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_p_platformId", "Coven-On-OSv")
vibPlatformInstance = imAgent.requestOperation(irManagement)
print(vibPlatformInstance, "\n")

#VALID UPDATE IN THE NON-KEY VALUES OF THE PLATFORM
vibPlatformInstance.platformDriver = "CovenOsvDriver"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_p_platformId", vibPlatformInstance)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF UPDATE OCCURED SUCCESSFULY
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_p_platformId", "Coven-On-OSv")
print(imAgent.requestOperation(irManagement), "\n")

#INVALID DELETING OPERATION
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_p_platformId", "Click-On-OSv")
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE INSERTED PLATFORM INSTANCE
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_p_platformId", "Coven-On-OSv")
print(imAgent.requestOperation(irManagement), "\n")
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #6 - INTERNAL MANAGER ACTING OVER THE VIB MODULE (VNFM TABLE) <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#INSERTING AN TESTING MANAGER INSTANCE
vibVnfmInstance = VibModels.VibVnfmInstance().fromData("Vines", "VinesDriver")
irManagement = IrModels.IrManagement().fromData("VIB", "post_vib_vnf_managers", vibVnfmInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL MANAGER INSTANCE TABLE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_vnf_managers", None)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED MANAGER INSTANCE
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_vnfm_managerId", "Vines")
vibVnfmInstance = imAgent.requestOperation(irManagement)
print(vibVnfmInstance, "\n")

#VALID UPDATE IN THE NON-KEY VALUES OF THE MANAGER
vibVnfmInstance.vnfmDriver = "VinesDriver2"
irManagement = IrModels.IrManagement().fromData("VIB", "patch_vib_vnfm_managerId", vibVnfmInstance)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF UPDATE OCCURED SUCCESSFULY
irManagement = IrModels.IrManagement().fromData("VIB", "get_vib_vnfm_managerId", "Vines")
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE INSERTED MANAGER INSTANCE
irManagement = IrModels.IrManagement().fromData("VIB", "delete_vib_vnfm_managerId", "Vines")
print(imAgent.requestOperation(irManagement), "\n")
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #7 - INTERNAL MANAGER ACTING OVER THE AS MODULE <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#GETTING AVAILABLE AUTHENTICATORS
irManagement = IrModels.IrManagement().fromData("AS", "get_as_auth", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF A PARTICULAR AUTHENTICATOR EXISTS
irManagement = IrModels.IrManagement().fromData("AS", "get_as_a_authId", "PlainText")
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING THE RUNNING AUTHENTICATOR
irManagement = IrModels.IrManagement().fromData("AS", "get_as_running_auth", None)
print(imAgent.requestOperation(irManagement), "\n")

#SETUP AUTHENTICATOR
irManagement = IrModels.IrManagement().fromData("AS", "post_as_running_auth", "PlainText")
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING THE RUNNING AUTHENTICATOR
irManagement = IrModels.IrManagement().fromData("AS", "get_as_running_auth", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF AN AUTHENTICATOR IS THE RUNNING AUTHENTICATOR
irManagement = IrModels.IrManagement().fromData("AS", "get_as_ra_authId", "PlainText")
print(imAgent.requestOperation(irManagement), "\n")


#GETTING AVAILABLE CREDENTIALS
irManagement = IrModels.IrManagement().fromData("AS", "get_as_credential", None)
print(imAgent.requestOperation(irManagement), "\n")

#INSERTING NEW CREDENTIAL
irManagement = IrModels.IrManagement().fromData("AS", "post_as_credential", VibModels.VibCredentialInstance().fromData("ADMIN", "VNF01", "LALA", None))
print(imAgent.requestOperation(irManagement), "\n")

#GETTING A PARTICULAR CREDENTIAL
irManagement = IrModels.IrManagement().fromData("AS", "get_as_c_credentialId", ("ADMIN", "VNF01"))
credential = imAgent.requestOperation(irManagement)
print(credential, "\n")

#VALID UPDATE IN THE RECENTLY INSERTED CREDENTIAL
credential.authData = "RERE"
irManagement = IrModels.IrManagement().fromData("AS", "patch_as_c_credentialId", credential)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING A PARTICULAR CREDENTIAL
irManagement = IrModels.IrManagement().fromData("AS", "get_as_c_credentialId", ("ADMIN", "VNF01"))
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE RECENTLY INSERTED CREDENTIAL
irManagement = IrModels.IrManagement().fromData("AS", "delete_as_c_credentialId", ("ADMIN", "VNF01"))
print(imAgent.requestOperation(irManagement), "\n")

#GETTING AVAILABLE CREDENTIALS
irManagement = IrModels.IrManagement().fromData("AS", "get_as_credential", None)
print(imAgent.requestOperation(irManagement), "\n")


#GETTING AVAILABLE VNFM DRIVERS
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vnfm_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#INSERTING A NEW VNFM DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "post_as_vnfm_driver", VibModels.VibVnfmInstance().fromData("DummyVnfmDriver2", "C:/Users/55559/Desktop/EMSPlatformTesting/DummyVnfmDriver2.py"))
print(imAgent.requestOperation(irManagement), "\n")

#GETTING A PARTICULAR VNFM DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vd_driverId", "DummyVnfmDriver2")
driver = imAgent.requestOperation(irManagement)
print(driver, "\n")

#UPDATE RECENTLY INSERTED DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "patch_as_vd_driverId", VibModels.VibVnfmInstance().fromData("DummyVnfmDriver2", "C:/Users/55559/Desktop/EMSPlatformTesting/DummyVnfmDriver2.py"))
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vnfm_running_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECKING IF A PARTICULAR DRIVER IS THE RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vrd_driverId", "DummyVnfmDriver")
print(imAgent.requestOperation(irManagement), "\n")

#TRYING TO DELETE THE RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "delete_as_vd_driverId", "DummyVnfmDriver")
print(imAgent.requestOperation(irManagement), "\n")

#POSTING THE NEW DRIVER AS RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "post_as_vnfm_running_driver", driver)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vnfm_running_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#POSTING THE NEW DRIVER AS RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "post_as_vnfm_running_driver", VibModels.VibVnfmInstance().fromData("DummyVnfmDriver", "DummyVnfmDriver"))
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RUNNING DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vnfm_running_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#DELETE THE RECENTLY INSERTED DRIVER
irManagement = IrModels.IrManagement().fromData("AS", "delete_as_vd_driverId", "DummyVnfmDriver2")
print(imAgent.requestOperation(irManagement), "\n")

#GETTING AVAILABLE VNFM DRIVERS
irManagement = IrModels.IrManagement().fromData("AS", "get_as_vnfm_driver", None)
print(imAgent.requestOperation(irManagement), "\n")
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #8 - INTERNAL MANAGER ACTING OVER THE VS MODULE <<--#
vibManager = VibManager.VibManager()
msManager = MsManager.MsManager()
asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
vsAgent = VsAgent.VsAgent()

imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

#GETTING THE VNF INSTANCES
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_vnf_instance", None)
print(imAgent.requestOperation(irManagement), "\n")

#INSERTING NEW VNF INSTANCE
irManagement = IrModels.IrManagement().fromData("VS", "post_vs_vnf_instance", VibModels.VibVnfInstance().fromData("VNF02", "127.0.0.1:5000", "Click-On-OSv", [], False))
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED VNF INSTANCE
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_vnfi_instanceId", "VNF02")
vibVnfInstance = imAgent.requestOperation(irManagement)
print(vibVnfInstance, "\n")

#TRYING TO UPDATE AN MONITORED INSTANCE - ERROR EXPECTED
vibVnfInstance.vnfId = "VNF01"
irManagement = IrModels.IrManagement().fromData("VS", "patch_vs_vnfi_instanceId", vibVnfInstance)
print(imAgent.requestOperation(irManagement), "\n")

#UPDATING THE RECENTLY INSERTED VNF
vibVnfInstance.vnfId = "VNF02"
irManagement = IrModels.IrManagement().fromData("VS", "patch_vs_vnfi_instanceId", vibVnfInstance)
print(imAgent.requestOperation(irManagement), "\n")

#TRYING TO DELETE AN MONITORED INSTANCE - ERROR EXPECTED
irManagement = IrModels.IrManagement().fromData("VS", "delete_vs_vnfi_instanceId", "VNF01")
print(imAgent.requestOperation(irManagement), "\n")

#DELETING THE RECENTLY INSERTED VNF INSTANCE
irManagement = IrModels.IrManagement().fromData("VS", "delete_vs_vnfi_instanceId", "VNF02")
print(imAgent.requestOperation(irManagement), "\n")

#CHECK THE RUNNING VS DRIVER - NONE IS EXPECTED
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_running_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#INSERT A RUNNING VS DRIVER - CLICK-ON-OSV
irManagement = IrModels.IrManagement().fromData("VS", "post_vs_running_driver", "Click-On-OSv")
print(imAgent.requestOperation(irManagement), "\n")

#CHECK THE RUNING VS DRIVER - CLICK-ON-OSV IS EXPECTED
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_running_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECK ALL THE OPERATION OF THE RUNING VS DRIVER
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_rd_operations", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECK MONITORING OPERATIONS OF THE RUNING VS DRIVER
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_rdo_monitoring", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECK MODIFICATION OPERATIONS OF THE RUNING VS DRIVER
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_rdo_modification", None)
print(imAgent.requestOperation(irManagement), "\n")

#CHECK OTHER OPERATIONS OF THE RUNING VS DRIVER
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_rdo_other", None)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING FULL PLATFORM INSTANCE TABLE
irManagement = IrModels.IrManagement().fromData("VS", "get_vs_driver", None)
print(imAgent.requestOperation(irManagement), "\n")

#INSERT A NEW PLATFORM DRIVER INTO THE VS
vibPlatformInstance = VibModels.VibPlatformInstance().fromData("DummyPlatform", "C:\\Users\\55559\\Desktop\\EMSPlatformTesting\\DummyPlatformDriver.py")
irManagement = IrModels.IrManagement().fromData("VS", "post_vs_driver", vibPlatformInstance)
print(imAgent.requestOperation(irManagement), "\n")

#GETTING THE RECENTLY INSERTED MANAGER INSTANCE
irManagement = IrModels.IrManagement().fromData("VS", "get_vsd_driverId", "DummyPlatform")
print(imAgent.requestOperation(irManagement), "\n")

#PATCH THE RECENTLY INSERTED PLATFORM DRIVER
vibPlatformInstance = VibModels.VibPlatformInstance().fromData("DummyPlatform", "C:\\Users\\55559\\Desktop\\EMSPlatformTesting\\DummyPlatformDriver.py")
irManagement = IrModels.IrManagement().fromData("VS", "patch_vsd_driverId", vibPlatformInstance)
print(imAgent.requestOperation(irManagement), "\n")

#DELETE THE RECENTLY INSERTED PLATFORM DRIVER
irManagement = IrModels.IrManagement().fromData("VS", "delete_vsd_driverId", "DummyPlatform")
print(imAgent.requestOperation(irManagement), "\n")
'''

'''
#-->> MANAGEMENT TESTING ROUTINE #9 - INTERNAL MANAGER ACTING OVER THE MS MODULE <<--#
import time
def main():
	vibManager = VibManager.VibManager()
	msManager = MsManager.MsManager()
	asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
	asOpAgent = AsOpAgent.OperationAgent().setupAgent(vibManager, "DummyVnfmDriver", None, asAuthAgent)
	vsAgent = VsAgent.VsAgent()

	imAgent = ImAgent.ImAgent().setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)

	#INSERTING AN TESTING MONITORING AGENT INSTANCE
	vibMaInstance = VibModels.VibMaInstance().fromData("DummyMonitoring", "C:/Users/55559/Desktop/EMSPlatformTesting/DummyMonitoringAgent.py", "Click-On-OSv")
	irManagement = IrModels.IrManagement().fromData("MS", "post_ms_agent", vibMaInstance)
	print(imAgent.requestOperation(irManagement), "\n")

	#GETTING FULL MANAGER INSTANCE TABLE
	irManagement = IrModels.IrManagement().fromData("MS", "get_ms_agent", None)
	print(imAgent.requestOperation(irManagement), "\n")

	#GETTING THE RECENTLY INSERTED MANAGER INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "get_msa_agentId", "DummyMonitoring")
	print(imAgent.requestOperation(irManagement), "\n")

	#VALID UPDATE IN THE NON-KEY VALUES OF THE MANAGER
	vibMaInstance.maSource = "C:/Users/55559/Desktop/EMSPlatformTesting/DummyMonitoringAgent.py"
	irManagement = IrModels.IrManagement().fromData("MS", "patch_msa_agentId", vibMaInstance)
	print(imAgent.requestOperation(irManagement), "\n")

	#DELETING THE INSERTED MANAGER INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "delete_msa_agentId", "DummyMonitoring")
	print(imAgent.requestOperation(irManagement), "\n")

	#GETTING FULL SUBSCRIPTION INSTANCE TABLE
	irManagement = IrModels.IrManagement().fromData("MS", "get_ms_subscription", None)
	print(imAgent.requestOperation(irManagement), "\n")

	#INVALID INSERTION OF SUBSCRIPTION (VNF INSTANCE)
	vnfIndicatorNotificationsFilter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["NonExist"], []), [], ["CooRunningAgent"])
	vnfIndicatorSubscriptionRequest = AsModels.VnfIndicatorSubscriptionRequest().fromData(vnfIndicatorNotificationsFilter, "http://127.0.0.1:5000/response", None)
	irManagement = IrModels.IrManagement().fromData("MS", "post_ms_subscription", vnfIndicatorSubscriptionRequest)
	print(imAgent.requestOperation(irManagement), "\n")

	#INVALID INSERTION OF SUBSCRIPTION (MONITORING AGENT INSTANCE)
	vnfIndicatorNotificationsFilter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["VNF01"], []), [], ["NonExist"])
	vnfIndicatorSubscriptionRequest = AsModels.VnfIndicatorSubscriptionRequest().fromData(vnfIndicatorNotificationsFilter, "http://127.0.0.1:5000/response", None)
	irManagement = IrModels.IrManagement().fromData("MS", "post_ms_subscription", vnfIndicatorSubscriptionRequest)
	print(imAgent.requestOperation(irManagement), "\n")

	#VALID INSERTION OF SUBSCRIPTION (MONITORING AGENT INSTANCE)
	vnfIndicatorNotificationsFilter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["VNF01"], []), [], ["CooRunningAgent"])
	vnfIndicatorSubscriptionRequest = AsModels.VnfIndicatorSubscriptionRequest().fromData(vnfIndicatorNotificationsFilter, "http://127.0.0.1:5000/response", None)
	irManagement = IrModels.IrManagement().fromData("MS", "post_ms_subscription", vnfIndicatorSubscriptionRequest)
	subscription = imAgent.requestOperation(irManagement)
	print(subscription, "\n")

	#GETTING THE RECENTLY INSERTED SUBSCRIPTION INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "get_mss_subscriptionId", subscription.id)
	vibSubscription = imAgent.requestOperation(irManagement)
	print(vibSubscription, "\n")

	#INVALID UPDATE OF SUBSCRIPTION (VNF INSTANCE)
	subscription.filter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["NonExist"], []), [], ["CooRunningAgent"])
	irManagement = IrModels.IrManagement().fromData("MS", "patch_mss_subscriptionId", subscription)
	print(imAgent.requestOperation(irManagement), "\n")

	#INVALID UPDATE OF SUBSCRIPTION (MONITORING AGENT INSTANCE)
	subscription.filter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["VNF01"], []), [], ["NonExist"])
	irManagement = IrModels.IrManagement().fromData("MS", "patch_mss_subscriptionId", subscription)
	print(imAgent.requestOperation(irManagement), "\n")

	#VALID UPDATE OF SUBSCRIPTION
	subscription.filter = AsModels.VnfIndicatorNotificationsFilter().fromData(AsModels.VnfInstanceSubscriptionFilter().fromData([], [], ["VNF01"], []), [], ["CooRunningAgent"])
	irManagement = IrModels.IrManagement().fromData("MS", "patch_mss_subscriptionId", subscription)
	print(imAgent.requestOperation(irManagement), "\n")

	#DELETE THE INSERTED SUBSCRIPTION
	irManagement = IrModels.IrManagement().fromData("MS", "delete_mss_subscriptionId", subscription.id)
	print(imAgent.requestOperation(irManagement), "\n")

	#SHOW ALL THE RUNNING SUBSCRIPTIONS
	irManagement = IrModels.IrManagement().fromData("MS", "get_ms_running_subscription", None)
	print(imAgent.requestOperation(irManagement), "\n")

	#REQUEST AN SUBSCRIPRION TO RUN
	irManagement = IrModels.IrManagement().fromData("MS", "post_ms_running_subscription", "SUBS01")
	print(imAgent.requestOperation(irManagement), "\n")

	#CHECK IF THE REQUESTED VNF IS NOW A RUNNING INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "get_msrs_subscriptionId", "SUBS01")
	print(imAgent.requestOperation(irManagement), "\n")

	#ACTIVATE THE MONITORING PROCESS OF A RUNNING INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "patch_msrs_subscriptionId", ("SUBS01", [{}]))
	print(imAgent.requestOperation(irManagement), "\n")

	#WAIT A MOMENT
	time.sleep(6)

	#DEACTIVATE THE MONITORING PROCESS OF A RUNNING INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "patch_msrs_subscriptionId", ("SUBS01", ))
	print(imAgent.requestOperation(irManagement), "\n")

	#DELETE THE RUNNING INSTANCE OF MONITORING SUBSYSTEM
	irManagement = IrModels.IrManagement().fromData("MS", "delete_msrs_subscriptionId", "SUBS01")
	print(imAgent.requestOperation(irManagement), "\n")

	#CHECK IF THE REQUESTED VNF IS NOW A RUNNING INSTANCE
	irManagement = IrModels.IrManagement().fromData("MS", "get_msrs_subscriptionId", "SUBS01")
	print(imAgent.requestOperation(irManagement), "\n")

if __name__ == '__main__':
    main()
'''
vibManager = VibManager.VibManager()

asAuthAgent = AsAuthAgent.AuthenticationAgent(vibManager)
asOpAgent = AsOpAgent.OperationAgent()
msManager = MsManager.MsManager()
vsAgent = VsAgent.VsAgent()
imAgent = ImAgent.ImAgent()
irAgent = IrAgent.IrAgent()

aiAgent = flask.Flask(__name__)

asOpAgent.setupAgent(vibManager, "DummyVnfmDriver", aiAgent, asAuthAgent, irAgent)
imAgent.setupAgent(vibManager, msManager, asAuthAgent, asOpAgent, vsAgent)
irAgent.setupAgent(imAgent, vsAgent)

aiAgent.run(port=9000)
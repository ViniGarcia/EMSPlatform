'''
GENERAL INFORMATION: This file contains several classes that defines the
					 data model to communicate with the VIB through the
					 VIB Manager.
NOTE:				 The classes contain two "to" standard methods ("toSql"/
					 "toDictionary") and two "from" standard methods. 
					 "toSql" returns the query to insert the class into the
					 VIB, and "fromSql" rebuild the class from data returned
					 by the VIB.  
					 "toDictionary" returns the dictionary containing the 
					 dictionary representation of all the classes objects,
					 while "fromDictionary" recreates the class from the 
					 dictionary representation.
'''

#######################################################################################################
#######################################################################################################
import AsModels

import json

'''
CLASS: VibSummaryModels
AUTHOR: Vinicius Fulber-Garcia
CREATION: 30 Oct. 2020
L. UPDATE: 10 Nov. 2020 (Fulber-Garcia; VibVnfIndicatorSubscription creation)
DESCRIPTION: This class represents the table creation rou-
			 tines of all the tables of the VIB. Once a
			 table is updated in its respective class, the
			 creation routine must be updated here too.
'''
class VibSummaryModels:
	VibPlatformInstance = """ CREATE TABLE IF NOT EXISTS PlatformInstance (
                     	 platformId text PRIMARY KEY,
                     	 basicOperations text NOT NULL,
                     	 monitoringOperations text NOT NULL,
                     	 configuringOperations text NOT NULL
                    	); """

	VibVnfInstance = """ CREATE TABLE IF NOT EXISTS VnfInstance (
                     vnfId text PRIMARY KEY,
                     vnfAddress text NOT NULL,
                     vnfPlatform text NOT NULL,
                     vnfExtAgents text,
                     vnfAuth boolean,
                     FOREIGN KEY (vnfPlatform)
       					REFERENCES PlatformInstance (platformId)
                    ); """

	VibAuthInstance = """ CREATE TABLE IF NOT EXISTS AuthInstance (
                     userId text PRIMARY KEY,
                     vnfId text NOT NULL,
                     authData text NOT NULL,
                     authResource text,
                     FOREIGN KEY (vnfId)
       					REFERENCES VnfInstance (vnfId)
                    ); """

	VibVnfIndicatorSubscription = """ CREATE TABLE IF NOT EXISTS VnfIndicatorSubscription (
                     visId text PRIMARY KEY,
                     visFilter text,
                     visCallback text NOT NULL,
                     visLinks text NOT NULL
                    ); """

'''
CLASS: VibPlatformInstance
AUTHOR: Vinicius Fulber-Garcia
CREATION: 05 Nov. 2020
L. UPDATE: 05 Nov. 2020 (Fulber-Garcia; Class creation)
DESCRIPTION: This class represents the PlatformInstance table of
			 the VIB. Note that modifications on this class, par-
			 ticulary in the attributes, must be updated in the
			 VibSummaryModels too.
'''
class VibPlatformInstance:
	platformId = None
	basicOperations = None
	monitoringOperations = None
	configuringOperations = None

	def __init__(self):
		return

	def fromData(self, platformId, basicOperations, monitoringOperations, configuringOperations):
		self.platformId = platformId
		self.basicOperations = basicOperations
		self.monitoringOperations = monitoringOperations
		self.configuringOperations = configuringOperations
		return self

	def fromSql(self, sqlData):
		self.platformId = sqlData[0]
		self.basicOperations = json.loads(sqlData[1])
		self.monitoringOperations = json.loads(sqlData[2])
		self.configuringOperations = json.loads(sqlData[3])
		return self

	def fromDictionary(self, dictData):
		self.platformId = dictData["platformId"]
		self.basicOperations = dictData["basicOperations"]
		self.monitoringOperations = dictData["monitoringOperations"]
		self.configuringOperations = dictData["configuringOperations"]
		return self

	def toSql(self):
		return ('''INSERT INTO PlatformInstance(platformId,basicOperations,monitoringOperations,configuringOperations)
              	   VALUES(?,?,?,?)''', (self.platformId, json.dumps(self.basicOperations), json.dumps(self.monitoringOperations), json.dumps(self.configuringOperations)))

	def toDictionary(self):
		return {"platformId":self.platformId, "basicOperations":self.basicOperations, "monitoringOperations":self.monitoringOperations, "configuringOperations":self.configuringOperations}

'''
CLASS: VibVnfInstance
AUTHOR: Vinicius Fulber-Garcia
CREATION: 30 Oct. 2020
L. UPDATE: 05 Nov. 2020 (Fulber-Garcia; New vnfAddress attribute; Update of vnfExtAgents; fromData method)
DESCRIPTION: This class represents the VnfInstance table of the
			 VIB. Note that modifications on this class, parti-
			 culary in the attributes, must be updated in the
			 VibSummaryModels too.
'''
class VibVnfInstance:
	vnfId = None
	vnfAddress = None
	vnfPlatform = None #TODO: setar chave estrangeira
	vnfExtAgents = None			
	vnfAuth = None
	
	def __init__(self):
		return

	def fromData(self, vnfId, vnfAddress, vnfPlatform, vnfExtAgents, vnfAuth):
		self.vnfId = vnfId
		self.vnfAddress = vnfAddress
		self.vnfPlatform = vnfPlatform
		self.vnfExtAgents = vnfExtAgents
		self.vnfAuth = vnfAuth
		return self

	def fromSql(self, sqlData):
		self.vnfId = sqlData[0]
		self.vnfAddress = sqlData[1]
		self.vnfPlatform = sqlData[2]
		self.vnfExtAgents = json.loads(sqlData[3])
		self.vnfAuth = bool(sqlData[3])
		return self

	def fromDictionary(self, dictData):
		self.vnfId = dictData["vnfId"]
		self.vnfAddress = dictData["vnfAddress"]
		self.vnfPlatform = dictData["vnfPlatform"]
		self.vnfExtAgents = dictData["vnfExtAgents"]
		self.vnfAuth = dictData["vnfAuth"]
		return self

	def toSql(self):
		return ('''INSERT INTO VnfInstance(vnfId,vnfAddress,vnfPlatform,vnfExtAgents,vnfAuth)
              	   VALUES(?,?,?,?,?)''', (self.vnfId, self.vnfAddress, self.vnfPlatform, json.dumps(self.vnfExtAgents), self.vnfAuth))

	def toDictionary(self):
		return {"vnfId":self.vnfId, "vnfAddress":self.vnfAddress, "vnfPlatform":self.vnfPlatform, "vnfExtAgents":self.vnfExtAgents, "vnfAuth":self.vnfAuth}

'''
CLASS: VibAuthInstance
AUTHOR: Vinicius Fulber-Garcia
CREATION: 04 Nov. 2020
L. UPDATE: 05 Nov. 2020 (Fulber-Garcia; fromData method)
DESCRIPTION: This class represents the AuthInstance table of the
			 VIB. Note that modifications on this class, parti-
			 culary in the attributes, must be updated in the
			 VibSummaryModels too.
'''
class VibAuthInstance:
	userId = None
	vnfId = None
	authData = None
	authResource = None

	def __init__(self):
		return

	def fromData(self, userId, vnfId, authData, authResource):
		self.userId = userId
		self.vnfId = vnfId
		self.authData = authData
		self.authResource = authResource
		return self

	def fromSql(self, sqlData):
		self.userId = sqlData[0]
		self.vnfId = sqlData[1]
		self.authData = sqlData[2]
		self.authResource = sqlData[3]
		return self

	def fromDictionary(self, dictData):
		self.userId = dictData["userId"]
		self.vnfId = dictData["vnfId"]
		self.authData = dictData["authData"]
		if "authResource" in self.dictData:
			self.authResource = dictData["authResource"]
		return self

	def toSql(self):
		return ('''INSERT INTO AuthInstance(userId,vnfId,authData,authResource)
              	   VALUES(?,?,?,?)''', (self.userId, self.vnfId, self.authData, self.authResource))

	def toDictionary(self):
		return {"userId":self.userId, "vnfId":self.vnfId, "authData":self.authData, "authResource":self.authResource}

'''
CLASS: VibVnfIndicatorSubscription
AUTHOR: Vinicius Fulber-Garcia
CREATION: 06 Nov. 2020
L. UPDATE: 10 Nov. 2020 (Fulber-Garcia; Methods creation)
DESCRIPTION: This class represents the VnfIndicatorSubscription 
			 table of the VIB. Note that modifications on this
			 class, particulary in the attributes, must be upda-
			 ted in the VibSummaryModels too.
'''
class VibVnfIndicatorSubscription:
	visId = None
	visFilter = None
	visCallback = None
	visLinks = None

	def __init__(self):
		return

	def fromData(self, visId, visFilter, visCallback, visLinks):
		self.visId = visId
		self.visFilter = visFilter
		self.visCallback = visCallback
		self.visLinks = visLinks
		return self

	def fromSql(self, sqlData):
		self.visId = sqlData[0]
		if sqlData[1] != None:
			self.visFilter = AsModels.VnfIndicatorNotificationsFilter().fromDictionary(json.loads(sqlData[1]))
		else:
			self.visFilter = sqlData[1]
		self.visCallback = sqlData[2]
		self.visLinks = json.loads(sqlData[3])
		return self

	def fromDictionary(self, dictData):
		self.visId = dictData["visId"]
		if dictData["visFilter"] != None:
			self.visFilter = AsModels.VnfIndicatorNotificationsFilter().fromDictionary(dictData["visFilter"])
		else:
			self.visFilter = dictData["visFilter"]
		self.visCallback = dictData["visCallback"]
		self.visLinks = dictData["visLinks"]
		return self

	def toSql(self):
		if self.visFilter != None:
			return ('''INSERT INTO VnfIndicatorSubscription(visId,visFilter,visCallback,visLinks)
              	   	VALUES(?,?,?,?)''', (self.visId, json.dumps(self.visFilter.toDictionary()), self.visCallback, json.dumps(self.visLinks)))
		else:
			return ('''INSERT INTO VnfIndicatorSubscription(visId,visFilter,visCallback,visLinks)
              	   	VALUES(?,?,?,?)''', (self.visId, self.visFilter, self.visCallback, json.dumps(self.visLinks)))

	def toDictionary(self):
		if self.visFilter != None:
			return {"visId":self.visId, "visFilter":self.visFilter.toDictionary(), "visCallback":self.visCallback, "visLinks":self.visLinks}
		else:
			return {"visId":self.visId, "visFilter":self.visFilter, "visCallback":self.visCallback, "visLinks":self.visLinks}
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.engine.url import URL
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import logging
import os
import settings

app = Flask(__name__)
app.config.from_object('settings.Config')
db = SQLAlchemy(app)

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

class NIST_800_53_r4_All_Requirements(db.Model):
	__tablename__ = '*800_53_r4_All_Requirements'

	requirementid = Column('requirementid', Integer, nullable=False, primary_key=True)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	controlfamily = Column('controlfamily', String, nullable=False)
	controltitle = Column('controltitle', String, nullable=False)
	controltext = Column('controltext', String, nullable=False)
	supplementalguidance = Column('supplementalguidance', String, nullable=False)
	references = Column('references', String, nullable=False)


class NIST_800_53_r4_Moderate_FedRAMP_Procedures(db.Model):
	__tablename__ = '*800_53_r4_Moderate_FedRAMP_Procedures'

	procedureid = Column('procedureid', Integer, nullable=False, primary_key=True)
	requirementid = Column('requirementid', Integer, nullable=False)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	sourceprocedure = Column('sourceprocedure', String, nullable=False)
	vermethod = Column('vermethod', String, nullable=False)
	overview = Column('overview', String, nullable=False)
	stepnum = Column('stepnum', Integer, nullable=False)
	roleid = Column('roleid', Integer, nullable=False)
	evaluationsteps = Column('evaluationsteps', String, nullable=False)
	expectedresults = Column('expectedresults', String, nullable=False)
	depson = Column('depson', Integer, nullable=False)
	depentresult = Column('depentresult', Integer, nullable=False)


class NIST_800_53_r4_Moderate_FedRAMP_Requirements(db.Model):
	__tablename__ = '*800_53_r4_Moderate_FedRAMP_Requirements'

	requirementid = Column('requirementid', Integer, nullable=False, primary_key=True)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	subcontrol = Column('subcontrol', String, nullable=False)
	controlfamily = Column('controlfamily', String, nullable=False)
	controltitle = Column('controltitle', String, nullable=False)
	controltext = Column('controltext', String, nullable=False)
	supplementalguidance = Column('supplementalguidance', String, nullable=False)


class NIST_800_53_r4_Moderate_FedRAMP_Requirements1(db.Model):
	__tablename__ = '*800_53_r4_Moderate_FedRAMP_Requirements1'

	requirementid = Column('requirementid', Integer, nullable=False, primary_key=True)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	subcontrol = Column('subcontrol', String, nullable=False)
	controlfamily = Column('controlfamily', String, nullable=False)
	controltitle = Column('controltitle', String, nullable=False)
	controltext = Column('controltext', String, nullable=False)
	supplementalguidance = Column('supplementalguidance', String, nullable=False)


class NIST_800_53_r4_Moderate_Procedures(db.Model):
	__tablename__ = '*800_53_r4_Moderate_Procedures'

	procedureid = Column('procedureid', Integer, nullable=False, primary_key=True)
	requirementid = Column('requirementid', Integer, nullable=False)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	sourceprocedure = Column('sourceprocedure', String, nullable=False)
	vermethod = Column('vermethod', String, nullable=False)
	overview = Column('overview', String, nullable=False)
	stepnum = Column('stepnum', Integer, nullable=False)
	roleid = Column('roleid', Integer, nullable=False)
	evaluationsteps = Column('evaluationsteps', String, nullable=False)
	expectedresults = Column('expectedresults', String, nullable=False)
	depson = Column('depson', Integer, nullable=False)
	depentresult = Column('depentresult', Integer, nullable=False)


class NIST_800_53_r4_Moderate_Requirements(db.Model):
	__tablename__ = '*800_53_r4_Moderate_Requirements'

	requirementid = Column('requirementid', Integer, nullable=False, primary_key=True)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	controlfamily = Column('controlfamily', String, nullable=False)
	controltitle = Column('controltitle', String, nullable=False)
	controltext = Column('controltext', String, nullable=False)
	supplementalguidance = Column('supplementalguidance', String, nullable=False)

class ArchiveActivities(db.Model):
	__tablename__ = 'ArchiveActivities'

	id = Column('id', Integer, nullable=False, primary_key=True)
	documentid = Column('documentid', Integer, nullable=False)
	projectid = Column('projectid', Integer, nullable=False)
	event = Column('event', String, nullable=False)
	version = Column('version', Float, nullable=False)
	versiondatetime = Column('versiondatetime', DateTime, nullable=False)
	uploaderid = Column('uploaderid', String, nullable=False)


class Artifacts(db.Model):
	__tablename__ = 'Artifacts'

	id = Column('id', Integer, nullable=False, primary_key=True)
	assessmentid = Column('assessmentid', Integer, nullable=False)
	documentid = Column('documentid', Integer, nullable=False)
	procedureid = Column('procedureid', Integer, nullable=False)


class AssessmentProgress(db.Model):
	__tablename__ = 'AssessmentProgress'

	id = Column('id', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	roleid = Column('roleid', Integer, nullable=False)
	assessor = Column('assessor', String, nullable=False)
	interviewcontactset = Column('interviewcontactset', Boolean, nullable=False)
	interviewcontactid = Column('interviewcontactid', Integer, nullable=False)
	status = Column('status', String, nullable=False)
	masterarchive = Column('masterarchive', Boolean, nullable=False)
	createtime = Column('createtime', DateTime, nullable=False)


class AssessmentRoles(db.Model):
    __tablename__ = 'AssessmentRoles'

    id = Column('id', Integer, nullable=False, primary_key=True)
    role = Column('role', String, nullable=False)
    description = Column('description', String, nullable=False)
    type = Column('type', String, nullable=False)

    def __init__(self, role, description, type):
        self.role = role
        self.description = description
        self.type = type

    def __repr__(self):
        return '<Role %r>' % self.role

'''
class CrossReferences(db.Model):
	__tablename__ = 'CrossReferences'

	crossrefid = Column('crossrefid', Integer, nullable=False, primary_key=True)
	source1table = Column('table', String, nullable=False)
	source2table = Column('table', String, nullable=False)
	source1id = Column('id', Integer, nullable=False)
	source2id = Column('id', Integer, nullable=False)
'''

class DocumentActivity(db.Model):
	__tablename__ = 'DocumentActivity'

	id = Column('id', Integer, nullable=False, primary_key=True)
	documentid = Column('documentid', Integer, nullable=False)
	projectid = Column('projectid', Integer, nullable=False)
	event = Column('event', String, nullable=False)
	version = Column('version', Float, nullable=False)
	versiondatetime = Column('versiondatetime', DateTime, nullable=False)
	uploaderid = Column('uploaderid', String, nullable=False)


class Documents(db.Model):
	__tablename__ = 'Documents'

	id = Column('id', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	frilyname = Column('frilyname', String, nullable=False)
	filename = Column('filename', String, nullable=False)
	description = Column('description', String, nullable=False)
	location = Column('location', String, nullable=False)
	hashvalue = Column('hashvalue', String, nullable=False)
	initialuploaderid = Column('initialuploaderid', String, nullable=False)
	lastmodifiedid = Column('lastmodifiedid', String, nullable=False)
	checkedout = Column('checkedout', Boolean, nullable=False)
	checkedoutuserid = Column('checkedoutuserid', String, nullable=False)


class FindingActionResults(db.Model):
	__tablename__ = 'FindingActionResults'

	id = Column('id', Integer, nullable=False, primary_key=True)
	actionresult = Column('actionresult', String, nullable=False)
	description = Column('description', String, nullable=False)


class FindingActions(db.Model):
	__tablename__ = 'FindingActions'

	id = Column('id', Integer, nullable=False, primary_key=True)
	findingid = Column('findingid', Integer, nullable=False)
	actiondate = Column('actiondate', DateTime, nullable=False)
	actioner = Column('actioner', String, nullable=False)
	actiontaken = Column('actiontaken', String, nullable=False)
	actiondescription = Column('actiondescription', String, nullable=False)
	actionresult = Column('actionresult', Integer, nullable=False)
	entrydatetime = Column('entrydatetime', DateTime, nullable=False)


class FindingRelationship(db.Model):
	__tablename__ = 'FindingRelationship'

	id = Column('id', Integer, nullable=False, primary_key=True)
	findingid = Column('findingid', Integer, nullable=False)
	procrefid = Column('procrefid', Integer, nullable=False)
	projectid = Column('projectid', Integer, nullable=False)
	type = Column('type', String, nullable=False)


class Findings(db.Model):
	__tablename__ = 'Findings'

	findingid = Column('findingid', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	findingtitle = Column('findingtitle', String, nullable=False)
	riskrating = Column('riskrating', String, nullable=False)
	findingdiscussion = Column('findingdiscussion', String, nullable=False)
	findingrecommation = Column('findingrecommation', String, nullable=False)
	masterstatus = Column('masterstatus', Integer, nullable=False)


class InterviewContacts(db.Model):
	__tablename__ = 'InterviewContacts'

	id = Column('id', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	roleid = Column('roleid', Integer, nullable=False)
	firstname = Column('firstname', String, nullable=False)
	lastname = Column('lastname', String, nullable=False)
	title = Column('title', String, nullable=False)
	companyagency = Column('companyagency', String, nullable=False)
	organization = Column('organization', String, nullable=False)
	address1 = Column('address1', String, nullable=False)
	address2 = Column('address2', String, nullable=False)
	city = Column('city', String, nullable=False)
	state = Column('state', String, nullable=False)
	zipcode = Column('zipcode', Integer, nullable=False)
	phone1 = Column('phone1', String, nullable=False)
	phone2 = Column('phone2', String, nullable=False)


class InterviewProgress(db.Model):
	__tablename__ = 'InterviewProgress'

	id = Column('id', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	roleid = Column('roleid', Integer, nullable=False)
	interviewer = Column('interviewer', String, nullable=False)
	contactset = Column('contactset', Boolean, nullable=False)
	contactid = Column('contactid', Integer, nullable=False)
	status = Column('status', String, nullable=False)
	masterarchive = Column('masterarchive', Boolean, nullable=False)
	createtime = Column('createtime', DateTime, nullable=False)


class Messages(db.Model):
	__tablename__ = 'Messages'

	id = Column('id', Integer, nullable=False, primary_key=True)
	fromuserid = Column('fromuserid', Integer, nullable=False)
	touserid = Column('touserid', Integer, nullable=False)
	subject = Column('subject', String, nullable=False)
	message = Column('message', String, nullable=False)
	messagetime = Column('messagetime', DateTime, nullable=False)
	priority = Column('priority', String, nullable=False)


class Nessus_Procedures(db.Model):
	__tablename__ = 'Nessus_Procedures'

	procedureid = Column('procedureid', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	sourceid = Column('sourceid', String, nullable=False)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	title = Column('title', String, nullable=False)
	description = Column('description', String, nullable=False)
	severityid = Column('severityid', Integer, nullable=False)
	severity = Column('severity', String, nullable=False)
	port = Column('port', String, nullable=False)
	platformid = Column('platformid', Integer, nullable=False)
	depson = Column('depson', Integer, nullable=False)
	depsonresult = Column('depsonresult', String, nullable=False)
	deponoperator = Column('deponoperator', String, nullable=False)


class Platforms(db.Model):
	__tablename__ = 'Platforms'

	platformid = Column('platformid', Integer, nullable=False, primary_key=True)
	platform = Column('platform', String, nullable=False)


class PolicyParameters(db.Model):
	__tablename__ = 'PolicyParameters'

	id = Column('id', Integer, nullable=False, primary_key=True)
	requirementsource = Column('requirementsource', String, nullable=False)
	requirementid = Column('requirementid', Integer, nullable=False)
	parameter = Column('parameter', String, nullable=False)
	replacementvariable = Column('replacementvariable', String, nullable=False)


class ProcedureActions(db.Model):
	__tablename__ = 'ProcedureActions'

	actionid = Column('actionid', Integer, nullable=False, primary_key=True)
	procedureid = Column('procedureid', Integer, nullable=False)
	resultid = Column('resultid', Integer, nullable=False)
	nextprocedureid = Column('nextprocedureid', Integer, nullable=False)


class ProjectList(db.Model):
	__tablename__ = 'ProjectList'

	id = Column('id', Integer, nullable=False, primary_key=True)
	name = Column('name', String, nullable=False)
	abbreviation = Column('abbreviation', String, nullable=False)
	purpose = Column('purpose', String, nullable=False)
	scope = Column('scope', String, nullable=False)
	background = Column('background', String, nullable=False)
	createdate = Column('createdate', DateTime, nullable=False)
	lastmodified = Column('lastmodified', DateTime, nullable=False)
	signoffdate = Column('signoffdate', DateTime, nullable=False)
	createdby = Column('createdby', String, nullable=False)
	released = Column('released', Boolean, nullable=False)
	projecttype = Column('projecttype', String, nullable=False)
	status = Column('status', String, nullable=False)
	requirementsource = Column('requirementsource', String, nullable=False)
	reviewgrouping = Column('reviewgrouping', String, nullable=False)


class ProjectRequirements(db.Model):
	__tablename__ = 'ProjectRequirements'

	procrefid = Column('procrefid', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	projectrequirementid = Column('projectrequirementid', String, nullable=False)
	source = Column('source', String, nullable=False)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	assessmentid = Column('assessmentid', Integer, nullable=False)
	requirementid = Column('requirementid', Integer, nullable=False)
	procedureid = Column('procedureid', Integer, nullable=False)
	roleid = Column('roleid', Integer, nullable=False)
	targetid = Column('targetid', Integer, nullable=False)
	stepnum = Column('stepnum', Integer, nullable=False)
	tester = Column('tester', String, nullable=False)
	timestamp = Column('timestamp', DateTime, nullable=False)
	observedresult = Column('observedresult', String, nullable=False)
	resultid = Column('resultid', Integer, nullable=False)
	notes = Column('notes', String, nullable=False)
	vermethod = Column('vermethod', String, nullable=False)
	version = Column('version', Integer, nullable=False)
	findingreferenced = Column('findingreferenced', Boolean, nullable=False)
	findingid = Column('findingid', Integer, nullable=False)


class ProjectTypes(db.Model):
	__tablename__ = 'ProjectTypes'

	id = Column('id', Integer, nullable=False, primary_key=True)
	projecttype = Column('projecttype', String, nullable=False)
	description = Column('description', String, nullable=False)


class ResultList(db.Model):
	__tablename__ = 'ResultList'

	id = Column('id', Integer, nullable=False, primary_key=True)
	result = Column('result', String, nullable=False)


class ReviewProgress(db.Model):
	__tablename__ = 'ReviewProgress'

	reviewid = Column('reviewid', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	reviewer = Column('reviewer', String, nullable=False)
	grouping = Column('grouping', String, nullable=False)
	currentpoint = Column('currentpoint', Integer, nullable=False)
	point = Column('point', Integer, nullable=False)
	status = Column('status', String, nullable=False)
	masterarchive = Column('masterarchive', Boolean, nullable=False)


class ReviewSummary(db.Model):
	__tablename__ = 'ReviewSummary'

	reviewid = Column('reviewid', Integer, nullable=False, primary_key=True)
	requirementid = Column('requirementid', Integer, nullable=False)
	sourceparagraph = Column('sourceparagraph', String, nullable=False)
	username = Column('username', String, nullable=False)
	summary = Column('summary', String, nullable=False)
	compliancestatusid = Column('compliancestatusid', Integer, nullable=False)
	party = Column('party', String, nullable=False)
	originator = Column('originator', String, nullable=False)


class Targets(db.Model):
	__tablename__ = 'Targets'

	targetid = Column('targetid', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	systemname = Column('systemname', String, nullable=False)
	ipaddress = Column('ipaddress', String, nullable=False)
	macaddress = Column('macaddress', String, nullable=False)
	entrydate = Column('entrydate', DateTime, nullable=False)


class Tasks(db.Model):
	__tablename__ = 'Tasks'

	id = Column('id', Integer, nullable=False, primary_key=True)
	taskname = Column('taskname', String, nullable=False)
	taskdescription = Column('taskdescription', String, nullable=False)
	priority = Column('priority', String, nullable=False)
	progress = Column('progress', String, nullable=False)
	assigner = Column('assigner', Integer, nullable=False)
	assignee = Column('assignee', Integer, nullable=False)
	completed = Column('completed', Boolean, nullable=False)


class TempDocuments(db.Model):
	__tablename__ = 'TempDocuments'

	id = Column('id', Integer, nullable=False, primary_key=True)
	projectid = Column('projectid', Integer, nullable=False)
	frilyname = Column('frilyname', String, nullable=False)
	filename = Column('filename', String, nullable=False)
	description = Column('description', String, nullable=False)
	location = Column('location', String, nullable=False)
	lastmodifiedid = Column('lastmodifiedid', Integer, nullable=False)
	checkedout = Column('checkedout', Boolean, nullable=False)
	checkedoutuserid = Column('checkedoutuserid', Integer, nullable=False)
	initialuploaderid = Column('initialuploaderid', String, nullable=False)


class Verifications(db.Model):
	__tablename__ = 'Verifications'

	verificationmethod = Column('verificationmethod', String, nullable=False, primary_key=True)

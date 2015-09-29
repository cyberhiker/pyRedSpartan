class *800-53_r3_High_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	sourceprocedure = StringField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	stepnum = IntField(required = true)
	roleid = IntField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class *800-53_r3_Moderate_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	sourceprocedure = StringField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	stepnum = IntField(required = true)
	roleid = IntField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class *800-53_r3_Moderate_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	controlclass = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)
	controlenhancements = StringField(required = true)
	references = StringField(required = true)
	priority = nchar(required = true)


class *800-53_r4_All_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)
	references = StringField(required = true)


class *800-53_r4_Moderate_FedRAMP_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	sourceprocedure = StringField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	stepnum = IntField(required = true)
	roleid = IntField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class *800-53_r4_Moderate_FedRAMP_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	subcontrol = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)


class *800-53_r4_Moderate_FedRAMP_Requirements1(DynamicDocument):
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	subcontrol = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)


class *800-53_r4_Moderate_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	sourceprocedure = StringField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	stepnum = IntField(required = true)
	roleid = IntField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class *800-53_r4_Moderate_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)


class 800-53_r1_Moderate_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	stepnum = FloatField(required = true)
	intervieworder = IntField(required = true)
	roleid = IntField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	ruletext = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class 800-53_r1_Moderate_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	source = StringField(required = true)
	sourceparagraph = StringField(required = true)
	controlclass = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)
	controlenhancements = StringField(required = true)
	superceded = StringField(required = true)
	superedby = StringField(required = true)


class 800-53_r2_High_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	stepnum = FloatField(required = true)
	intervieworder = IntField(required = true)
	roleid = IntField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class 800-53_r2_High_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	source = StringField(required = true)
	sourceparagraph = StringField(required = true)
	controlclass = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)


class 800-53_r2_Low_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	stepnum = FloatField(required = true)
	intervieworder = IntField(required = true)
	roleid = IntField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class 800-53_r2_Low_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	source = StringField(required = true)
	sourceparagraph = StringField(required = true)
	controlclass = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)


class 800-53_r2_Moderate_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	requirementid = IntField(required = true)
	source = StringField(required = true)
	sourceparagraph = StringField(required = true)
	sourceprocedure = StringField(required = true)
	vermethod = StringField(required = true)
	overview = StringField(required = true)
	stepnum = IntField(required = true)
	roleid = IntField(required = true)
	evaluationsteps = StringField(required = true)
	expectedresults = StringField(required = true)
	depson = IntField(required = true)
	depentresult = IntField(required = true)


class 800-53_r2_Moderate_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	source = StringField(required = true)
	sourceparagraph = StringField(required = true)
	controlclass = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)


class 800-53_r3_All_Requirements(DynamicDocument):
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	controlclass = StringField(required = true)
	controlfamily = StringField(required = true)
	controltitle = StringField(required = true)
	controltext = StringField(required = true)
	supplementalguidance = StringField(required = true)
	controlenhancements = StringField(required = true)
	references = StringField(required = true)
	priority = nchar(required = true)


class ArchiveActivities(DynamicDocument):
	id = IntField(required = true)
	documentid = IntField(required = true)
	projectid = IntField(required = true)
	event = StringField(required = true)
	version = FloatField(required = true)
	versiondatetime = DateTimeField(required = true)
	uploaderid = StringField(required = true)


class Artifacts(DynamicDocument):
	id = IntField(required = true)
	assessmentid = IntField(required = true)
	documentid = IntField(required = true)
	procedureid = IntField(required = true)


class AssessmentProgress(DynamicDocument):
	id = IntField(required = true)
	projectid = IntField(required = true)
	roleid = IntField(required = true)
	assessor = StringField(required = true)
	interviewcontactset = BooleanField(required = true)
	interviewcontactid = IntField(required = true)
	status = StringField(required = true)
	masterarchive = BooleanField(required = true)
	createtime = DateTimeField(required = true)


class AssessmentRoles(DynamicDocument):
	id = IntField(required = true)
	role = StringField(required = true)
	description = StringField(required = true)
	type = StringField(required = true)


class ComplianceStatuses(DynamicDocument):
	id = IntField(required = true)
	status = nchar(required = true)


class CrossReferences(DynamicDocument):
	crossrefid = IntField(required = true)
	source1table = StringField(required = true)
	source2table = StringField(required = true)
	source1id = IntField(required = true)
	source2id = IntField(required = true)


class DocumentActivity(DynamicDocument):
	id = IntField(required = true)
	documentid = IntField(required = true)
	projectid = IntField(required = true)
	event = StringField(required = true)
	version = FloatField(required = true)
	versiondatetime = DateTimeField(required = true)
	uploaderid = StringField(required = true)


class Documents(DynamicDocument):
	id = IntField(required = true)
	projectid = IntField(required = true)
	frilyname = StringField(required = true)
	filename = StringField(required = true)
	description = StringField(required = true)
	location = StringField(required = true)
	hashvalue = StringField(required = true)
	initialuploaderid = StringField(required = true)
	lastmodifiedid = StringField(required = true)
	checkedout = BooleanField(required = true)
	checkedoutuserid = StringField(required = true)


class FindingActionResults(DynamicDocument):
	id = IntField(required = true)
	actionresult = StringField(required = true)
	description = StringField(required = true)


class FindingActions(DynamicDocument):
	id = IntField(required = true)
	findingid = IntField(required = true)
	actiondate = DateTimeField(required = true)
	actioner = StringField(required = true)
	actiontaken = StringField(required = true)
	actiondescription = StringField(required = true)
	actionresult = IntField(required = true)
	entrydatetime = DateTimeField(required = true)


class FindingRelationship(DynamicDocument):
	id = IntField(required = true)
	findingid = IntField(required = true)
	procrefid = IntField(required = true)
	projectid = IntField(required = true)
	type = StringField(required = true)


class Findings(DynamicDocument):
	findingid = IntField(required = true)
	projectid = IntField(required = true)
	findingtitle = StringField(required = true)
	riskrating = StringField(required = true)
	findingdiscussion = StringField(required = true)
	findingrecommation = StringField(required = true)
	masterstatus = IntField(required = true)


class InterviewContacts(DynamicDocument):
	id = IntField(required = true)
	projectid = IntField(required = true)
	roleid = IntField(required = true)
	firstname = StringField(required = true)
	lastname = StringField(required = true)
	title = StringField(required = true)
	companyagency = StringField(required = true)
	organization = StringField(required = true)
	address1 = StringField(required = true)
	address2 = StringField(required = true)
	city = StringField(required = true)
	state = StringField(required = true)
	zipcode = bigint(required = true)
	phone1 = StringField(required = true)
	phone2 = StringField(required = true)


class InterviewProgress(DynamicDocument):
	id = IntField(required = true)
	projectid = IntField(required = true)
	roleid = IntField(required = true)
	interviewer = StringField(required = true)
	contactset = BooleanField(required = true)
	contactid = IntField(required = true)
	status = StringField(required = true)
	masterarchive = BooleanField(required = true)
	createtime = DateTimeField(required = true)


class Messages(DynamicDocument):
	id = IntField(required = true)
	fromuserid = IntField(required = true)
	touserid = IntField(required = true)
	subject = StringField(required = true)
	message = StringField(required = true)
	messagetime = DateTimeField(required = true)
	priority = StringField(required = true)


class Nessus_Procedures(DynamicDocument):
	procedureid = IntField(required = true)
	projectid = IntField(required = true)
	sourceid = StringField(required = true)
	sourceparagraph = StringField(required = true)
	title = StringField(required = true)
	description = StringField(required = true)
	severityid = IntField(required = true)
	severity = StringField(required = true)
	port = StringField(required = true)
	platformid = IntField(required = true)
	depson = IntField(required = true)
	depsonresult = StringField(required = true)
	deponoperator = StringField(required = true)


class Platforms(DynamicDocument):
	platformid = IntField(required = true)
	platform = StringField(required = true)


class PolicyParameters(DynamicDocument):
	id = IntField(required = true)
	requirementsource = StringField(required = true)
	requirementid = IntField(required = true)
	parameter = StringField(required = true)
	replacementvariable = StringField(required = true)


class ProcedureActions(DynamicDocument):
	actionid = IntField(required = true)
	procedureid = IntField(required = true)
	resultid = IntField(required = true)
	nextprocedureid = IntField(required = true)


class ProjectList(DynamicDocument):
	id = IntField(required = true)
	name = StringField(required = true)
	abbreviation = StringField(required = true)
	purpose = StringField(required = true)
	scope = StringField(required = true)
	background = StringField(required = true)
	createdate = DateTimeField(required = true)
	lastmodified = DateTimeField(required = true)
	signoffdate = DateTimeField(required = true)
	createdby = StringField(required = true)
	released = BooleanField(required = true)
	projecttype = StringField(required = true)
	status = StringField(required = true)
	requirementsource = StringField(required = true)
	reviewgrouping = StringField(required = true)


class ProjectRequirements(DynamicDocument):
	procrefid = IntField(required = true)
	projectid = IntField(required = true)
	projectrequirementid = StringField(required = true)
	source = StringField(required = true)
	sourceparagraph = StringField(required = true)
	assessmentid = IntField(required = true)
	requirementid = IntField(required = true)
	procedureid = IntField(required = true)
	roleid = IntField(required = true)
	targetid = IntField(required = true)
	stepnum = IntField(required = true)
	tester = StringField(required = true)
	timestamp = DateTimeField(required = true)
	observedresult = StringField(required = true)
	resultid = IntField(required = true)
	notes = StringField(required = true)
	vermethod = StringField(required = true)
	version = IntField(required = true)
	findingreferenced = BooleanField(required = true)
	findingid = IntField(required = true)


class ProjectTypes(DynamicDocument):
	id = IntField(required = true)
	projecttype = StringField(required = true)
	description = StringField(required = true)


class ResultList(DynamicDocument):
	id = IntField(required = true)
	result = char(required = true)


class ReviewProgress(DynamicDocument):
	reviewid = IntField(required = true)
	projectid = IntField(required = true)
	reviewer = StringField(required = true)
	grouping = StringField(required = true)
	currentpoint = IntField(required = true)
	point = IntField(required = true)
	status = StringField(required = true)
	masterarchive = BooleanField(required = true)


class ReviewSummary(DynamicDocument):
	reviewid = IntField(required = true)
	requirementid = IntField(required = true)
	sourceparagraph = StringField(required = true)
	username = StringField(required = true)
	summary = text_basic(required = true)
	compliancestatusid = IntField(required = true)
	party = StringField(required = true)
	originator = StringField(required = true)


class Targets(DynamicDocument):
	targetid = IntField(required = true)
	projectid = IntField(required = true)
	systemname = StringField(required = true)
	ipaddress = StringField(required = true)
	macaddress = StringField(required = true)
	entrydate = DateTimeField(required = true)


class Tasks(DynamicDocument):
	id = IntField(required = true)
	taskname = StringField(required = true)
	taskdescription = StringField(required = true)
	priority = StringField(required = true)
	progress = StringField(required = true)
	assigner = IntField(required = true)
	assignee = IntField(required = true)
	completed = BooleanField(required = true)


class TempDocuments(DynamicDocument):
	id = IntField(required = true)
	projectid = IntField(required = true)
	frilyname = StringField(required = true)
	filename = StringField(required = true)
	description = StringField(required = true)
	location = StringField(required = true)
	lastmodifiedid = IntField(required = true)
	checkedout = BooleanField(required = true)
	checkedoutuserid = IntField(required = true)
	initialuploaderid = IntField(required = true)


class Verifications(DynamicDocument):
	verificationmethod = StringField(required = true)

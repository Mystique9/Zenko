import pytest
import zenko_e2e.conf as conf
import zenko_e2e.util as util

'''
This module contains all boto3 Buckets created from the various backends or zenko itself
'''

def create_bucket(resource, name):
	return resource.Bucket(name)

# These are buckets from the actual cloud backend

@pytest.fixture(scope = 'session')
def aws_target_bucket(aws_resource):
	bucket = create_bucket(aws_resource, conf.AWS_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def gcp_target_bucket(gcp_resource):
	bucket =  create_bucket(gcp_resource, conf.GCP_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def azure_target_bucket(azure_resource):
	bucket =  create_bucket(azure_resource, conf.AZURE_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def wasabi_target_bucket(wasabi_resource):
	bucket = create_bucket(wasabi_resource, conf.WASABI_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def digital_ocean_target_bucket(digital_ocean_resource):
	bucket = create_bucket(digital_ocean_resource, conf.DO_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def aws_crr_target_bucket(aws_resource):
	bucket = create_bucket(aws_resource, conf.AWS_CRR_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def gcp_crr_target_bucket(gcp_resource):
	bucket = create_bucket(gcp_resource, conf.GCP_CRR_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def azure_crr_target_bucket(azure_resource):
	bucket = create_bucket(azure_resource, conf.AZURE_CRR_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def wasabi_crr_target_bucket(wasabi_resource):
	bucket = create_bucket(wasabi_resource, conf.WASABI_CRR_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

@pytest.fixture(scope = 'session')
def digital_crr_ocean_bucket(digital_ocean_resource):
	bucket = create_bucket(digital_ocean_resource, conf.DO_CRR_TARGET_BUCKET)
	yield bucket
	util.cleanup_bucket(bucket, delete_bucket= False)

# A generic bucket in zenko
@pytest.fixture(scope = 'function')
def zenko_bucket(zenko_resource):
	name = util.gen_bucket_name()
	bucket = create_bucket(zenko_resource, name)
	yield bucket
	util.cleanup_bucket(bucket)

# These are buckets that exists in zenko, not on the actual cloud services
# They are configured to use backend specific endpoints,
# with default locations configured to the respective backend
@pytest.fixture
def aws_ep_bucket(aws_endpoint_resource):
	name = util.gen_bucket_name()
	bucket = create_bucket(aws_endpoint_resource, name)
	yield bucket
	util.cleanup_bucket(bucket)

@pytest.fixture
def gcp_ep_bucket(gcp_endpoint_resource):
	name = util.gen_bucket_name()
	bucket = create_bucket(gcp_endpoint_resource, name)
	yield bucket
	util.cleanup_bucket(bucket)

@pytest.fixture
def azure_ep_bucket(azure_endpoint_resource):
	name = util.gen_bucket_name()
	bucket = create_bucket(azure_endpoint_resource, name)
	yield bucket
	util.cleanup_bucket(bucket)

@pytest.fixture
def wasabi_ep_bucket(wasabi_endpoint_resource):
	name = util.gen_bucket_name()
	bucket = create_bucket(wasabi_endpoint_resource, name)
	yield bucket
	util.cleanup_bucket(bucket)

@pytest.fixture
def digital_ocean_ep_bucket(digital_ocean_endpoint_resource):
	name = util.gen_bucket_name()
	bucket = create_bucket(digital_ocean_endpoint_resource, name)
	yield bucket
	util.cleanup_bucket(bucket)

# These buckets are configured using a LocationConstraint to each backend

@pytest.fixture
def aws_loc_bucket(zenko_bucket):
	name = util.gen_bucket_name()
	loc_config = { 'LocationConstraint': conf.AWS_BACKEND }
	zenko_bucket.create(
		CreateBucketConfiguration = loc_config
	)
	return zenko_bucket

@pytest.fixture
def gcp_loc_bucket(zenko_bucket):
	name = util.gen_bucket_name()
	loc_config = { 'LocationConstraint': conf.GCP_BACKEND }
	zenko_bucket.create(
		CreateBucketConfiguration = loc_config
	)
	return zenko_bucket

@pytest.fixture
def azure_loc_bucket(zenko_bucket):
	name = util.gen_bucket_name()
	loc_config = { 'LocationConstraint': conf.AZURE_BACKEND }
	zenko_bucket.create(
		CreateBucketConfiguration = loc_config
	)
	return zenko_bucket

@pytest.fixture
def wasabi_loc_bucket(zenko_bucket):
	name = util.gen_bucket_name()
	loc_config = { 'LocationConstraint': conf.WASABI_BACKEND }
	zenko_bucket.create(
		CreateBucketConfiguration = loc_config
	)
	return zenko_bucket

@pytest.fixture
def digital_ocean_loc_bucket(zenko_bucket):
	name = util.gen_bucket_name()
	loc_config = { 'LocationConstraint': conf.DO_BACKEND }
	zenko_bucket.create(
		CreateBucketConfiguration = loc_config
	)
	return zenko_bucket

# These are bucket in zenko with replication enabled

@pytest.fixture
def aws_crr_bucket(vault, aws_replication_policy, crr_role):
	bucket, policy = aws_replication_policy
	bucket.create()
	policy.attach_role(RoleName = crr_role.name)
	bucket.Versioning().enable()
	doc = util.format_json(conf.REPL_CONF_TPL,
		role = crr_role.arn,
		prefix = '',
		dest = 'arn:aws:s3:::stuff',
		backends = conf.AWS_CRR_BACKEND,
		asString = False
		)
	bucket.meta.client.put_bucket_replication(
		Bucket = bucket.name,
		ReplicationConfiguration = doc
		)
	print(bucket.name)
	yield bucket

@pytest.fixture
def gcp_crr_bucket(vault, gcp_replication_policy, crr_role):
	bucket, policy = gcp_replication_policy
	bucket.create()
	policy.attach_role(RoleName = crr_role.name)
	bucket.Versioning().enable()
	doc = util.format_json(conf.REPL_CONF_TPL,
		role = crr_role.arn,
		prefix = '',
		dest = 'arn:aws:s3:::stuff',
		backends = conf.GCP_CRR_BACKEND,
		asString = False
		)
	bucket.meta.client.put_bucket_replication(
		Bucket = bucket.name,
		ReplicationConfiguration = doc
		)
	return bucket

@pytest.fixture
def azure_crr_bucket(vault, azure_replication_policy, crr_role):
	bucket, policy = azure_replication_policy
	bucket.create()
	policy.attach_role(RoleName = crr_role.name)
	bucket.Versioning().enable()
	doc = util.format_json(conf.REPL_CONF_TPL,
		role = crr_role.arn,
		prefix = '',
		dest = 'arn:aws:s3:::stuff',
		backends = conf.AZURE_CRR_BACKEND,
		asString = False
		)
	bucket.meta.client.put_bucket_replication(
		Bucket = bucket.name,
		ReplicationConfiguration = doc
		)
	return bucket

@pytest.fixture
def wasabi_crr_bucket(vault, wasabi_replication_policy, crr_role):
	bucket, policy = wasabi_replication_policy
	bucket.create()
	policy.attach_role(RoleName = crr_role.name)
	bucket.Versioning().enable()
	doc = util.format_json(conf.REPL_CONF_TPL,
		role = crr_role.arn,
		prefix = '',
		dest = 'arn:aws:s3:::stuff',
		backends = conf.WASABI_CRR_BACKEND,
		asString = False
		)
	bucket.meta.client.put_bucket_replication(
		Bucket = bucket.name,
		ReplicationConfiguration = doc
		)
	return bucket

@pytest.fixture
def digital_ocean_crr_bucket(vault, digital_ocean_replication_policy, crr_role):
	bucket, policy = digital_ocean_replication_policy
	bucket.create()
	policy.attach_role(RoleName = crr_role.name)
	bucket.Versioning().enable()
	doc = util.format_json(conf.REPL_CONF_TPL,
		role = crr_role.arn,
		prefix = '',
		dest = 'arn:aws:s3:::stuff',
		backends = conf.DO_CRR_BACKEND,
		asString = False
		)
	bucket.meta.client.put_bucket_replication(
		Bucket = bucket.name,
		ReplicationConfiguration = doc
		)
	return bucket

@pytest.fixture
def multi_crr_bucket(vault, multi_replication_policy, crr_role):
	bucket, policy = multi_replication_policy
	bucket.create()
	policy.attach_role(RoleName = crr_role.name)
	bucket.Versioning().enable()
	backends = ','.join([getattr(conf, '%s_CRR_BACKEND'%b) for b in conf.MULTI_CRR_TARGETS])
	doc = util.format_json(conf.REPL_CONF_TPL,
		role = crr_role.arn,
		prefix = '',
		dest = 'arn:aws:s3:::stuff',
		backends = backends,
		asString = False
		)
	bucket.meta.client.put_bucket_replication(
		Bucket = bucket.name,
		ReplicationConfiguration = doc
		)
	return bucket

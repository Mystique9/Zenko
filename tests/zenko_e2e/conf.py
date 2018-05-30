import os
from datetime import timedelta
import requests
import socket

def get_env(key, default = None, error = False):
	if not error:
		return os.environ.get(key, default)
	return os.environ[key]

SERVICEACCOUNT_PATH = '/var/run/secrets/kubernetes.io/serviceaccount'

K8S_NAMESPACE = os.getenv('ZENKO_K8S_NAMESPACE', None)
if K8S_NAMESPACE is None:
    try:
        with open(os.path.join(SERVICEACCOUNT_PATH, 'namespace'), 'r') as nsfd:
            K8S_NAMESPACE = nsfd.read()
    except IOError:
        K8S_NAMESPACE = None
        raise RuntimeError('Unable to determine Zenko K8s namespace')


ZENKO_HELM_RELEASE = os.getenv('ZENKO_HELM_RELEASE', None)

ZENKO_ENDPOINT = get_env('CLOUDSERVER_FRONT_ENDPOINT', 'http://%s-cloudserver-front:80'%ZENKO_HELM_RELEASE)
ZENKO_VAULT_ENDPOINT = get_env('ZENKO_VAULT_ENDPOINT', 'http://zenko.test:8600')
ORBIT_ENDPOINT = get_env('ORBIT_ENDPOINT', 'http://ciutil-orbit-simulator:4222')

ZENKO_ROOT_ENDPOINT = ZENKO_ENDPOINT[ZENKO_ENDPOINT.index('//') + 2:]
# The endpoints configured with a default location
ZENKO_AWS_ENDPOINT = get_env('ZENKO_AWS_ENDPOINT', 'http://aws.%s'%ZENKO_ROOT_ENDPOINT)
ZENKO_GCP_ENDPOINT = get_env('ZENKO_GCP_ENDPOINT',  'http://gcp.%s'%ZENKO_ROOT_ENDPOINT)
ZENKO_AZURE_ENDPOINT =  get_env('ZENKO_AZURE_ENDPOINT', 'http://azure.%s'%ZENKO_ROOT_ENDPOINT)
ZENKO_WASABI_ENDPOINT = get_env('ZRNKO_WASABI_ENDPOINT', 'http://wasabi.%s'%ZENKO_ROOT_ENDPOINT)
ZENKO_DO_ENDPOINT = get_env('ZENKO_DO_ENDPOINT', 'http://do.%s'%ZENKO_ROOT_ENDPOINT)
# Setup endpoints in hosts file

try:
    orbit_ip = socket.gethostbyname(ORBIT_ENDPOINT.split('//')[1].split(':')[0])
    with open('/etc/hosts', 'a') as hosts:
        hosts.write('%s\t%s'%(orbit_ip, ' '.join([
            ZENKO_AWS_ENDPOINT,
            ZENKO_AZURE_ENDPOINT,
            ZENKO_DO_ENDPOINT,
            ZENKO_GCP_ENDPOINT,
            ZENKO_WASABI_ENDPOINT
        ])))
except socket.gaierror as exc:
    raise RuntimeError('Unable to resolve Orbit management endpoint')



# Sets whether to verify ssl certicates of remote services
VERIFY_CERTIFICATES = get_env('VERIFY_CERTIFICATES', False)

# When False, objects placed in cloud backends will have their origin bucket name added as prefix
# When True, objects will be place in backend cloud buckets with their name unchanged
#	NOTE This can result in name conflict if multiple zenko buckets target the same backennd bucket
BUCKET_MATCH = False


# The names of the backends as configured in zenko
AWS_BACKEND = get_env('AWS_BACKEND', 'awsbackend')
GCP_BACKEND = get_env('GCP_BACKEND', 'gcpbackend')
AZURE_BACKEND = get_env('AZURE_BACKEND', 'azurebackend')
WASABI_BACKEND = get_env('WASABI_BACKEND', 'wasabibackend')
DO_BACKEND = get_env('DO_BACKEND', 'dobackend')

AWS_CRR_BACKEND = get_env('AWS_CRR_BACKEND', 'awsbackend-crr')
GCP_CRR_BACKEND = get_env('GCP_CRR_BACKEND', 'gcpbackend-crr')
AZURE_CRR_BACKEND = get_env('AZURE_CRR_BACKEND', 'azurebackend-crr')
WASABI_CRR_BACKEND = get_env('WASABI_CRR_BACKEND', 'wasabibackend-crr')
DO_CRR_BACKEND = get_env('DO_CRR_BACKEND', 'dobackend-crr')

# The endpoints to feed boto3 sdk
GCP_ENDPOINT = get_env('GCP_ENDPOINT', 'https://storage.googleapis.com')
AZURE_ENDPOINT = get_env('AZURE_ENDPOINT', 'http://azure.test:9000')
WASABI_ENDPOINT = get_env('ZENKO_WASABI_ENDPOINT', 'https://s3.wasabisys.com')
DO_ENDPOINT = get_env('DO_ENDPOINT', 'https://nyc3.digitaloceanspaces.com')


# This is the bucket the various cloud backends target
# In other words, where my stuff gonna end up
AWS_TARGET_BUCKET = get_env('AWS_S3_BUCKET_NAME', 'zenko-aws-target-bucket')
GCP_TARGET_BUCKET = get_env('GCP_BUCKET_NAME', 'zenko-gcp-target-bucket')
AZURE_TARGET_BUCKET = get_env('AZURE_BACKEND_CONTAINER_NAME', 'zenko-azure-target-bucket')
WASABI_TARGET_BUCKET = get_env('WASABI_TARGET_BUCKET', 'zenko-wasabi-target-bucket')
DO_TARGET_BUCKET = get_env('DO_TARGET_BUCKET', 'zenko-digitalocean-target-bucket')

# The target buckets configured for CR replication
AWS_CRR_TARGET_BUCKET = get_env('AWS_S3_BACKBEAT_BUCKET_NAME', 'zenko-aws-crr-target-bucket')
GCP_CRR_TARGET_BUCKET = get_env('GCP_CRR_BUCKET_NAME', 'zenko-gcp-crr-target-bucket')
AZURE_CRR_TARGET_BUCKET = get_env('AZURE_BACKBEAT_CONTAINER_NAME', 'zenko-azure-crr-target-bucket')
WASABI_CRR_TARGET_BUCKET = get_env('WASABI_TARGET_BUCKET', 'zenko-wasabi-crr-target-bucket')
DO_CRR_TARGET_BUCKET = get_env('DO_TARGET_BUCKET', 'zenko-digitalocean-crr-target-bucket')

AWS_CRR_SRC_BUCKET = get_env('AWS_S3_BACKBEAT_SRC_BUCKET_NAME', 'zenko-aws-crr-src-bucket')
GCP_CRR_SRC_BUCKET = get_env('GCP_CRR_SRC_BUCKET_NAME', 'zenko-gcp-crr-src-bucket')
AZURE_CRR_SRC_BUCKET = get_env('AZURE_BACKBEAT_SRC_CONTAINER_NAME', 'zenko-azure-crr-src-bucket')
WASABI_CRR_SRC_BUCKET = get_env('WASABI_CRR_SRC_BUCKET', 'zenko-wasabi-crr-src-bucket')
DO_CRR_SRC_BUCKET = get_env('DO_CRR_SRC_BUCKET', 'zenko-do-crr-src-bucket')
MULTI_CRR_SRC_BUCKET = get_env('MULTI_CRR_SRC_BUCKET', 'zenko-multi-crr-src-bucket')


BACKBEAT_METRICS_ENDPOINT = get_env('BACKBEAT_METRICS_ENDPOINT', 'https://zenko.test:')

# This should list the prefixes for the conf values of all backends to be tested with 1-M replication
MULTI_CRR_TARGETS = [
	'AWS', 'GCP', 'AZURE', 'WASABI'
]

AWS_ACCESS_KEY = get_env('AWS_S3_BACKEND_ACCESS_KEY', error = True)
AWS_SECRET_KEY = get_env('AWS_S3_BACKEND_SECRET_KEY', error = True)

GCP_ACCESS_KEY = get_env('AWS_GCP_BACKEND_ACCESS_KEY', error = True)
GCP_SECRET_KEY = get_env('AWS_GCP_BACKEND_SECRET_KEY', error = True)

AZURE_ACCESS_KEY = get_env('AZURE_BACKEND_ACCOUNT_NAME', error = True)
AZURE_SECRET_KEY = get_env('AZURE_BACKEND_ACCESS_KEY', error = True)

ZENKO_ACCESS_KEY = get_env('ZENKO_ACCESS_KEY')
ZENKO_SECRET_KEY = get_env('ZENKO_SECRET_KEY')
if ZENKO_ACCESS_KEY is None and ZENKO_SECRET_KEY is None:
    creds_ep = ORBIT_ENDPOINT + '/api/v1/instance/uuid/account-credentials'
    resp = requests.get(creds_ep)
    if resp.status_code == 200:
        ZENKO_ACCESS_KEY = resp.json().get('accessKey', None)
        ZENKO_SECRET_KEY = resp.json().get('secretKey', None)
        print('+'*50)
        print(ZENKO_ACCESS_KEY, ZENKO_SECRET_KEY)
        print('+'*50)
        if ZENKO_ACCESS_KEY is None and ZENKO_SECRET_KEY is None:
            raise RuntimeError('Unable to retrieve credentials from orbit!')
    else:
        raise RuntimeError('Unable to retrieve credentials from orbit!')

# Ignore these as theyre overiding the config with 'legacy' values
# AWS_TARGET_BUCKET = get_env('AWS_TARGET_BUCKET', 'zenko-aws-backend-test-bucket')
# GCP_TARGET_BUCKET = get_env('GCP_TARGET_BUCKET', 'zenko-gcp-backend-test-bucket')
# AZURE_TARGET_BUCKET = get_env('AZURE_TARGET_BUCKET', 'zenko-azure-backend-test-bucket')
# AWS_CRR_TARGET_BUCKET = get_env('AWS_CRR_TARGET_BUCKET', 'zenko-aws-crr-test-bucket')
# GCP_CRR_TARGET_BUCKET = get_env('GCP_CRR_TARGET_BUCKET', 'zenko-gcp-crr-test-bucket')
# AZURE_CRR_TARGET_BUCKET = get_env('AZURE_CRR_TARGET_BUCKET', 'zenko-azure-crr-test-bucket')

REPL_POLICY_TPL = '''
{{
	"Version": "2012-10-17",
	"Statement": [
		{{
			"Effect": "Allow",
			"Action": [
				"s3:GetObjectVersion",
				"s3:GetObjectVersionAcl"
			],
			"Resource": [
				"arn:aws:s3:::{src}/*"
			]
		}},
		{{
			"Effect": "Allow",
			"Action": [
				"s3:ListBucket",
				"s3:GetReplicationConfiguration"
			],
			"Resource": [
				"arn:aws:s3:::{src}"
			]
		}},
		{{
			"Effect": "Allow",
			"Action": [
				"s3:ReplicateObject",
				"s3:ReplicateDelete"
			],
			"Resource": "arn:aws:s3:::{dest}/*"
		}}
	]
}}
'''

MULTI_REPL_POLICY_TPL_PT1 = '''
{{
	"Version": "2012-10-17",
	"Statement": [
		{{
			"Effect": "Allow",
			"Action": [
				"s3:GetObjectVersion",
				"s3:GetObjectVersionAcl"
			],
			"Resource": [
				"arn:aws:s3:::{src}/*"
			]
		}},
		{{
			"Effect": "Allow",
			"Action": [
				"s3:ListBucket",
				"s3:GetReplicationConfiguration"
			],
			"Resource": [
				"arn:aws:s3:::{src}"
			]
		}}
	]
}}
'''

MULTI_REPL_POLICY_TPL_PT2 = '''
		{{
			"Effect": "Allow",
			"Action": [
				"s3:ReplicateObject",
				"s3:ReplicateDelete"
			],
			"Resource": "arn:aws:s3:::{dest}/*"
		}}
'''

ROLE_CONF = '''
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"Service": "backbeat"
			},
			"Action": "sts:AssumeRole"
		}
	]
}
'''

REPL_CONF_TPL = '''{{"Role": "{role}",
	"Rules": [
	  {{
		"Prefix": "{prefix}",
		"Status": "Enabled",
		"Destination": {{
		  "Bucket": "{dest}",
		  "StorageClass": "{backends}"
		}}
	  }}
	]
  }}'''


METADATA_EXAMPLE = {
	'color': 'red',
	'flavor': 'strawberry'
}

METADATA_EXAMPLE2 = {
	'color': 'blue',
	'flavor': 'strawberry'
}


EXPIRY_DELTA = timedelta(minutes = 1)

EXPIRY_RULE = {
  'Rules': [{
    'Expiration': {
      'Date': None,
    },
    'Status': 'Enabled',
	'Filter': {
		'Prefix': ''
	}
  }]
}

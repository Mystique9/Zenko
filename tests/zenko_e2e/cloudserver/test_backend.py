import zenko_e2e.util as util
import logging
from ..fixtures import *

logging.basicConfig(level = logging.INFO,
				format =  '%(asctime)s %(name)s %(levelname)s: %(message)s',
				datefmt = '%S')

_log = logging.getLogger('test')


@pytest.mark.skip(reason ='Not implemented in CI')
def test_ring_storage(zenko_bucket, testfile):
	util.mark_test('RING STORAGE DEFAULT EP LOCATION')
	zenko_bucket.create()
	zenko_bucket.put_object(
		Body = testfile,
		Key = 'zenko-test'
	)
	assert util.check_object('zenko-test', testfile, zenko_bucket)

@pytest.mark.skip(reason ='Not implemented in CI')
def test_aws_storage(aws_ep_bucket, aws_target_bucket, testfile):
	util.mark_test('AWS STORAGE DEFAULT EP LOCATION')
	aws_ep_bucket.create()
	aws_ep_bucket.put_object(
		Body = testfile,
		Key = 'aws-test'
	)
	assert util.check_object('aws-test', testfile, aws_ep_bucket, aws_target_bucket)

@pytest.mark.skip(reason ='Not implemented in CI')
def test_gcp_storage(gcp_ep_bucket, gcp_target_bucket, testfile):
	util.mark_test('GCP STORAGE DEFAULT EP LOCATION')
	gcp_ep_bucket.create()
	gcp_ep_bucket.put_object(
		Body = testfile,
		Key = 'gcp-test'
	)
	assert util.check_object('gcp-test', testfile, gcp_ep_bucket, gcp_target_bucket)

@pytest.mark.skip(reason ='Not implemented in CI')
def test_azure_storage(azure_ep_bucket, azure_target_bucket, testfile):
	util.mark_test('AZURE STORAGE DEFAULT EP LOCATION')
	azure_ep_bucket.create()
	azure_ep_bucket.put_object(
		Body = testfile,
		Key = 'azure-test'
	)
	assert util.check_object('azure-test', testfile, azure_ep_bucket, azure_target_bucket)

@pytest.mark.skip(reason ='Not implemented in CI')
def test_wasabi_storage(wasabi_ep_bucket, wasabi_target_bucket, testfile):
	util.mark_test('WASABI STORAGE DEFAULT EP LOCATION')
	wasabi_ep_bucket.create()
	wasabi_ep_bucket.put_object(
		Body = testfile,
		Key = 'wasabi-test'
	)
	assert util.check_object('wasabi-test', testfile, wasabi_ep_bucket, wasabi_target_bucket)

@pytest.mark.skip(reason = 'Digital Ocean Spaces is super flakey causing this test to fail')
def test_digital_ocean_storage(digital_ocean_ep_bucket, digital_ocean_target_bucket, testfile):
	util.mark_test('DIGITAL OCEAN STORAGE DEFAULT EP LOCATION')
	digital_ocean_ep_bucket.create()
	digital_ocean_ep_bucket.put_object(
		Body = testfile,
		Key = 'digital-ocean-test'
	)
	assert uitl.check_object('digital-ocean-test', testfile, digital_ocean_ep_bucket, digital_ocean_target_bucket)

from ..fixtures import *
import logging

logging.basicConfig(level = logging.DEBUG,
				format =  '%(asctime)s %(name)s %(levelname)s: %(message)s',
				datefmt = '%S')

@pytest.mark.skip(reason = 'This test requires manual work to complete')
def test_crr_retry(aws_crr_bucket, aws_crr_target_bucket, testfile):
	util.mark_test('CRR RETRY')
	aws_crr_bucket.put_object(
		Body = testfile,
		Key = 'crr-retry-test'
	)
	util.remark('Finished uploading')
	input()
	assert util.check_object('crr-retry-test', testfile, aws_crr_bucket, aws_crr_target_bucket, timeout = 30)
	# assert util.check_object(aws_crr_bucket, 'crr-retry-test', mpufile)
	# assert util.check_object(aws_crr_target_bucket, 'crr-retry-test', mpufile, timeout = 30)

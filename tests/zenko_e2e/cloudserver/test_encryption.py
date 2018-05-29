from zenko_e2e.fixtures import *
import zenko_e2e.util as util


def test_serverside_encryption(encrypted_bucket, aws_target_bucket, testfile):
    encrypted_bucket.put_object(
        Key = 'enc-test'
        Body = testfile
    )
    refHash = hashobj(testfile)
    localHash = get_object_hash(encrypted_bucket, 'enc-test')
    assert refHash == localHash
    remotekey = '%s/%s'%(encrypted_bucket.name, 'enc-test') if not conf.BUCKET_MATCH else 'enc-test'
    remoteHash = get_object_hash(aws_target_bucket, 'enc-test', timeout, backoff)
    assert refHash != remoteHash

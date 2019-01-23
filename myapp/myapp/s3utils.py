# from storages.backends.s3boto import S3BotoStorage
# StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
# MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
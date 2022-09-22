import time

class CloudFront_commands():
    def __init__(self, session, DistributionId):
        self._client = session
        self._ecs = self._client.client('cloudfront')
        self._DistributionId = DistributionId

    def clearCache(self):
        response = self._ecs.create_invalidation(DistributionId=self._DistributionId,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*',
                ]
            },
            'CallerReference': str(time.time())
        }
        )
        print(response)
        
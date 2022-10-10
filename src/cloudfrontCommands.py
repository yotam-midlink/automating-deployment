import time

class CloudFront_commands():
    def __init__(self, session, DistributionId):
        self._client = session
        self._cloudfront = self._client.client('cloudfront')
        self._DistributionId = DistributionId

    def clearCache(self):
        response = self._cloudfront.create_invalidation(DistributionId=self._DistributionId,
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
        return(self.__isClearCacheCompleted(response['Invalidation']['Id']))


    def __isClearCacheCompleted(self, invalidationId):
        for i in range (10):
            if self.__checkIfInvalidationCompleted(invalidationId):
                return True
            time.sleep(15)
        return False

    def __checkIfInvalidationCompleted(self, invalidationId):
        response = self._cloudfront.get_invalidation(DistributionId = self._DistributionId, Id =invalidationId)
        status = response['Invalidation']['Status']
        print(f"cache is {status}")
        return 'Completed' == status
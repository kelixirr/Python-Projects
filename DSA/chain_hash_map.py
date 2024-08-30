from Maps.hash_map_base import HashMapBase
from Maps.unsorted_table_maps import UnsortedTableMaps

class ChainHashMap(HashMapBase):

    def _bucket_getiteme(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMaps()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))
        del bucket[k]

    def __item__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
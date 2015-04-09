def new(num_bucket = 256):
    # initializing map
    aMap = []
    for i in range(0, num_bucket):
        aMap.append([])
    return aMap
    
def hash_key (aMap, key):
    #given a key this will create a number and then convert it to an index for a map bucket
    return hash(key) % len(aMap)
    
def get_bucket(aMap,key):
    #from key find bucket
    bucket_id = hash_key(aMap,Key)
    return aMap[bucket_id]
    
def get_slot(aMap, Key, default=None)
    #return the index key and values of a slot found in a bucket
    
    bucket = get_bucket(aMap, key)
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i,k,v
    
    return -1, key , default
    
def get(aMap, key, default=None):
    """get the values in the bucket for the given key """
    i, k, v = get_slot(aMap, key, default =default)
    return v
    
def set(aMap, key, value):
    """sets teh key to the value , replacing any existing value"""
    bucket = get_bucket(aMap,key)
    i,k,v = get_slot(aMap,key)
    
    if i >=0:
        #key exist replace it
        bucket[i]= (key,value)
    else:
        #if key does not exist then create it
        bucket.append((key,value))
        
def delete(aMap, key):
    """delete the given key from map"""
    bucket = get_bucket(aMap,key)
    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key == k:
            del bucket[i]
            break
            
def list(aMap):
    """print out whats in the map"""
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print k,v
     

#!/usr/bin/env Python3

import pickle

if __name__ == '__main__':
    obj = ("test", (2,3))
    obj2 = "qwertygfgfgfg"
    f = open(r'file.txt', 'wb')
    pickle.dump(obj, f)
    pickle.dump(obj2, f)
    f.close()

    f = open(r'file.txt', 'rb')
    obj = pickle.load(f)
    obj2 = pickle.load(f)
    print(obj[0], obj2)
    f.close()

    obj3 = pickle.dumps("test", protocol=pickle.HIGHEST_PROTOCOL)
    print(obj3)
    print(pickle.loads(obj3))
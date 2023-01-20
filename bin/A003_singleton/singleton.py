#!/usr/bin/env python

class Singleton_01():
    """
    __new__で、クラススコープにインスタンスを保持。
    2回目以降のコール時には、すでに生成されたインスタンスを返す。

    インスタンス生成にて引数を取りたい場合は、
    2回目以降の取得時に、デフォルトコンストラクタを利用できるようにしたいが、
    可能か検証する。
    """    

    def __new__(cls, *args, **kargs):

        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton_01, cls).__new__(cls)
        
        return cls._instance

    def __init__(self, test: str = None):

        if hasattr(__class__, "_instance"):
            return
            
        self.test_value = test

class Singleton_02():

    __only_instance = None

    def __init__(self):
        raise NotImplementedError('Cannot Generate Instance By Constructor')

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__only_instance = super(Singleton_01, cls).__new__(cls, args, kargs)
        return cls.__only_instance

class Singleton_03():

    shared_state = {}

    def __init__(self):
        self.__dict__ = self.shared_state
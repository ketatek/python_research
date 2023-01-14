#!/usr/bin/env python

#-----------------------------------------
# 引数付きデコレーターを利用して、
# クラス内のフィールドに値を保持できるか調査
#-------------------------------------------

import functools
from typing import Callable, TypeVar
from argparse import FileType

_T = TypeVar("_T")

class DecoSample():

    def sample_deco(
        type: Callable[[str], _T] | FileType,
        help: str, 
        validator: Callable=None
    ):
        def _sample_deco(func):

            @functools.wraps(func)
            def _wrapper(*args, **keywords):
                
                print(__name__, "開始")

                result = func(*args, **keywords)

                print(__name__, "終了")

                return result

            return _wrapper

        return _sample_deco

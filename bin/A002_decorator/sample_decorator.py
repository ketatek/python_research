#!/usr/bin/env python

#-----------------------------------------
# 引数付きデコレーターを利用して、
# クラス内のフィールドに値を保持できるか調査
#-------------------------------------------

import functools
from typing import Callable, TypeVar
from argparse import FileType, ArgumentParser

_T = TypeVar("_T")

class DecoSample():

    parser = ArgumentParser()

    @classmethod
    def get_arg_name(name: str, is_option: bool) -> str:
        return name if is_option else f'--{name}'
    
    @classmethod
    def sample_deco(
        type: Callable[[str], _T] | FileType,
        help: str,
        is_option: bool=True 
    ):  

        def _sample_deco(func):

            # パラメタの追加
            DecoSample.parser.add_argument(
                DecoSample.get_arg_name(func.__name__), 
                type=type, 
                help=help
            )

            @functools.wraps(func)
            def _wrapper(*args, **keywords):
                
                print(__name__, "開始")

                result = func(*args, **keywords)

                print(__name__, "終了")

                return result

            return _wrapper

        return _sample_deco


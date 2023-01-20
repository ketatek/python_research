#!/usr/bin/env python

#-----------------------------------------
# 引数付きデコレーターを利用して、
# クラス内のフィールドに値を保持できるか調査
#-------------------------------------------

import functools
from typing import Callable, TypeVar, Union
from argparse import FileType, ArgumentParser, HelpFormatter
from abc import ABCMeta, abstractmethod

_T = TypeVar("_T")

class DecoSample(metaclass=ABCMeta):

    __arg_configs = []

    def __init__(
        self,
    ) -> None:
        """
        インスタンスの初期化
        """

        self.__argParser = self._setup_perser()

        
        self.__args = self.parse()

    def _setup_perser(self) -> ArgumentParser:
          return ArgumentParser()  

    def _parse(self) -> dict:
          return __class__.__argParser.parse_args()  

    @property
    def args(self) -> dict:
        return self.__args 

    @classmethod
    def get_arg_name(cls, name: str, is_option: bool) -> str:
        return name if not is_option else f'--{name}'
    
    @classmethod
    def sample_deco(
        cls,
        type: Union[Callable[[str], _T] , FileType] = ...,
        help: str = ...,
        is_optional: bool=False,
    ):
        """_summary_

        Args:
            type (Union[Callable[[str], _T] , FileType]): _description_
            help (str): _description_
            is_option (bool, optional): _description_. Defaults to False.
        """      

        def _sample_deco(func):
            
            # パラメタの追加
            DecoSample.parser.add_argument(
                DecoSample.get_arg_name(func.__name__, is_optional), 
                type=type, 
                help=help,
#                required=required
            )

            @functools.wraps(func)
            def _wrapper(*args, **keywords):
                
                print(__name__, "開始")

                result = func(*args, **keywords)

                print(__name__, "終了")

                return result

            return _wrapper

        return _sample_deco


#!/usr/bin/env python

#-----------------------------------------
# 引数付きデコレーターを利用して、
# クラス内のフィールドに値を保持できるか調査
#-------------------------------------------

import functools
from typing import Callable, TypeVar, Union
from argparse import FileType, ArgumentParser, HelpFormatter
from abc import ABCMeta, abstractmethod
from types import MappingProxyType

_T = TypeVar("_T")

class DecoSample(metaclass=ABCMeta):

    __arg_configs = []

    def __init__(
        self,
    ) -> None:
        """
        インスタンスの初期化
        """
        for arg_item in type(self).__arg_configs:
            
            # パラメタの追加
            self._parser.add_argument(
                arg_item["name"], 
                type=arg_item["type"], 
                help=arg_item["help"],
    #                required=required
            )

        # argument のパース実行
        self.__args = self._parse()

    def _setup_perser(self) -> ArgumentParser:
        return ArgumentParser()  

    def _parse(self) -> dict:
        return self._parser.parse_args()  

    @property
    def _parser(self) -> ArgumentParser:
        if not hasattr(self, "_DecoSample__argParser"):
           self.__argParser = self._setup_perser()

        return self.__argParser

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
            
            cls.__arg_configs.append(
                {
                    "name":DecoSample.get_arg_name(func.__name__, is_optional), 
                    "type":type, 
                    "help":help
                }
            )

            @functools.wraps(func)
            def _wrapper(*args, **keywords):
                
                print(__name__, "開始")

                result = func(*args, **keywords)

                print(__name__, "終了")

                return result

            return _wrapper

        return _sample_deco


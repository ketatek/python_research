#!/usr/bin/env python

#-----------------------------------------
# プロパティの定義と一緒に、
# 起動引数パラメタを定義するよう実装できないか調査
# パターンとしては、以下を検討中。
# 1. スーパークラスで起動パラメタ定義のデコレーターを実装。
#    アプリごとに、このクラスを継承した、サブクラスを定義
#    サブクラスで、スーパークラスのデコレーターを使用して、対象パラメタのプロパティを定義
# 2. 起動パラメタの定義ヘルパとして実装。
#    アプリごとに、ヘルパクラスを利用した、パラメタアクセッサクラスを定義。
#    パラメタアクセッサクラスで、ヘルパクラスのデコレーターを使用して、
#    対象パラメタのプロパティを定義
# なお、パラメタ名は定義したプロパティ明から取得することを前提とする。
#-------------------------------------------

from  sample_decorator import DecoSample
from argparse import ArgumentParser

class ArgsSample(DecoSample):

    @property
    @DecoSample.sample_deco(
        type=str
        , help='サンプルパラメタA'
    )
    def param_a(self) -> str:
        return self.args.param_a 

    # def _setup_perser(self) -> ArgumentParser:
    #     return ArgumentParser(
    #         prog="test_01_プログラム名"
    #     )

    def __init__(self) -> None:
        super(ArgsSample, self).__init__()



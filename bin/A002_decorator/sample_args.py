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

class ArgsSample(DecoSample):

    @property
    @DecoSample.sample_deco(
        type=str
        , help='サンプルパラメタA'
        , is_option=True
    )
    def param_a(self) -> str:
        return self.__params.param_a 

    def __init__(self) -> None:
        # パラメタをパース
        self.__params = super().parser.parse_args()


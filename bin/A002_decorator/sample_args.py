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
    )
    def param_a(self) -> str:
        return self.__params.param_a 

    def __init__(self) -> None:

        #---------------------------------------------
        # parse_args の 前での実行ヘルプの内容を編集可能か検証
        # 編集可能だった。
        # > ということはスーパークラス側で、ArgumentParser の
        # > インスタンス保持しても問題なさそう。
        #---------------------------------------------
        super().parser.prog = 'foo_bar_プログラム名'

        # パラメタをパース
        self.__params = super().parser.parse_args()


import libs.utils as utils

def main():
    # 子ディレクトリ配置のライブラリからのパス
    print(f'モジュール配置先ベースのmainモジュールパス取得 > {utils.get_root_path()}')

if __name__ == '__main__':
    main()

# SPAAL2 Template

SPAAL2でシミュレーションをしたい場合はこのテンプレートを使ってください。

# リポジトリ

- spaal2-core ([Keio-CSG/spaal2-core](https://github.com/Keio-CSG/spaal2-core))
  - シミュレータのコア部分。LiDARやSpooferの実装が含まれる。
- spaal2-template ([Keio-CSG/spaal2-template](https://github.com/Keio-CSG/spaal2-template))
  - シミュレータ利用のワークスペースを作るためのテンプレート。submodule経由でcoreをimportする。
- fastlyzer ([organic-nailer/fastlyzer](https://github.com/organic-nailer/fastlyzer))
  - シミュレーション実験の補助ライブラリ。複数パラメータを変えながら並列でシミュレーションを回すことができる。
- simple_pcd_viewer ([organic-nailer/simple_pcd_viewer](https://github.com/organic-nailer/simple_pcd_viewer))
  - 点群表示用のOpen3Dのラッパーライブラリ。

# Getting Started

## リポジトリを用意する場合

1. GitHubの画面で[Use This Template]を押して新しいリポジトリを作成
2. `git clone --recursive git@github.com:Keio-CSG/xxx.git`
3. `uv run main.py`

## 用意しない場合

1. `git clone --recursive git@github.com:Keio-CSG/spaal2-template.git`
2. `uv run main.py`

フォルダ名をつけたい場合は`git clone --recursive git@github.com:Keio-CSG/spaal2-template.git xxx`とするとxxxになるよ

## `--recursive`をつけずにCloneしちゃった場合

`git submodule update --init --recursive`と唱えれば必要なものを全部Cloneしてくれる

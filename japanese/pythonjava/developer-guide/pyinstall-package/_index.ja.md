---
title: PyInstallerを使用してPythonアプリケーションを簡単に配布する
linktitle: Pyinstallerを使用したパッケージ
type: docs
weight: 10
url: /ja/python-java/pyinstaller-python/
description: pyinstallerを使ってpythonコードをexeにパッケージ化する
---

## **PyInstallerは何に使われていますか？**
PyInstallerは、あなたが書いたPythonスクリプトを読み込みます。コードを分析して、スクリプトが実行するために必要な他のすべてのモジュールとライブラリを見つけ出します。それから、それらのファイルのコピー（アクティブなPythonインタープリターを含む！）を収集します。

## **なぜPyinstallerを使ってPythonをパッケージ化するのですか？**
PyInstallerは、さまざまなオペレーティングシステム用にPythonコードをスタンドアロンの実行可能アプリケーションにパッケージ化するために使用されます。Pythonスクリプトを取り、すべての必要な依存関係を含む単一の実行可能ファイルを生成し、Pythonがインストールされていないコンピューターで実行できるようにします。これにより、Pythonおよび必要なモジュールをシステムにインストールする必要がないため、Pythonアプリケーションを簡単に配布および展開できます。また、PyInstallerは、1つのファイルの実行可能ファイルも作成でき、これにより、ユーザーはアプリケーションをダウンロードする際に単一のファイルのみを必要とします。

## **PyInstallerをインストールする方法**
PyInstallerは通常のPythonパッケージとして利用可能です。リリースされたバージョンのソースアーカイブは[PyPi](https://pypi.org/project/pyinstaller/)から入手できますが、最新バージョンを[ピップ](https://pip.pypa.io/en/stable/)を使用して簡単にインストールすることができます。
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

既存のPyInstallerのインストールを最新バージョンにアップグレードするには、次を使用します:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
現在の開発バージョンをインストールするには、次を使用します:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **PyInstallerを使用してEXEを作成する方法**
詳細なパッケージング手順を説明するために、単一のPythonファイルを例として取り上げます。[aspose.cells](https://pypi.org/project/aspose-cells/)をインストールした後にPython 3.11.0を例に取り上げます。

1. [example.py](example.py)という名前のPythonサンプルファイルを作成します。
{{< highlight java >}}

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "aspose-cells-23.1.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcpkix-jdk15on-1.60.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "JavaClassBridge.jar"))

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, CellsHelper

print(CellsHelper.getVersion())
workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}
1. c:\appというフォルダを作成し、example.py（添付）をc:\appにコピーします。
1. コマンドプロンプトを開き、pyinstaller example.pyコマンドを実行します。
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. jarファイル（aspose-cells-xxx.jar、bcprov-jdk15on-160.jar、bcpkix-jdk15on-1.60.jar、JavaClassBridge.jar。これらはC:\Python311\Lib\site-packages\asposecells\libフォルダに存在します。）をc:\appにコピーします。
1. spec接尾辞のファイルを編集して、[example.spec](example.spec)のようにデータセクションを追加します。
![todo:image_alt_text](example.png)
1. コマンドプロンプトウィンドウでpyinstaller example.specを実行します。
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. ディレクトリをC:\app\dist\exampleに切り替えると、example.exeファイルが見つかります。

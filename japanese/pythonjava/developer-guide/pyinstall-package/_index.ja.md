---
title: PyInstaller を使用して Python アプリケーションを簡単に配布する
linktitle: Pyinstallerを使用したパッケージ化
type: docs
weight: 10
url: /ja/python-java/pyinstaller-python/
description: Python コードを pyinstaller 経由で exe にパッケージ化します。
---
##  **PyInstaller は何に使用されますか?**
PyInstaller は、ユーザーが作成した Python スクリプトを読み取ります。コードを分析して、スクリプトの実行に必要な他のすべてのモジュールとライブラリを検出します。次に、アクティブな Python インタープリタを含む、これらすべてのファイルのコピーを収集します。

##  **Python をパッケージ化するのに Pyinstaller を使用するのはなぜですか?**
PyInstaller は、Python コードをさまざまなオペレーティング システム用のスタンドアロン実行可能アプリケーションにパッケージ化するために使用されます。これは、Python スクリプトを受け取り、必要な依存関係をすべて含む単一の実行可能ファイルを生成します。このファイルは、Python がインストールされていないコンピューター上でも実行できます。これにより、ユーザーはアプリケーションを実行するために Python と必要なモジュールをシステムにインストールする必要がないため、Python アプリケーションの配布と展開が容易になります。さらに、PyInstaller を使用して、アプリケーションに必要な依存関係をすべて含む単一の実行可能ファイルを作成することもできます。これにより、ユーザーは 1 つのファイルをダウンロードするだけで済むため、アプリケーションの配布がさらに簡単になります。

##  **PyInstaller をインストールする方法**
PyInstaller は通常の Python パッケージとして入手できます。リリースされたバージョンのソース アーカイブは、次の場所から入手できます。[ピピ](https://pypi.org/project/pyinstaller/)ただし、次を使用して最新バージョンをインストールする方が簡単です。[ピップ](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

既存の PyInstaller インストールを最新バージョンにアップグレードするには、以下を使用します。
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
現在の開発バージョンをインストールするには、次を使用します。
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **PyInstaller を使用して EXE を作成するにはどうすればよいですか**
単一の Python ファイルを例として、パッケージ化手順を詳しく説明します。インストール後の Python 3.11.0 を例として取り上げます。[aspose.cells](https://pypi.org/project/aspose-cells/).

1. という名前の Python サンプル ファイルを作成します。[たとえば .py](example.py).
{{< highlight "java" >}}

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
1. c:\app としてフォルダーを作成し、example.py(添付) を c:\app にコピーします。
1. コマンド プロンプトを開き、pyinstaller example.py コマンドを実行します。
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. jars(aspose-cells-xxx.jar、bcprov-jdk15on-160.jar、bcpkix-jdk15on-1.60.jar、JavaClassBridge.jar をコピーします。これらは C:\Python311\Lib\site-packages\asposecells\lib フォルダーに存在します。 ) を c:\app にコピーします。
1.  spec サフィックスを含むファイルを編集して、次のようなデータ セクションを追加します。[例.仕様](example.spec).
![todo:image_alt_text](example.png)
1. コマンド プロンプト ウィンドウで pyinstaller example.spec を実行します。
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. ディレクトリを C:\app\dist\example に切り替えると、example.exe ファイルが見つかります。

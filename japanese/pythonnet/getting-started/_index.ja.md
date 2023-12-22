---
title: はじめる
linktitle: はじめる
type: docs
weight: 4
url: /ja/python-net/getting-started/
description: Aspose.Cells for Python via .NET をインストールし、Hello World アプリケーションを作成する方法を学びます。
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **システム要求**
 Aspose.Cells for Python via .NET はプラットフォームに依存しない API であり、どのプラットフォーム (Windows および Linux) でも使用できます。[Python](https://www.python.org/downloads/)がインストールされています。

##  **Python バージョン**
- Python 3.6以上

##  **インストール**
###  **Windows:**
Aspose.Cells for Python via .NET から簡単に使用できます。[ピピ](https://pypi.org/project/aspose-cells-python/)次のコマンドで。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
Aspose.Cells for Python via .NET から簡単に使用できます。[ピピ](https://pypi.org/project/aspose-cells-python/)次のコマンドで。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注:インストール前に次のコマンドを実行する必要があります。
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **マックOS：**
Aspose.Cells for Python via .NET から簡単に使用できます。[ピピ](https://pypi.org/project/aspose-cells-python/)次のコマンドで。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注: Python が Python3.7 である場合 (ここでは python3.7 を例にします)、aspose-cells-python をインストールした後、次のエラーが発生する可能性があります。
 '/usr/local/lib/libpython3.7m.dylib' (そのようなファイルはありません)、'/usr/lib/libpython3.7m.dylib' (そのようなファイルはありません) プロンプト。
このような状況では、次のコマンドを bash_profile に追加してください (まず libpython3.7m.dylib がどこにあるかを見つけて、/Library/Frameworks/Python.framework/Versions/3.7/lib を取得してください)
たとえばここ）
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- 注: SkiaSharp グラフィック ライブラリに依存しているため、次のエラーが発生した場合:
**System.DllNotFoundException: 共有ライブラリ 'libSkiaSharp' またはその依存関係の 1 つをロードできません。** SkiaSharp をインストールしてください。
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
インストール後、次のコマンドを実行してください
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

もちろん、もっと簡単にしたい場合は、ダウンロードすることもできます[libSkiaSharp.dylib](libSkiaSharp.dylib)その後**コピー**それを**/usr/local/lib**ディレクトリ。

##  **Aspose.Cells for Python via .NET を使用して Hello World アプリケーションを作成する方法**

- という名前のファイルを作成します**HelloWorldFile.py の作成**次のサンプルコードを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 次に、上記のコードを「CreatingHelloWorldFile.py」に保存し、「python CreationHelloWorldFile.py」@コマンド プロンプトを実行します。


---
title: はじめに
linktitle: はじめに
type: docs
weight: 4
url: /ja/python-net/getting-started/
description: Aspose.Cells for Python via .NET のインストール方法とHello Worldアプリケーションの作成方法を学びます。
keywords: Windows LinuxおよびMacOSでAspose.Cells for Python via .NET をインストールし、Aspose.Cells for Python via .NET のインストールガイドライン、Python Via .NET Hello Worldプログラムの手引きについて。 
---

## **システム要件**
Aspose.Cells for Python via .NET はプラットフォームに依存しないAPIで、[Python](https://www.python.org/downloads/)がインストールされているWindowsおよびLinuxなど、どのプラットフォームでも使用できます。 

## **Pythonのバージョン**
- Python 3.6 以上

## **インストール**
### **Windows:**
以下のコマンドを使用して、[pypi](https://pypi.org/project/aspose-cells-python/)からAspose.Cells for Python via .NET を簡単に使用できます。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
以下のコマンドを使用して、[pypi](https://pypi.org/project/aspose-cells-python/)からAspose.Cells for Python via .NET を簡単に使用できます。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：インストール前に以下のコマンドを実行する必要があります
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
以下のコマンドを使用して、[pypi](https://pypi.org/project/aspose-cells-python/)からAspose.Cells for Python via .NET を簡単に使用できます。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：PythonがPython3.7の場合（例として、ここではpython3.7を取る）、aspose-cells-pythonをインストールした後、以下のエラーが発生する場合があります
  '/usr/local/lib/libpython3.7m.dylib'（そのようなファイルはありません）、'/usr/lib/libpython3.7m.dylib'（そのようなファイルはありません）とプロンプトが表示されます。
  そのような状況では、次のコマンドをbash_profileに追加してください（まずlibpython3.7m.dylibがどこにあるかを見つけます。例として/Library/Frameworks/Python.framework/Versions/3.7/libを取ります）
  たとえばここ
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- 注意：SkiaSharpグラフィックスライブラリに頼っているため、次のエラーが発生する場合は
**System.DllNotFoundException: 'libSkiaSharp'またはその依存関係の共有ライブラリを読み込めません。** SkiaSharpをインストールしてください。
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
インストール後、次のコマンドを実行してください 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

もちろん、より簡単にしたい場合は、[libSkiaSharp.dylib](libSkiaSharp.dylib)をダウンロードして、**/usr/local/lib**ディレクトリに**コピー**することもできます。

## **Aspose.Cells for Python via .NET を使用してHello Worldアプリケーションを作成する方法**

- **CreatingHelloWorldFile.py**という名前のファイルを作成し、次のサンプルコードを使用します:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 上記のコードを"CreatingHelloWorldFile.py"に保存して、「python CreatingHelloWorldFile.py」をコマンドプロンプトで実行します。

## **Python via .NET 例 github**
- より多くのサンプルコードを表示するには、[Aspose.Cells for Python via .NET Example](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) githubをご覧ください。



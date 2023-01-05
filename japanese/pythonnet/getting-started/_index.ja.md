---
title: 入門
linktitle: 入門
type: docs
weight: 4
url: /ja/python-net/getting-started/ 
keywords: python, excel, instal
description: セットアップ Aspose.Cells for Python via .NET とインストールのガイドライン。
---
## **システム要求**
 Aspose.Cells for Python via .NET はプラットフォームに依存しない API であり、任意のプラットフォーム (Windows および Linux) で使用できます。[Python](https://www.python.org/downloads/)がインストールされています。

## **Python バージョン**
- Python 3.6以上

## **インストール**
### **Windows:**
Aspose.Cells for Python via .NET から簡単に使用できます[ピピ](https://pypi.org/project/aspose-cells-python/)次のコマンドで。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Aspose.Cells for Python via .NET から簡単に使用できます[ピピ](https://pypi.org/project/aspose-cells-python/)次のコマンドで。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **マックOS：**
Aspose.Cells for Python via .NET から簡単に使用できます[ピピ](https://pypi.org/project/aspose-cells-python/)次のコマンドで。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注: Python が Python3.7 の場合 (たとえば、ここでは python3.7 を使用します)、aspose-cells-python をインストールした後、次のエラーが発生する可能性があります。
 「/usr/local/lib/libpython3.7m.dylib」(そのようなファイルはありません)、「/usr/lib/libpython3.7m.dylib」(そのようなファイルはありません) プロンプト。
このような状況では、次のコマンドを bash_profile に追加してください (最初に libpython3.7m.dylib の場所を見つけ、/Library/Frameworks/Python.framework/Versions/3.7/lib を取得します)。
例えばここ）
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
## **Hello World アプリケーションの作成**

- という名前のファイルを作成します。**HelloWorldFile.py の作成**次のサンプル コードを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 上記のコードを「CreatingHelloWorldFile.py」に保存し、「python CreationHelloWorldFile.py」@コマンド プロンプトを実行します。


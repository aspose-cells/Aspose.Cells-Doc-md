---
title: DBNumのカスタムパターン書式を指定する
description: Aspose.Cellsは、カスタムフォーマットパターンを使用して日付と数値のフォーマットをサポートするスプレッドシートファイル操作用のPythonライブラリです。このこの記事では、 dbnum のカスタムフォーマットパターンを指定し、ユーザーが数値の表示方法をより制御できるようにする方法を紹介します。
keywords: Aspose.Cells、Pythonライブラリ、電子スプレッドシート、カスタムフォーマットパターン、フォーマット、「dbnum」、表示制御
type: docs
weight: 110
url: /ja/python-net/specifying-dbnum-custom-pattern-formatting/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETは、*DBNum* カスタムパターンフォーマットをサポートします。例えば、セルの値が123で、カスタムフォーマットを [DBNum2][$-804]General に設定すると、「壹佰贰拾叁」と表示されます。セルのカスタムフォーマットは [**Cell.get_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style/#) メソッドと [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) プロパティを使用して指定できます。

## **サンプルコード**

次のサンプルコードは*DBNum* カスタムパターンフォーマットの指定方法を示しています。詳細については、[出力PDF](43352081.pdf)をチェックしてください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SpecifyingDBNumCustomPatternFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}

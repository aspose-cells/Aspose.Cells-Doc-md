---
title: Aspose.Cellsを使用したテキストを列に変換する
type: docs
weight: 30
url: /ja/python-net/convert-text-to-columns-using-aspose-cells/
description: この記事では、Aspose.Cells for Python via .NET API を使用して、テキストを列に変換する方法について説明します。
keywords: Python Excel ライブラリ、Python でテキストを列に変換、Python でテキストを列に変換、Aspose.Cells for Python via .NET でテキストを列に変換、Convert Text to Columns using Microsoft Excel.
---

## **可能な使用シナリオ**

Microsoft Excel を使用してテキストを列に変換できます。この機能は、*データ* タブの*データ ツール* から利用できます。列の内容を複数の列に分割するには、データに特定の区切り記号（コンマなど）が含まれている必要があります。これにより、Microsoft Excel がセルの内容を複数のセルに分割します。Aspose.Cells for Python via .NET でも、この機能を [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) メソッドを介して提供しています。

## **Aspose.Cells for Python Excel ライブラリを使用して、テキストを列に変換する**

次のサンプルコードは、[**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/)メソッドの使用法を説明しています。このコードでは、まず第1ワークシートの列Aに人名を追加します。名前はスペース文字で区切られています。その後、列Aに[**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/)メソッドを適用し、出力エクセルファイルとして保存します。[出力エクセルファイル](25395213.xlsx)を開くと、名前が列Aに、姓が列Bに表示されます。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}

---
title: ExcelをJSONに変換
type: docs
weight: 300
url: /ja/python-net/convert-excel-to-json/
description: Aspose.Cells for Python via .NET APIを使用して、ExcelファイルをJSON形式に変換する方法を学びます。
keywords: PythonでExcelをJSONに変換する、PythonでExcelをJSONに変換するvia NET、ワークブックをJSONにエクスポートする、ExcelファイルをJSONに変換する。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ワークブックをJson（JavaScript Object Notation）ファイルに変換する機能をサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells for Python via .NET APIを使用してExcelワークブックをJSON形式に変換する方法について疑問に思う必要はありません。Aspose.Cells APIは、スプレッドシートをJSON形式に変換する機能を提供しています。ワークブックをJSONにエクスポートするには、第2パラメータとして[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)を渡します。また、[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions)メソッドの追加設定を指定するために[**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions)クラスを使用できます。

次のコード例は、ExcelワークブックをJSONにエクスポートする方法を示しています。参照用に、[ソースファイル](sample.xlsx)をJSONファイルに変換するためのコードが含まれています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New.py" >}}

以下のコード例は、JsonSaveOptionsクラスを使用して追加の設定を指定することで、ExcelワークブックをJsonにエクスポートする方法を示しています。参照のためにコードで生成されたJsonファイルの[source file](sample.xlsx)を変換するコードを参照してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New2.py" >}}


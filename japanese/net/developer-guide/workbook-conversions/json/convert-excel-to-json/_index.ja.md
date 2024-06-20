---
title: ExcelをJSONに変換
type: docs
weight: 300
url: /ja/net/convert-excel-to-json/
description: Aspose.CellsでExcelファイルをJSONに変換する方法を学ぶ。
keywords: Office 2013、Office 2016、Office 2019、およびOffice 365なしでブックをJSONにエクスポートする
---

{{% alert color="primary" %}}

Aspose.CellsはワークブックをJson(JavaScript Object Notation)ファイルに変換することをサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

ExcelワークブックをJSON形式に変換する方法を疑問に思う必要はありません。なぜなら、Apose.Cells for .NETライブラリには最良の決定があるからです。Aspose.Cells APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2パラメータに[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を渡します。[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)クラスを使用してワークシートをJSONにエクスポートするための追加設定を指定することもできます。

次のコード例は、ExcelワークブックをJSONにエクスポートする方法を示しています。参照用に、[ソースファイル](sample.xlsx)をJSONファイルに変換するためのコードが含まれています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

以下のコード例は、JsonSaveOptionsクラスを使用して追加の設定を指定することで、ExcelワークブックをJsonにエクスポートする方法を示しています。参照のためにコードで生成されたJsonファイルの[source file](sample.xlsx)を変換するコードを参照してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}


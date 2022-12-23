---
title: Convert-Excel-to-JSON
type: docs
weight: 300
url: /ja/net/convert-excel-to-json/
description: Aspose.Cells で Excel ファイルを json に変換する方法を学びます。
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells は、ワークブックを Json (JavaScript Object Notation) ファイルに変換することをサポートしています。

{{% /alert %}}

## **Excel ワークブックを JSON に変換**

Apose.Cells for .NET ライブラリには最適な決定があるため、Excel ワークブックを JSON に変換する方法を考える必要はありません。 Aspose.Cells API は、スプレッドシートを JSON 形式に変換するためのサポートを提供します。ワークブックを JSON にエクスポートするには、次を渡します。[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)の 2 番目のパラメータとして[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法。使用することもできます[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)クラスを使用して、ワークシートを JSON にエクスポートするための追加設定を指定します。

次のコード例は、Excel ワークブックを Json にエクスポートする方法を示しています。変換するコードを参照してください[ソースファイル](sample.xlsx)参照用のコードによって生成された Json ファイルに。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

 JsonSaveOptions クラスを使用して追加の設定を指定する次のコード例は、Excel ワークブックを Json にエクスポートする方法を示しています。変換するコードを参照してください[ソースファイル](sample.xlsx)参照用のコードによって生成された Json ファイルに。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}


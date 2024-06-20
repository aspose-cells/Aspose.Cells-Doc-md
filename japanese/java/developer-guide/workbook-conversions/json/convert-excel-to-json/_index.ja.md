---
title: ExcelをJSONに変換
type: docs
weight: 20
url: /ja/java/convert-excel-to-json/
description: Aspose.Cells for JavaのAPIを使用して、Excelファイルをjsonに変換する方法を学びます。
keywords: Javaでワークブックをjsonにエクスポートし、Javaを使用してExcelをJSONに変換し、JavaでExcelをJSONに保存し、Javaを使用してワークブックをJSONに変換し、JavaでワークブックをJSONに保存し、ExcelをJSONにエクスポートするvia Java。
---

{{% alert color="primary" %}}

Aspose.CellsはワークブックをJson(JavaScript Object Notation)ファイルに変換することをサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換する方法**

Aspose.Cells Javaライブラリが最適な決定を提供しているため、ExcelワークブックをJSONに変換する方法を悩む必要はありません。 Aspose.Cells Java APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int))メソッドの第2パラメーターとして[**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)を渡します。ワークシートをJSONにエクスポートするための追加の設定を指定するには、[**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions)クラスを使用できます。

以下のコード例は、ExcelワークブックをJsonにエクスポートすることを示しています。参照のためにコードで生成されたJsonファイルの[source file](sample.xlsx)を変換するコードを参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

以下のコード例は、JsonSaveOptionsクラスを使用して追加の設定を指定することで、ExcelワークブックをJsonにエクスポートする方法を示しています。参照のためにコードで生成されたJsonファイルの[source file](sample.xlsx)を変換するコードを参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}

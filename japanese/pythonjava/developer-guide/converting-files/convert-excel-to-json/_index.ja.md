---
title: ExcelをJSONに変換
type: docs
weight: 300
url: /ja/python-java/convert-excel-to-json/
description: Aspose.Cells for Python via Javaを使用して、ExcelファイルをJSON形式に変換する方法を学びます。
keywords: Office 2013、Office 2016、Office 2019、およびOffice 365なしでブックをJSONにエクスポートする
---

{{% alert color="primary" %}}

Aspose.Cells for Python via JavaはワークブックをJSON（JavaScript Object Notation）ファイルに変換する操作をサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells for Python via Javaライブラリには、ExcelワークブックをJSONに変換するための最適な決定があります。 Aspose.Cells for Python via Java APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\))メソッドの第2パラメータとして[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)を渡します。ワークシートをJSONにエクスポートする追加設定を指定するには、[**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions)クラスを使用することもできます。

以下のコード例は、ExcelワークブックをJsonにエクスポートすることを示しています。参照のためにコードで生成されたJsonファイルの[source file](sample.xlsx)を変換するコードを参照してください。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

以下のコード例は、JsonSaveOptionsクラスを使用して追加の設定を指定することで、ExcelワークブックをJsonにエクスポートする方法を示しています。参照のためにコードで生成されたJsonファイルの[source file](sample.xlsx)を変換するコードを参照してください。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}

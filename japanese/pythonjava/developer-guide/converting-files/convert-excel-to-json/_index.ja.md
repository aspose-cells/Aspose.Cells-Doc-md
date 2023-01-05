---
title: Convert-Excel-to-JSON
type: docs
weight: 300
url: /ja/python-java/convert-excel-to-json/
description: Aspose.Cells for Python via Java で Excel ファイルを json に変換する方法を学びます。
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells for Python via Java は、ワークブックの Json (JavaScript Object Notation) ファイルへの変換をサポートしています。

{{% /alert %}}

## **Excel ワークブックを JSON に変換**

Aspose.Cells for Python via Java ライブラリが最適な決定を行うため、Excel ワークブックを JSON に変換する方法を考える必要はありません。 Aspose.Cells for Python via Java API は、スプレッドシートを JSON 形式に変換するためのサポートを提供します。ワークブックを JSON にエクスポートするには、次を渡します。[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)の 2 番目のパラメータとして[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ） 方法。使用することもできます[**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions)クラスを使用して、ワークシートを JSON にエクスポートするための追加設定を指定します。

次のコード例は、Excel ワークブックを Json にエクスポートする方法を示しています。変換するコードを参照してください[ソースファイル](sample.xlsx)参照用のコードによって生成された Json ファイルに。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

 JsonSaveOptions クラスを使用して追加の設定を指定する次のコード例は、Excel ワークブックを Json にエクスポートする方法を示しています。変換するコードを参照してください[ソースファイル](sample.xlsx)参照用のコードによって生成された Json ファイルに。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}

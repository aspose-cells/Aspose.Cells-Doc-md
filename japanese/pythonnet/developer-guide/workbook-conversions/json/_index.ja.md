---
title: Json
type: docs
weight: 300
url: /ja/python-net/convert-workbook-to-json/
description: Aspose.Cells for Python via .NET APIを使用してExcelワークブックをJSON形式に変換する方法を学ぶ。
keywords: PythonでExcelワークブックをJSONに変換する、Python via NETでExcelワークブックをJSONに変換する、ワークブックをJSONにエクスポートする、ExcelワークブックをJSONに変換する。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ワークブックをJson（JavaScript Object Notation）ファイルに変換することをサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells for Python via .NET APIは、スプレッドシートをJSON形式に変換することをサポートしています。ワークブックをJSONにエクスポートするには、[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions)メソッドの第二パラメータとして[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)を渡します。ワークシートをJSONにエクスポートするための追加の設定を指定するためには、[**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions)クラスを使用することもできます。

次のコード例は、[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)列挙型メンバーを使用してアクティブなワークシートをJsonにエクスポートする方法を示しています。変換に関連するコードで、[ソースファイル](book1.xlsx)とコードによって生成された[出力Jsonファイル](book1.Json)を参照してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **高度なトピック**
- [CSVをJSONに変換](/cells/ja/python-net/convert-csv-to-json/)
- [ExcelをJSONに変換する](/cells/ja/python-net/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/python-net/convert-json-to-csv/)
- [JSONをExcelに変換する](/cells/ja/python-net/convert-json-to-excel/)
{{< app/cells/assistant language="python-net" >}}

---
title: Json
type: docs
weight: 300
url: /ja/net/convert-workbook-to-json/
---

{{% alert color="primary" %}}

Aspose.CellsはワークブックをJSON(JavaScript Object Notation)ファイルに変換する機能をサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells APIは、スプレッドシートをJSON形式に変換する機能を提供します。ワークブックをJSONにエクスポートするには、[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2パラメータとして渡します。また、ワークシートをJSONにエクスポートするための追加設定を指定するために[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)クラスを使用することもできます。

次のコード例は、[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型メンバーを使用してアクティブなワークシートをJsonにエクスポートする方法を示しています。変換に関連するコードで、[ソースファイル](book1.xlsx)とコードによって生成された[出力Jsonファイル](book1.Json)を参照してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **高度なトピック**
- [CSVをJSONに変換](/cells/ja/net/convert-csv-to-json/)
- [ExcelをJSONに変換する](/cells/ja/net/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/net/convert-json-to-csv/)
- [JSONをExcelに変換する](/cells/ja/net/convert-json-to-excel/)
{{< app/cells/assistant language="csharp" >}}

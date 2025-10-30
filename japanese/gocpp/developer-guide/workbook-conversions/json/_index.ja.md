---
title: GolangとC++を使ってWorkbookをJSONに変換
linktitle: ワークブックをJSONに変換
type: docs
weight: 300
url: /ja/go-cpp/convert-workbook-to-json/
description: Aspose.Cells for C++を使用してExcelワークブックをJSON形式に変換する方法を学びましょう。
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークブックをJSON（JavaScript Object Notation）ファイルに変換することをサポートします。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2パラメータとして[**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/)を渡してください。さらに、[**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)クラスを使用してワークシートをJSONにエクスポートする追加設定を指定することも可能です。

次のコード例は、[**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙子を使用してアクティブなワークシートをJSONにエクスポートする方法を示しています。ソースファイル（book1.xlsx）からコードが生成した出力JSONファイル（book1.json）への変換例も参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **上級トピック**
- [CSVをJSONに変換](/cells/ja/cpp/convert-csv-to-json/)
- [ExcelをJSONに変換](/cells/ja/cpp/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/cpp/convert-json-to-csv/)
- [JSONをExcelに変換](/cells/ja/cpp/convert-json-to-excel/)

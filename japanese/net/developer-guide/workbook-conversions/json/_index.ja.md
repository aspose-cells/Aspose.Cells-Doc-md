---
title: ジェイソン
type: docs
weight: 300
url: /ja/net/convert-workbook-to-json/
---
{{% alert color="primary" %}}

Aspose.Cells は、ワークブックを Json (JavaScript Object Notation) ファイルに変換することをサポートしています。

{{% /alert %}}

## **Excel ワークブックを JSON に変換**

Aspose.Cells API は、スプレッドシートを JSON 形式に変換するためのサポートを提供します。ワークブックを JSON にエクスポートするには、次を渡します。[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)の 2 番目のパラメータとして[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法。使用することもできます[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)クラスを使用して、ワークシートを JSON にエクスポートするための追加設定を指定します。

次のコード例は、アクティブなワークシートを Json にエクスポートする方法を示しています。[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙メンバー。変換するコードを参照してください[ソースファイル](book1.xlsx)に[出力Jsonファイル](book1.Json)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **先行トピック**
- [CSV を JSON に変換](/cells/ja/net/convert-csv-to-json/)
- [Convert-Excel-to-JSON](/cells/ja/net/convert-excel-to-json/)
- [JSON を CSV に変換](/cells/ja/net/convert-json-to-csv/)
- [Convert-JSON-to-Excel](/cells/ja/net/convert-json-to-excel/)

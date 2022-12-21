---
title: Aspose.Cells を使用してテキストを列に変換します
type: docs
weight: 30
url: /ja/net/convert-text-to-columns-using-aspose-cells/
---
## **考えられる使用シナリオ**

Microsoft Excel を使用して、テキストを列に変換できます。この機能は、*データツール*下*データ*タブ。列の内容を複数の列に分割するには、Microsoft Excel がセルの内容を複数のセルに分割するためのコンマ (またはその他の文字) などの特定の区切り文字をデータに含める必要があります。 Aspose.Cells もこの機能を提供しています[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法。

## **Aspose.Cells を使用してテキストを列に変換します**

次のサンプル コードは、[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法。このコードは、最初のワークシートの列 A に人の名前を最初に追加します。姓と名はスペース文字で区切られています。それなら当てはまる[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)メソッドを列 A に追加し、出力 Excel ファイルとして保存します。開くと[出力エクセルファイル](25395213.xlsx)、このスクリーンショットに示すように、名は列 A にあり、姓は列 B にあることがわかります。

![todo:画像_代替_文章](convert-text-to-columns-using-aspose-cells_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}

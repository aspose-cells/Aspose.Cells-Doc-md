---
title: Aspose.Cellsを使用したテキストを列に変換する
type: docs
weight: 30
url: /ja/net/convert-text-to-columns-using-aspose-cells/
---

## **可能な使用シナリオ**

Microsoft Excelを使用して、テキストを列に変換することができます。この機能は、*Data*タブの*Data Tools*から利用できます。列の内容を複数の列に分割するには、Microsoft Excelがセルの内容を複数のセルに分割する基準となる、コンマ（または他の文字）などの特定の区切り文字を含むデータが必要です。Aspose.Cellsもこの機能を提供します。[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)メソッドを介して。

## **Aspose.Cellsを使用したテキストを列に変換する**

次のサンプルコードは、[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)メソッドの使用法を説明しています。このコードでは、まず第1ワークシートの列Aに人名を追加します。名前はスペース文字で区切られています。その後、列Aに[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)メソッドを適用し、出力エクセルファイルとして保存します。[出力エクセルファイル](25395213.xlsx)を開くと、名前が列Aに、姓が列Bに表示されます。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}

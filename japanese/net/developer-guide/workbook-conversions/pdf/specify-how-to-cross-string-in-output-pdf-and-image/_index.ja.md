---
title: 出力PDFおよびイメージで文字列をクロスする方法を指定します。
type: docs
weight: 120
url: /ja/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **可能な使用シナリオ**

セルにテキストが含まれているが、セルの幅を超える場合、次の列の次のセルがnullまたは空の場合、文字列がオーバーフローします。 ExcelファイルをPDF /イメージに保存する際、このオーバーフローを制御することができます。これは[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)列挙型を使用して、クロスタイプを指定することで可能です。以下の値が含まれます

- **TextCrossType.Default**: 次のセルに依存するようにMS Excelのようにテキストを表示します。次のセルがnullの場合、文字列が交差するか、切り捨てられます。

- **TextCrossType.CrossKeep**: MS ExcelでPDF /イメージをエクスポートしたように文字列を表示します。

- **TextCrossType.CrossOverride**: すべてのテキストを表示して、他のセルを交差して上書きします

- **TextCrossType.StrictInCell**: セルの幅内で文字列のみを表示します。

## **TextCrossTypeを使用して出力PDF/イメージで文字列をクロスする方法を指定します。**

以下のサンプルコードは、さまざまな[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)を指定してサンプルExcelファイルをロードし、PDF/イメージ形式で保存するものです。 サンプルExcelファイルと出力ファイルは、以下のリンクからダウンロードできます。

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

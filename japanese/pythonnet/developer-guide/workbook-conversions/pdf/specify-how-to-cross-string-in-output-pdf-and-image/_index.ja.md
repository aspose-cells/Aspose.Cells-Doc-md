---
title: 出力PDFおよびイメージで文字列をクロスする方法を指定します。
type: docs
weight: 120
url: /ja/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aspose.Cells for Python via .NET APIを使用して、出力PDFおよび画像で文字列交差の方法を学びます。
keywords: Pythonでの出力PDFおよび画像での文字列交差
---

## **可能な使用シナリオ**

セルにテキストが含まれているが、セルの幅を超える場合、次の列の次のセルがnullまたは空の場合、文字列がオーバーフローします。 ExcelファイルをPDF /イメージに保存する際、このオーバーフローを制御することができます。これは[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)列挙型を使用して、クロスタイプを指定することで可能です。以下の値が含まれます

- **TextCrossType.DEFAULT**: 次のセルに依存するMS Excelのようにテキストを表示します。次のセルが空の場合、文字列は交差しますか、切り捨てられます。

- **TextCrossType.CROSS_KEEP**: MS Excelと同じように文字列を表示します。

- **TextCrossType.CROSS_OVERRIDE**: 他のセルを交差させてすべてのテキストを表示し、交差したセルのテキストをオーバーライドします。

- **TextCrossType.STRICT_IN_CELL**: セルの幅内で文字列のみを表示します。

## **TextCrossTypeを使用して出力PDF/イメージで文字列をクロスする方法を指定します。**

以下のサンプルコードは、さまざまな[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)を指定してサンプルExcelファイルをロードし、PDF/イメージ形式で保存するものです。 サンプルExcelファイルと出力ファイルは、以下のリンクからダウンロードできます。

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### サンプルコード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

---
title: 出力PDFおよびイメージで文字列をクロスする方法を指定します。
type: docs
weight: 110
url: /ja/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれていますが、セルの幅を超える場合、次の列のセルがnullまたは空の場合、文字列がオーバーフローします。 ExcelファイルをPDF /イメージに保存すると、[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)列挙型を使用してこのオーバーフローを制御できます。 以下の値があります

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT)：MS Excelのように表示され、次のセルに依存します。 次のセルがnullの場合、文字列はクロスされるか、切り捨てられます。

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP)：MS ExcelにエクスポートされたPDF/イメージのように文字列を表示します

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE)：他のセルをCrossしてテキストを上書きしてすべてのテキストを表示します。

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL)：セルの幅内で文字列のみを表示します。

## **TextCrossTypeを使用して出力PDF/イメージで文字列をクロスする方法を指定します。**

以下のサンプルコードは、さまざまな[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)を指定してサンプルExcelファイルをロードし、PDF/イメージ形式で保存するものです。 サンプルExcelファイルと出力ファイルは、以下のリンクからダウンロードできます。

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: 出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定
type: docs
weight: 140
url: /ja/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能な使用シナリオ**

セルにはテキストまたは文字列が含まれていますが、セルの幅よりも大きい場合、次の列の次のセルがヌルまたは空の場合に文字列がオーバーフローします。 ExcelファイルをHTMLに保存すると、[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)列挙型を使用してこのオーバーフローを制御できます。次の値があります。

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): MS Excelのように表示しますが、次のセルに依存します。次のセルがnullの場合、文字列はクロスされるか、切り捨てられます。

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): MS ExcelのHTMLエクスポートのように文字列を表示します。

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): HTMLクロス文字列を表示し、大きなHTMLファイルの作成のパフォーマンスは[**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT)または[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL)の値を設定するよりも10倍速くなります。

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): HTMLクロス文字列を表示し、テキストが重なる場合は右側の文字列を非表示にします。

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): セルの幅内で文字列のみを表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

次のサンプルコードは、異なる[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)を指定して[sample Excel file](51740747.xlsx)をロードし、HTML形式で保存します。このコードで生成された[出力HTMLファイル](51740745.zip)をダウンロードしてください。サンプルExcelファイルにはこのスクリーンショットに示されているように赤色で枠線を引いた画像が含まれています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}

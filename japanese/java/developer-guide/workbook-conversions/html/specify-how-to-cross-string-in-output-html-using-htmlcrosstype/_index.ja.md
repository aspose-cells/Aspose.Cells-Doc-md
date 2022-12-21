---
title: HtmlCrossType を使用して、出力 HTML で文字列をクロスする方法を指定します
type: docs
weight: 140
url: /ja/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **考えられる使用シナリオ**

セルにテキストまたは文字列が含まれているが、セルの幅よりも大きい場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを HTML に保存する場合、[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)列挙。次の値があります。

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): 次のセルに依存する MS Excel のように表示します。次のセルが null の場合、文字列が交差するか、切り捨てられます。

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): HTML をエクスポートする MS Excel のような文字列を表示します。

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : HTML クロス文字列を表示します。大きな HTML ファイルを作成する場合のパフォーマンスは、値を に設定するよりも 10 倍以上速くなります。[**デフォルト**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT)また[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)：HTMLクロス文字列を表示し、テキストが重なると右文字列を非表示にします。

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): セルの幅内の文字列のみを表示します。

## **HtmlCrossType を使用して、出力 HTML で文字列をクロスする方法を指定します**

次のサンプル コードは、[サンプル Excel ファイル](51740747.xlsx)を指定して HTML 形式で保存します。[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType).をダウンロードしてください[出力HTML](51740745.zip)このコードで生成されたファイル。サンプルの Excel ファイルには、このスクリーンショットに示すように、赤い色で囲まれた画像が含まれています。[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)出力 HTML の値。

![todo:画像_代替_文章](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}

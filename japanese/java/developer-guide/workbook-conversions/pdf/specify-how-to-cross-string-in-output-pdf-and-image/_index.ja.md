---
title: 出力 PDF と画像での文字列の交差方法を指定する
type: docs
weight: 110
url: /ja/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **考えられる使用シナリオ**

セルにテキストまたは文字列が含まれているが、セルの幅よりも大きい場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを PDF/Image に保存する場合、クロスタイプを指定してこのオーバーフローを制御できます[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)列挙。次の値があります。

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): MS Excel のような表示で、次のセルに依存します。次のセルが null の場合、文字列が交差するか、切り捨てられます。

- [**TextCrossType。 CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): PDF/画像をエクスポートするMS Excelのような文字列を表示します

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): 他のセルと交差してすべてのテキストを表示し、交差したセルのテキストを上書きします

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): セルの幅内の文字列のみを表示します。

## **TextCrossType を使用して、出力 PDF/画像で文字列を交差させる方法を指定します**

次のサンプル コードは、サンプルの Excel ファイルを読み込み、別のファイルを指定して PDF/Image 形式で保存します。[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType).サンプルの Excel ファイルと出力ファイルは、次のリンクからダウンロードできます。

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}

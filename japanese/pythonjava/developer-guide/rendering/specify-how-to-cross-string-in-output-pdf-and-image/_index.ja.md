---
title: 出力PDFと画像の文字列の交差方法を指定
type: docs
weight: 20
url: /ja/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **出力PDFと画像の文字列の交差方法を指定**
セルにセルの幅より大きいテキストまたは文字列が含まれている場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを PDF/Image に保存すると、[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType)列挙。次の値があります。

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): MS Excel のような表示で、次のセルに依存します。次のセルが null の場合、文字列が交差するか、切り捨てられます。
- [TextCrossType。 CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): PDF/Image をエクスポートする MS Excel のような文字列を表示します
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)他のセルと交差してすべてのテキストを表示し、交差したセルのテキストを上書きします
- [TextCrossType.STRICT_の_細胞](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): セルの幅内の文字列のみを表示します。

次のサンプル コードは、サンプル Excel ファイルを読み込み、別の TextCrossType を指定して PDF/Image 形式で保存します。サンプルの Excel ファイルと出力ファイルは、次のリンクからダウンロードできます。

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}

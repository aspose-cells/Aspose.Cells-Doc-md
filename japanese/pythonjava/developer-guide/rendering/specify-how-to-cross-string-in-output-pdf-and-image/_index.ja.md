---
title: 出力 PDF と画像での文字列の交差方法を指定する
type: docs
weight: 20
url: /ja/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **出力 PDF と画像での文字列の交差方法を指定する**
セルにセルの幅より大きいテキストまたは文字列が含まれている場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを PDF/Image に保存する場合、クロスタイプを指定してこのオーバーフローを制御できます[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType)列挙。次の値があります。

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): MS Excel のような表示で、次のセルに依存します。次のセルが null の場合、文字列が交差するか、切り捨てられます。
- [TextCrossType。 CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): PDF/画像をエクスポートする MS Excel と同様の文字列を表示します
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)他のセルと交差してすべてのテキストを表示し、交差したセルのテキストを上書きします
- [TextCrossType.STRICT_の_細胞](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): セルの幅内の文字列のみを表示します。

次のサンプル コードは、サンプルの Excel ファイルを読み込み、別の TextCrossType を指定して PDF/Image 形式で保存します。サンプルの Excel ファイルと出力ファイルは、次のリンクからダウンロードできます。

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}

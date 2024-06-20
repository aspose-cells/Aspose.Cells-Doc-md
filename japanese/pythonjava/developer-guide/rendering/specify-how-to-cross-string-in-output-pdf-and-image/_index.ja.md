---
title: 出力PDFおよびイメージで文字列をクロスする方法を指定します。
type: docs
weight: 20
url: /ja/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **出力PDFおよび画像内の文字列の交差方法を指定**
セルに文字列がセルの幅よりも大きい場合、次の列のセルがnullまたは空である場合、文字列がオーバーフローします。ExcelファイルをPDF/Imageに保存するときには、[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) 列挙型を使用してこのオーバーフローを制御できます。

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT)：MS Excelの表示に従い、次のセルに依存します。次のセルがnullの場合、文字列がクロスされるか切り取られます。
- [TextCrossType.CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP)：MS Excelのエクスポートと類似した方法で文字列を表示
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)：他のセルをクロスして文字列をオーバーライドしてすべてのテキストを表示
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL)：セルの幅内で文字列を表示

次のサンプルコードは、サンプルExcelファイルをロードし、異なるTextCrossTypeを指定してPDF/Image形式で保存します。サンプルExcelファイルと出力ファイルは、以下のリンクからダウンロードできます。

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}

---
title: 出力PDFと画像の文字列を交差させる方法を指定します
type: docs
weight: 120
url: /ja/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: 出力 PDF と画像の文字列を Aspose.Cells for Python via .NET API と交差させる方法を学びます。
keywords: Python Cross String in output PDF and image
---
##  **考えられる使用シナリオ**

セルにテキストまたは文字列が含まれているが、それがセルの幅より大きい場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを PDF/Image に保存するときに、[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)列挙。次の値があります

- *TextCrossType.DEFAULT**: 次のセルに依存する MS Excel のようなテキストを表示します。次のセルが null の場合、文字列は交差するか切り詰められます。

- *TextCrossType.CROSS_KEEP**: PDF/Image をエクスポートする MS Excel のような文字列を表示します

- *TextCrossType.CROSS_OVERRIDE**: 他のセルを交差させてすべてのテキストを表示し、交差したセルのテキストを上書きします。

- *TextCrossType.STRICT_IN_CELL**: セルの幅内の文字列のみを表示します。

##  **TextCrossType を使用して、出力 PDF/Image の文字列を交差する方法を指定します**

次のサンプル コードでは、サンプル Excel ファイルを読み込み、別の形式を指定して PDF/Image 形式で保存します。[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)。サンプル Excel ファイルと出力ファイルは、次のリンクからダウンロードできます。

[サンプルクロスタイプ.xlsx](81920905.xlsx)

[出力クロスタイプ.pdf](81920903.pdf)

[出力クロスタイプ.png](81920904.png)

### サンプルコード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}

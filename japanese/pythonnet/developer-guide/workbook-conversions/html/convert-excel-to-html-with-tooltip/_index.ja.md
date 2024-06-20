---
title: ツールチップ付きでExcelをHTMLに変換する
type: docs
weight: 200
url: /ja/python-net/convert-excel-to-html-with-tooltip/
description: Aspose.Cells for Python via NETを使用して、ツールチップ付きでExcelをHTMLに変換する方法を示しています。
keywords: Pythonツールチップ付きでExcelをHTMLに変換、Python via NET Excelツールチップ付きHTMLに変換、Pythonワークブックをツールチップ付きHTMLに変換。
---

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り捨てられる場合があるかもしれません。ホバーイベントで完全なテキストをツールチップとして表示したい場合。Aspose.Cells はこれをサポートしており、[**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) プロパティを提供しています。[**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) プロパティをtrueに設定すると、生成されたHTMLに完全なテキストがツールチップとして追加されます。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[ソースのExcelファイル](98107416.xlsx)を読み込んで、ツールチップを含む[出力のHTMLファイル](98107417.zip)を生成します。

サンプルコード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}

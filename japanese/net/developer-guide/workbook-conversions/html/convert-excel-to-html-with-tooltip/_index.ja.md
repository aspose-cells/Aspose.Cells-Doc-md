---
title: ツールチップ付きでExcelをHTMLに変換する
type: docs
weight: 200
url: /ja/net/convert-excel-to-html-with-tooltip/
---

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り捨てられる場合があるかもしれません。ホバーイベントで完全なテキストをツールチップとして表示したい場合。Aspose.Cells はこれをサポートしており、[**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) プロパティを提供しています。[**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) プロパティをtrueに設定すると、生成されたHTMLに完全なテキストがツールチップとして追加されます。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[ソースのExcelファイル](98107416.xlsx)を読み込んで、ツールチップを含む[出力のHTMLファイル](98107417.zip)を生成します。

サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

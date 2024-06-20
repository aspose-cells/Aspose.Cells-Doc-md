---
title: ツールチップ付きでExcelをHTMLに変換する
type: docs
weight: 150
url: /ja/java/convert-excel-to-html-with-tooltip/
---

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り取られる場合があり、ホバーイベントで完全なテキストをツールチップとして表示したい場合があります。Aspose.Cellsは、この機能をサポートし、[**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)プロパティを提供しています。 [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)プロパティを**true**に設定すると、生成されたHTMLに完全なテキストがツールチップとして追加されます。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[ソースExcelファイル](AddTooltipToHtmlSample.xlsx)をロードし、ツールチップを追加した[出力HTMLファイル](AddTooltipToHtmlSample_out.zip)を生成します。

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}

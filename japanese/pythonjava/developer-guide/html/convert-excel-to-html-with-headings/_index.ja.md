---
title: 見出しを含めてExcelをHTMLに変換する
type: docs
weight: 10
url: /ja/python-java/convert-excel-to-html-with-headings/
---

## **見出しを使用したExcelからHTMLへの変換**
Excel ファイルを HTML に変換する際、Aspose.Cells は列と行の見出しをエクスポートするオプションを提供しています。API が提供する [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) プロパティを使用することで、これを実現できます。[HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) のデフォルト値は **False** です。出力の HTML ファイルで見出しをレンダリングするには、パラメータとして **True** を渡します。以下の画像は、このコードによって生成された出力ファイルを示しています。

![todo:image_alt_text](PrintHeadings.jpg)

以下のサンプルコードは、[HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) プロパティを使用して、出力の HTML ファイルで見出しをレンダリングする方法を示しています。
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

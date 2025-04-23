---
title: HTMLに印刷エリア範囲をエクスポートする
type: docs
weight: 60
url: /ja/net/export-print-area-range-to/
---

## **可能な使用シナリオ**

PDFレンダリングにはすでに利用可能な機能ですが、HTMLにも適用可能な、ワークシートの選択範囲である印刷範囲のみをエクスポートする場合があります。ワークシートのページ設定オブジェクトに印刷範囲を設定し、後で[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly)フラグを使用して選択範囲のみをエクスポートしてください。

## サンプルコード

次のサンプルコードはワークブックをロードし、プリントエリアをHTMLにエクスポートします。この機能のテスト用にサンプルファイルを以下のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

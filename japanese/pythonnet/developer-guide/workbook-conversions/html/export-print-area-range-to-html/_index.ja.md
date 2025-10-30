---
title: HTMLに印刷エリア範囲をエクスポートする
type: docs
weight: 60
url: /ja/python-net/export-print-area-range-to/
---

## **可能な使用シナリオ**

PDFレンダリングにはすでに利用可能な機能ですが、HTMLにも適用可能な、ワークシートの選択範囲である印刷範囲のみをエクスポートする場合があります。ワークシートのページ設定オブジェクトに印刷範囲を設定し、後で[**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only)フラグを使用して選択範囲のみをエクスポートしてください。

## サンプルコード

次のサンプルコードはワークブックをロードし、プリントエリアをHTMLにエクスポートします。この機能のテスト用にサンプルファイルを以下のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

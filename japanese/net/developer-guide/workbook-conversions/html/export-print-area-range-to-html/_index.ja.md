---
title: 印刷範囲の範囲を HTML にエクスポート
type: docs
weight: 60
url: /ja/net/export-print-area-range-to/
---
## **考えられる使用シナリオ**

これは、シート全体ではなく、印刷領域、つまり選択した範囲のセルのみを HTML にエクスポートする必要がある一般的なシナリオです。この機能は既に PDF レンダリングで利用できますが、HTML でもこのタスクを実行できるようになりました。まず、ワークシートのページ設定オブジェクトで印刷範囲を設定します。後で、使用します[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly)選択した範囲のみをエクスポートするフラグ。

## サンプルコード

次のサンプル コードは、ワークブックを読み込み、印刷領域を HTML にエクスポートします。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}

---
title: 印刷範囲の範囲を HTML にエクスポート
type: docs
weight: 60
url: /ja/java/export-print-area-range-to-html/
---
## 考えられる使用シナリオ

これは、HTML にシート全体ではなく、印刷領域、つまり選択した範囲のセルのみをエクスポートする必要がある非常に一般的なシナリオです。この機能は、PDF レンダリングで既に利用可能ですが、HTML に対してもこのタスクを実行できるようになりました。まず、ワークシートのページ設定オブジェクトで印刷範囲を設定します。後で使用する[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)選択した範囲のみをエクスポートするプロパティ。

## Java 印刷領域範囲を HTML にエクスポートするコード

次のサンプル コードは、ワークブックを読み込み、印刷領域を HTML にエクスポートします。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}


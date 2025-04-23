---
title: HTMLに印刷エリア範囲をエクスポートする
type: docs
weight: 60
url: /ja/java/export-print-area-range-to-html/
---

## 可能な使用シナリオ

選択したセル範囲（印刷エリア）のみをHTMLにエクスポートする必要があるというのは非常に一般的なシナリオです。この機能はすでにPDFの出力に対して利用可能ですが、HTMLの場合も実行できます。まず、ワークシートのページ設定オブジェクトで印刷エリアを設定します。後で、[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)プロパティを使用して選択した範囲のみをエクスポートしてください。

## HTMLに印刷エリア範囲をエクスポートするためのJavaコード

次のサンプルコードはワークブックを読み込み、印刷エリアをHTMLにエクスポートします。この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

{{< app/cells/assistant language="java" >}}

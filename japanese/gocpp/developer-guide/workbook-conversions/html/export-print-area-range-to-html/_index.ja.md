---
title: GolangをC++経由で印刷範囲をHTMLにエクスポート
linktitle: 印刷範囲をHTMLにエクスポートする
type: docs
weight: 60
url: /ja/go-cpp/export-print-area-range-to/
description: Aspose.Cells for C++を使用して印刷範囲をHTMLにエクスポートする方法を学びます。
---

## **可能な使用シナリオ**

これは、シート全体の代わりに印刷範囲（選択したセル範囲）のみをHTMLにエクスポートする必要がある一般的なシナリオです。この機能はすでにPDFレンダリングに対応していますが、今度はHTMLに対してもこの作業を行うことができます。まず、ワークシートのページ設定オブジェクトで印刷範囲を設定します。次に、[**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/)フラグを使用して選択された範囲のみをエクスポートします。

## **サンプルコード**

以下のサンプルコードは、ワークブックを読み込み、その後印刷範囲をHTMLにエクスポートします。この機能をテストするためのサンプルファイルは次のリンクからダウンロードできます：

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}

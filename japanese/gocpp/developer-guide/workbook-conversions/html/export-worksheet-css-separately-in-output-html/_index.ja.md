---
title: GolangをC++経由で出力HTMLにワークシートCSSを別途エクスポート
linktitle: 出力HTMLでワークシートのCSSを別々にエクスポートする
type: docs
weight: 80
url: /ja/go-cpp/export-worksheet-css-separately-in-output/
description: Aspose.Cells for C++を使用して、ExcelファイルをHTMLに変換する際にワークシートのCSSを個別にエクスポートする方法を学びます。
---

## **可能な使用シナリオ**

Aspose.Cellsは、ExcelファイルをHTMLに変換する際にワークシートのCSSを個別にエクスポートする機能を提供しています。この目的のために[**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/)プロパティを使用し、HTML形式で保存する際に**true**に設定してください。

## **出力HTMLでワークシートのCSSを別々にエクスポートする**

次のサンプルコードは、Excelファイルを作成し、セル**B5**に**Red**のテキストを追加し、[**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/)プロパティを使用してHTML形式で保存します。コードによって生成された[output HTML](60489766.zip)には、**stylesheet.css**が含まれています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **単一シートのワークブックをHTMLにエクスポート**

Aspose.Cellsを使用して複数シートを持つワークブックをHTMLに変換すると、CSSを含むフォルダと複数のHTMLファイルが作成されます。ブラウザでこのHTMLファイルを開くとタブが表示されます。同じ動作は、単一シートのワークブックをHTMLに変換する場合でも必要です。以前は、単一シートのワークブックには別のフォルダは作成されず、HTMLファイルのみが作成されていました。このHTMLファイルをブラウザで開くとタブは表示されません。Microsoft Excelも適切なフォルダとHTMLを作成しますので、Aspose.CellsのAPIを使用して同じ動作を実現しています。以下のリンクからサンプルファイルをダウンロードし、下記のサンプルコードで使用できます：

[sampleSingleSheet.xlsx](79527937.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}

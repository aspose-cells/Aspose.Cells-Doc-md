---
title: 出力HTMLでワークシートのCSSを別々にエクスポートする
type: docs
weight: 80
url: /ja/java/export-worksheet-css-separately-in-output-html/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、ExcelファイルをHTMLに変換する際にワークシートのCSSを別々にエクスポートする機能を提供しています。この目的で、[HtmlSaveOptions.ExportWorksheetCSSSeparately](true)プロパティを使用してください。

## **出力HTMLでワークシートのCSSを別々にエクスポートする**

次のサンプルコードは、Excelファイルを作成し、セルB5に赤色のテキストを追加し、[HtmlSaveOptions.ExportWorksheetCSSSeparately](true)プロパティを使用してHTML形式で保存します。参照用のコードで生成された[output HTML](60489780.zip)には結果としてstylesheet.cssが含まれています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **単一のシートのワークブックをHTMLにエクスポートする**

Aspose.Cellsを使用して複数のシートを持つワークブックをHTMLに変換すると、HTMLファイルとCSSおよび複数のHTMLファイルを含むフォルダが作成されます。このHTMLファイルをブラウザで開くと、タブが表示されます。ワークブックが1つのワークシートでHTMLに変換された場合も同様の動作が必要です。以前は、1枚のシートのワークブックには別個のフォルダが作成されず、HTMLファイルのみが作成されていました。このようなHTMLファイルは、ブラウザで開かれるとタブが表示されませんでした。Excelは1つのシートに適切なフォルダとHTMLを作成し、そのためAspose.Cellsを使用して同じ動作を実装します。サンプルファイルは以下のリンクからダウンロードして、以下のサンプルコードで使用できます。

[sampleSingleSheet.xlsx](79527948.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}

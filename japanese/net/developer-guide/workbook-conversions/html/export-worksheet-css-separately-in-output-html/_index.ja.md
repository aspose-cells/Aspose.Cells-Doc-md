---
title: 出力HTMLでワークシートのCSSを別々にエクスポートする
type: docs
weight: 80
url: /ja/net/export-worksheet-css-separately-in-output/
---

## **可能な使用シナリオ**

Aspose.CellsはExcelファイルをHTMLに変換する際に、ワークシートCSSを別々にエクスポートする機能を提供しています。この目的のために[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)プロパティを使用し、**true**に設定してください。

## **出力HTMLでワークシートのCSSを別々にエクスポートする**

次のサンプルコードは、Excelファイルを作成し、セル**B5**に**Red**のテキストを追加し、[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)プロパティを使用してHTML形式で保存します。コードによって生成された[output HTML](60489766.zip)には、**stylesheet.css**が含まれています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **単一のシートのワークブックをHTMLにエクスポートする**

Aspose.Cellsを使用して、複数のシートを含むワークブックをHTMLに変換すると、CSSと複数のHTMLファイルを含むフォルダが作成されます。このHTMLファイルをブラウザで開くと、タブが表示されます。同様の動作が、1つのワークシートを含むワークブックをHTMLに変換する場合に必要です。このようなHTMLファイルのために、以前は単一のシートのための別々のフォルダが作成されず、HTMLファイルだけが作成されていました。このようなHTMLファイルは、ブラウザで開くとタブが表示されません。MS Excelは、単一のシートについても適切なフォルダとHTMLを作成し、Aspose.Cells APIを使用して同じ動作を実装しています。サンプルファイルは以下のリンクからダウンロードできます。

[sampleSingleSheet.xlsx](79527937.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}

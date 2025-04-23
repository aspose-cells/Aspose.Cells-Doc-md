---
title: 出力HTMLでワークシートのCSSを別々にエクスポートする
type: docs
weight: 80
url: /ja/python-net/export-worksheet-css-separately-in-output/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETは、ExcelファイルをHTMLに変換する際にワークシートのCSSを個別にエクスポートする機能を提供します。この目的のために[**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately)プロパティを使用し、HTMLに保存する際に**true**に設定してください。

## **出力HTMLでワークシートのCSSを別々にエクスポートする**

次のサンプルコードは、Excelファイルを作成し、セル**B5**に**Red**のテキストを追加し、[**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately)プロパティを使用してHTML形式で保存します。コードによって生成された[output HTML](60489766.zip)には、**stylesheet.css**が含まれています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **単一のシートのワークブックをHTMLにエクスポートする**

複数シートのワークブックをHTMLに変換すると、HTMLファイルとCSSや複数のHTMLファイルを含むフォルダが作成されます。このHTMLファイルをブラウザで開くとタブが表示されます。同じ動作はシングルシートのワークブックにも適用され、変換時に同様のフォルダとHTMLが作成されます。以前は、単一シートのワークブックではフォルダは作成されず、HTMLファイルのみでした。このHTMLファイルはブラウザで開いたときタブを表示しません。MS Excelは単一シートでも適切なフォルダとHTMLを作成します。したがって、同じ動作をAspose.Cells for Python via .NET APIを使用して実現しています。サンプルファイルは以下のリンクからダウンロード可能で、以下のサンプルコードに使用できます：

[sampleSingleSheet.xlsx](79527937.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}

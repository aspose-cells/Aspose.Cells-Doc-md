---
title: 出力 HTML でワークシート CSS を個別にエクスポートする
type: docs
weight: 80
url: /ja/java/export-worksheet-css-separately-in-output-html/
---
## **考えられる使用シナリオ**

Aspose.Cells は、Excel ファイルを HTML に変換するときに、ワークシート CSS を個別にエクスポートする機能を提供します。この目的のために HtmlSaveOptions.ExportWorksheetCSSSeparately プロパティを使用し、Excel ファイルを HTML 形式で保存するときに true に設定してください。

## **出力 HTML でワークシート CSS を個別にエクスポートする**

次のサンプル コードでは、Excel ファイルを作成し、セル B5 にテキストを赤色で追加してから、HtmlSaveOptions.ExportWorksheetCSSSeparately プロパティを使用して HTML 形式で保存します。をご覧ください[出力 HTML](60489780.zip)参照用のコードによって生成されます。サンプル コードの結果として、その中に stylesheet.css があります。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **シングル シート ワークブックを HTML にエクスポートする**

複数のシートを含むワークブックを Aspose.Cells を使用して HTML に変換すると、CSS と複数の HTML ファイルを含むフォルダーと共に HTML ファイルが作成されます。この HTML ファイルをブラウザで開くと、タブが表示されます。 HTML に変換される場合、単一のワークシートを含むワークブックにも同じ動作が必要です。 以前は、単一シートのワークブック用に別のフォルダーが作成されず、HTML ファイルのみが作成されました。このような HTML ファイルは、ブラウザで開いたときにタブが表示されません。 Excel は適切なフォルダーと単一シートの HTML も作成するため、Aspose.Cells を使用して同じ動作が実装されます。サンプル ファイルは、以下のサンプル コードで使用するために次のリンクからダウンロードできます。

[sampleSingleSheet.xlsx](79527948.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}

---
title: 出力 HTML でワークシート CSS を個別にエクスポートする
type: docs
weight: 80
url: /ja/net/export-worksheet-css-separately-in-output/
---
## **考えられる使用シナリオ**

 Aspose.Cells は、Excel ファイルを HTML に変換するときに、ワークシートの CSS を個別にエクスポートする機能を提供します。[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)この目的のためにプロパティを設定し、**真実** ExcelファイルをHTML形式で保存しています。

## **出力 HTML でワークシート CSS を個別にエクスポートする**

次のサンプル コードは、Excel ファイルを作成し、セルにテキストを追加します。**B5**の**赤**color を使用して HTML 形式で保存します[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)財産。をご覧ください[出力 HTML](60489766.zip)参照用のコードによって生成されます。見つけるだろう**stylesheet.css**サンプルコードの結果としてその中に。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **シングル シート ワークブックを HTML にエクスポートする**

複数のシートを含むワークブックを Aspose.Cells を使用して HTML に変換すると、CSS と複数の HTML ファイルを含むフォルダーと共に HTML ファイルが作成されます。この HTML ファイルをブラウザで開くと、タブが表示されます。 HTML に変換される場合、単一のワークシートを含むワークブックには同じ動作が必要です。 以前は、単一シートのワークブック用に別のフォルダーが作成されず、HTML ファイルのみが作成されました。このような HTML ファイルは、ブラウザで開いたときにタブが表示されません。 MS Excel は、1 つのシートに対して適切なフォルダーと HTML も作成するため、Aspose.Cells API を使用して同じ動作が実装されます。サンプル ファイルは、次のリンクからダウンロードして、以下のサンプル コードで使用できます。

[sampleSingleSheet.xlsx](79527937.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}

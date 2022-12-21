---
title: HtmlCrossType を使用して、出力 HTML で文字列をクロスする方法を指定します
type: docs
weight: 140
url: /ja/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **考えられる使用シナリオ**

セルにテキストまたは文字列が含まれているが、セルの幅よりも大きい場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを HTML に保存する場合、[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)列挙。次の値があります。

- **HtmlCrossType.Default**: MS Excel のような表示で、次のセルに依存します。次のセルが null の場合、文字列が交差するか、切り捨てられます。

- **HtmlCrossType.MSExport**: HTML をエクスポートする MS Excel のような文字列を表示します。

- **HtmlCrossType.Cross**: HTML クロス文字列を表示します。大きな HTML ファイルを作成する場合のパフォーマンスは、値を Default または FitToCell に設定するよりも 10 倍以上速くなります。

- **HtmlCrossType.FitToCell**: セルの幅内の文字列のみを表示します。

## **HtmlCrossType を使用して、出力 HTML で文字列をクロスする方法を指定します**

次のサンプル コードは、[サンプル Excel ファイル](51740732.xlsx)を指定して HTML 形式で保存します。[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) .をダウンロードしてください[出力 HTML](51740734.zip)このコードで生成されます。サンプルの Excel ファイルには、このスクリーンショットに示すように、赤い色で囲まれた画像が含まれています。[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)出力 HTML の値。

![todo:画像_代替_文章](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}

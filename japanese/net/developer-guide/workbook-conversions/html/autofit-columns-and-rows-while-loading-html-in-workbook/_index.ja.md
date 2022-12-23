---
title: ワークブックに HTML をロードする際の列と行の自動調整
type: docs
weight: 120
url: /ja/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **考えられる使用シナリオ**

Workbook オブジェクト内に HTML ファイルをロードするときに、列と行を自動調整できます。を設定してください**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**プロパティへ**真実**この目的のために。

## **ワークブックに HTML をロードする際の列と行の自動調整**

次のサンプル コードは、最初にサンプル HTML を読み込みオプションなしで Workbook に読み込み、XLSX 形式で保存します。次に、サンプル HTML を再度 Workbook に読み込みますが、今回は、設定後に HTML を読み込みます。**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**プロパティへ**真実**XLSX 形式で保存します。両方の出力 Excel ファイルをダウンロードしてください。[AutoFitColsAndRows なしで Excel ファイルを出力する](outputWithout_AutoFitColsAndRows.xlsx)と[AutoFitColsAndRows を使用して Excel ファイルを出力する](outputWith_AutoFitColsAndRows.xlsx).次のスクリーンショットは、**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**両方の出力 Excel ファイルのプロパティ。

![todo:画像_代替_文章](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}


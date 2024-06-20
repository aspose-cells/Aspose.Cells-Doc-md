---
title: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 120
url: /ja/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能な使用シナリオ**

HTMLファイルをWorkbookオブジェクト内で読み込む際に列と行を自動調整できます。このためには、[**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)プロパティを**true**に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

次のサンプルコードは、最初にロードオプションなしでサンプルHTMLをWorkbookに読み込み、XLSX形式で保存します。その後、[**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)プロパティを**true**に設定してサンプルHTMLをWorkbookに再度読み込み、XLSX形式で保存します。出力エクセルファイル、つまり[Auftput Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx)と[AutoFitColsAndRowsを使用した出力Excelファイル](outputWith_AutoFitColsAndRows.xlsx)をダウンロードしてください。次のスクリーンショットは、[**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)プロパティの効果を示したものです。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}


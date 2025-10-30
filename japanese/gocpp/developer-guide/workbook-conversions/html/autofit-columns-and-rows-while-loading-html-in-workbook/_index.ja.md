---
title: Golangを使ったC++経由でWorkbookにHTMLを読み込みながら列と行を自動調整する
linktitle: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 120
url: /ja/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: HTMLを読み込みながら列と行を自動調整する方法について、Aspose.Cells for C++を使用して学びます。
---

## **可能な使用シナリオ**

HTMLファイルをWorkbookオブジェクト内で読み込む際に列と行を自動調整できます。このためには、[**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/)プロパティを**true**に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

次のサンプルコードは、最初にロードオプションなしでサンプルHTMLをWorkbookに読み込み、XLSX形式で保存します。その後、[**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/)プロパティを**true**に設定してサンプルHTMLをWorkbookに再度読み込み、XLSX形式で保存します。出力エクセルファイル、つまり[Auftput Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx)と[AutoFitColsAndRowsを使用した出力Excelファイル](outputWith_AutoFitColsAndRows.xlsx)をダウンロードしてください。次のスクリーンショットは、[**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/)プロパティの効果を示したものです。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}

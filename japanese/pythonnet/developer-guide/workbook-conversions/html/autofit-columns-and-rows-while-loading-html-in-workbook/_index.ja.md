---
title: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 120
url: /ja/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aspose.Cells for Python via NETを使用して、ブックをロードしながらHTMLの列と行を自動調整する方法を示しています。
keywords: ワークブックにHTMLをロードする際に、列と行を自動的に調整することができます。このためには{0}プロパティを true に設定してください。
---

## **可能な使用シナリオ**

HTMLファイルをWorkbookオブジェクト内で読み込む際に列と行を自動調整できます。このためには、[**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)プロパティを**true**に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

次のサンプルコードは、最初にロードオプションなしでサンプルHTMLをWorkbookに読み込み、XLSX形式で保存します。その後、[**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)プロパティを**true**に設定してサンプルHTMLをWorkbookに再度読み込み、XLSX形式で保存します。出力エクセルファイル、つまり[Auftput Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx)と[AutoFitColsAndRowsを使用した出力Excelファイル](outputWith_AutoFitColsAndRows.xlsx)をダウンロードしてください。次のスクリーンショットは、[**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)プロパティの効果を示したものです。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}


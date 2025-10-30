--- 
title: GolangをC++経由でExcelファイルをHTMLに保存する際にコメントをエクスポート 
linktitle: Excel ファイルを HTML に保存する際にコメントをエクスポート 
type: docs 
weight: 40 
url: /ja/go-cpp/export-comments-while-saving-excel-file-to/ 
description: GolangをC++経由でAspose.Cellsを使用してExcelファイルをHTMLに保存する際にコメントをエクスポートする方法を学ぶ 
--- 

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際にコメントはエクスポートされませんが、Aspose.Cellsはこの機能を [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/isexportcomments/) プロパティで提供しています。これを **true** に設定すると、コメントもHTMLに表示されます。

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**

以下のサンプルコードは、[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/isexportcomments/) プロパティの使い方を説明しています。スクリーンショットは、設定を **true** にした場合のHTMLへの影響を示しています。参考のために [サンプルExcelファイル](50528260.xlsx) と [生成されたHTML](5052826.txt) をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportCommentsWhileSavingExcelFileToHtml.go" >}}

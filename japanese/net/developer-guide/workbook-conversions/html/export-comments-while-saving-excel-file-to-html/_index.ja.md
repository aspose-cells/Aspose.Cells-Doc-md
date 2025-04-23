---
title: Excel ファイルを HTML に保存する際にコメントをエクスポート
type: docs
weight: 40
url: /ja/net/export-comments-while-saving-excel-file-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存すると、コメントはエクスポートされません。ただし、Aspose.Cellsは[**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/)プロパティを使用してこの機能を提供します。**true**に設定すると、HTMLにExcelファイルに含まれるコメントも表示されます。

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**

次のサンプルコードでは[**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/)プロパティの使用方法を説明しています。コードによるHTMLへの影響を示すスクリーンショットが**true**として設定されている場合に表示されます。参照用に、[サンプルExcelファイル](50528260.xlsx)と[生成されたHTML](5052826.txt)をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}

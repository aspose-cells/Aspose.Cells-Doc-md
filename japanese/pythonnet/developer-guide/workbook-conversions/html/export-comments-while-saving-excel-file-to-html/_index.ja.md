---
title: Excel ファイルを HTML に保存する際にコメントをエクスポート
type: docs
weight: 40
url: /ja/python-net/export-comments-while-saving-excel-file-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとコメントはエクスポートされませんが、Aspose.Cells for Python via .NETは[**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments)プロパティを使用してこの機能を提供します。これを**true**に設定すると、Excelファイル内のコメントもHTMLに表示されます。

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**

次のサンプルコードでは[**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments)プロパティの使用方法を説明しています。コードによるHTMLへの影響を示すスクリーンショットが**true**として設定されている場合に表示されます。参照用に、[サンプルExcelファイル](50528260.xlsx)と[生成されたHTML](5052826.txt)をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}

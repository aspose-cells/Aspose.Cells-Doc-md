---
title: Excel ファイルを HTML に保存する際にコメントをエクスポート
type: docs
weight: 60
url: /ja/python-java/export-comments-while-saving-excel-file-to/
---

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**
ExcelをHTMLに変換すると、コメントはエクスポートされません。Aspose.Cells for Python via Javaは、ExcelからHTMLへの変換中にコメントをエクスポートする機能を提供しています。これを実現するには、APIは[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)プロパティを提供しています。[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)プロパティの値を**True**に設定すると、出力HTMLにコメントがエクスポートされます。

以下のスクリーンショットは、サンプルコードスニペットによって生成された出力HTMLファイルを示しています。

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

以下のサンプルコードは、ExcelからHTMLに変換する際にコメントをエクスポートする方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}

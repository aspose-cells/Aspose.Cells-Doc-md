---
title: Excel ファイルを HTML に保存しながらコメントをエクスポートする
type: docs
weight: 60
url: /ja/python-java/export-comments-while-saving-excel-file-to/
---
## **Excel ファイルを HTML に保存しながらコメントをエクスポートする**
Excel を HTML に変換すると、コメントはエクスポートされません。 Aspose.Cells for Python via Java は、Excel から HTML への変換中にコメントをエクスポートする機能を提供します。これを実現するために、API は[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)財産。値の設定[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)プロパティへ**真実**出力 HTML にコメントをエクスポートします。

次のスクリーンショットは、サンプル コード スニペットによって生成された出力 HTML ファイルを示しています。

![todo:画像_代替_文章](Export-Comments-while-Saving-Excel-file-to-Html.png)

次のサンプル コードは、Excel から HTML への変換中にコメントをエクスポートする方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}

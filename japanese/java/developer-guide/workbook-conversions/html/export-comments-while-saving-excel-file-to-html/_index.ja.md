---
title: Excel ファイルを HTML に保存する際にコメントをエクスポート
type: docs
weight: 40
url: /ja/java/export-comments-while-saving-excel-file-to-html/
---

## **可能な使用シナリオ**

Excel ファイルを HTML に保存する際、コメントはエクスポートされません。ただし、Aspose.Cells ではこの機能を [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments) プロパティを使用して提供しています。true に設定すると、HTML に Excel ファイル内のコメントが表示されます。

## **Excel ファイルを HTML に保存する際にコメントをエクスポート**

次のサンプルコードは、[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments) プロパティの使用方法を説明しています。コードが true に設定されたときの HTML への影響を示すスクリーンショットです。参照には、[サンプル Excel ファイル](50528270.xlsx) と生成された[HTML](50528269) をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.java" >}}
{{< app/cells/assistant language="java" >}}

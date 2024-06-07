---
title: 在将Excel文件保存为HTML时导出评论
type: docs
weight: 40
url: /zh/java/export-comments-while-saving-excel-file-to-html/
---

## **可能的使用场景**

当您将Excel文件保存为HTML时，注释不会被导出。但是Aspose.Cells通过[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments)属性提供了此功能。如果您将其设置为**true**，那么HTML中将显示Excel文件中的注释。

## **在保存Excel文件为Html时导出注释**

以下示例代码解释了[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments)属性的用法。当属性设置为**true**时，截图显示了代码对HTML的影响。请下载[sample Excel文件](50528270.xlsx)和生成的[HTML](50528269)以供参考。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.java" >}}

---
title: 在将Excel文件保存为HTML时导出评论
type: docs
weight: 40
url: /zh/net/export-comments-while-saving-excel-file-to/
---

## **可能的使用场景**

当您将Excel文件保存为HTML时，评论不会被导出。但是，Aspose.Cells通过[**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/)属性提供了此功能。如果将其设置为**true**，则HTML也将显示Excel文件中存在的评论。

## **在将Excel文件保存为HTML时导出评论**

以下示例代码解释了[**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/)属性的用法。当将其设置为**true**时，代码对HTML的影响在截图中显示。请参考[示例Excel文件](50528260.xlsx)和[生成的HTML](5052826.txt)。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.cs" >}}

---
title: 导出Excel文件为HTML时导出注释
type: docs
weight: 40
url: /zh/net/export-comments-while-saving-excel-file-to/
---

## **可能的使用场景**

当您将 Excel 文件保存为HTML时，注释不会被导出。但是，Aspose.Cells 提供了使用 [**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/) 属性来实现此功能。如果您将其设置为 **true**，那么HTML中也会显示 Excel 文件中存在的注释。

## **在将 Excel 文件保存为 HTML 时导出批注**

下面的示例代码解释了 [**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/) 属性的用法。截图展示了当它设置为 **true** 时代码对 HTML 的影响。请下载[sample Excel file](50528260.xlsx)和[generated HTML](5052826.txt)以供参考。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.cs" >}}

--- 
title: 用 Golang 通过 C++ 导出评论在保存 Excel 为 HTML 时 
linktitle: 导出Excel文件为HTML时导出注释 
type: docs 
weight: 40 
url: /zh/go-cpp/export-comments-while-saving-excel-file-to/ 
description: 学习用 Golang 通过 C++ 在将 Excel 文件导出为 HTML 时导出评论 
--- 

## **可能的使用场景**

将Excel保存为HTML时，评论不会被导出。但是，Aspose.Cells通过[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/isexportcomments/)属性提供此功能。如果将其设置为**true**，HTML中也会显示Excel文件中的评论。

## **在将 Excel 文件保存为 HTML 时导出批注**

下面的示例代码演示了[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/isexportcomments/)属性的用法。截图显示将其设置为**true**时，HTML的效果。请下载【示例Excel文件】(50528260.xlsx)和【生成的HTML】(5052826.txt)以供参考。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportCommentsWhileSavingExcelFileToHtml.go" >}}

---
title: 用 Golang 通过 C++ 导出 Excel 转 HTML 时的文档工作簿和工作表属性
linktitle: 导出Excel中的文档工作簿和工作表属性到HTML
type: docs
weight: 50
url: /zh/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: 学习如何在将Excel文件转换为HTML时导出或避免导出文档、工作簿和工作表属性，使用编号Aspose.Cells for C++。
---

## **可能的使用场景**

当使用Microsoft Excel或Aspose.Cells导出Excel为HTML时，它还会导出各种类型的文档、工作簿和工作表属性，如下截图所示。可以通过将[**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/)、[**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/)和[**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/)设置为**false**来避免导出这些属性。这些属性的默认值是**true**。下图显示了导出HTML中这些属性的样子。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **将Excel中的文档、工作簿和工作表属性导出为HTML**

下方示例代码加载【示例Excel文件】(61767776.xlsx)，并将其转换为HTML，未导出文档、工作簿及工作表属性，输出的HTML文件为(61767779.zip)。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}

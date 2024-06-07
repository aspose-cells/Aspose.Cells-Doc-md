---
title: 在Excel转HTML转换中导出文档工作簿和工作表属性
type: docs
weight: 50
url: /zh/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能的使用场景**

当使用Microsoft Excel或Aspose.Cells将Microsoft Excel文件导出为HTML时，它还会导出各种类型的文档、工作簿和工作表属性，如下图所示。您可以通过将[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties)、[**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)和[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties)设置为**false**来避免导出这些属性。这些属性的默认值为**true**。以下截图显示了导出的HTML中这些属性的外观。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **在Excel转HTML转换中导出文档、工作簿和工作表属性**

以下示例代码加载了[示例Excel文件](61767776.xlsx)并将其转换为HTML，在[输出HTML](61767779.zip)中不导出文档、工作簿和工作表属性。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}

---
title: 在Excel转HTML转换中导出文档工作簿和工作表属性
type: docs
weight: 50
url: /zh/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能的使用场景**

当将Microsoft Excel文件使用Microsoft Excel或Aspose.Cells导出为HTML时，它也会导出各种类型的文档、工作簿和工作表属性，如下面的截图所示。您可以通过将[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties)、[**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)和[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)设置为**false**来避免导出这些属性。这些属性的默认值为**true**。以下截图显示了这些属性在导出的HTML中的外观。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **在Excel转HTML转换中导出文档、工作簿和工作表属性**

以下示例代码加载了[示例Excel文件](61767784.xlsx)，将其转换为HTML，并在[输出的HTML](61767783.zip)中不导出文档、工作簿和工作表属性。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}

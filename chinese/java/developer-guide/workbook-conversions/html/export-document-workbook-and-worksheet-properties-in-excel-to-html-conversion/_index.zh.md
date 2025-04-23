---
title: 将Excel中的文档、工作簿和工作表属性导出为HTML
type: docs
weight: 50
url: /zh/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能的使用场景**

当使用Microsoft Excel或Aspose.Cells将Microsoft Excel文件导出为HTML时，也将导出各种类型的文档、工作簿和工作表属性，如下截图所示。您可以通过将 [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties)、[**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) 和 [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) 设为 **false** 来避免导出这些属性。这些属性的默认值为 **true**。下面的截图展示了导出的HTML中这些属性的样子。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **将Excel中的文档、工作簿和工作表属性导出为HTML**

以下示例代码加载了 [样本Excel文件](61767784.xlsx) 并将其转换为HTML，在 [输出HTML](61767783.zip) 中不导出文档、工作簿和工作表属性。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
{{< app/cells/assistant language="java" >}}

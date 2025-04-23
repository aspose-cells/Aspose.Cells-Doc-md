---
title: 将Excel中的文档、工作簿和工作表属性导出为HTML
type: docs
weight: 50
url: /zh/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能的使用场景**

当使用 Microsoft Excel 或 Aspose.Cells 将 Microsoft Excel 文件导出为 HTML 时，还会导出各种类型的文档、工作簿和工作表属性，如下面的截图所示。您可以通过将 [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties)、[**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) 和 [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) 设置为 **false** 来避免导出这些属性。这些属性的默认值是 **true**。下面的截图展示了导出的 HTML 中这些属性的样子。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **将Excel中的文档、工作簿和工作表属性导出为HTML**

下面的示例代码加载了[sample Excel file](61767776.xlsx)并将其转换为 HTML，并且在[output HTML](61767779.zip)中不导出文档、工作簿和工作表属性。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}

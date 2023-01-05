---
title: 将 Excel 中的文档工作簿和工作表属性导出到 HTML 转换
type: docs
weight: 50
url: /zh/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **可能的使用场景**

当使用 Microsoft Excel 或 Aspose.Cells 将 Microsoft Excel 文件导出到 HTML 时，它还会导出各种类型的文档、工作簿和工作表属性，如下面的屏幕截图所示。您可以通过设置[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)和[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties)作为**错误的**.这些属性的默认值为**真的**.以下屏幕截图显示了这些属性在导出的 HTML 中的样子。

![待办事项：图片_替代_文本](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **将 Excel 中的文档、工作簿和工作表属性导出到 HTML 转换**

下面的示例代码加载[示例 Excel 文件](61767776.xlsx)并将其转换为 HTML 并且不导出文档、工作簿和工作表属性[输出 HTML](61767779.zip).

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}

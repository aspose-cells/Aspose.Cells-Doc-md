---
title: Export Document Workbook and Worksheet Properties in Excel to HTML conversion
type: docs
weight: 50
url: /net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Possible Usage Scenarios**
When Microsoft Excel file is exported to HTML using Microsoft Excel or Aspose.Cells, it also exports various types of Document, Workbook and Worksheet properties as shown in the following screenshot. You can avoid exporting these properties by setting the [HtmlSaveOptions.ExportDocumentProperties](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [HtmlSaveOptions.ExportWorkbookProperties](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) and [HtmlSaveOptions.ExportWorksheetProperties](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) as **false**. The default value of these properties is **true**. The following screenshot shows how these properties look like in exported HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)
## **Export Document, Workbook and Worksheet Properties in Excel to HTML conversion**
The following sample code loads the [sample Excel file](61767776.xlsx) and converts it to HTML and does not export the Document, Workbook and Worksheet properties in [output HTML](61767779.zip).
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}

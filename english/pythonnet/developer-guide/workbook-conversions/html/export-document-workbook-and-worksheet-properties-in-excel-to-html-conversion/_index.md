---
title: Export Document Workbook and Worksheet Properties in Excel to HTML conversion
type: docs
weight: 50
url: /python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When Microsoft Excel file is exported to HTML using Microsoft Excel or Aspose.Cells, it also exports various types of Document, Workbook and Worksheet properties as shown in the following screenshot. You can avoid exporting these properties by setting the [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties), [**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties) and [**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) as **false**. The default value of these properties is **true**. The following screenshot shows how these properties look like in exported HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Export Document, Workbook and Worksheet Properties in Excel to HTML conversion**

The following sample code loads the [sample Excel file](61767776.xlsx) and converts it to HTML and does not export the Document, Workbook and Worksheet properties in [output HTML](61767779.zip).

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}

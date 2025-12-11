---
title: PDF
type: docs
weight: 220
url: /python-net/convert-excel-to-pdf/
description: Learn how to convert Excel to PDF with Aspose.Cells for Python via .NET API.
keywords: Python convert Excel to PDF, Convert Excel to PDF using Python, Python save Excel to PDF, Excel to PDF in Python
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET supports conversion of an Excel workbook into PDF. In this example, we will see the complete conversion of an Excel workbook into PDF.

{{% /alert %}}

## **Converting Excel Workbook to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells for Python via .NET supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET directly writes information about the API and version number in output documents. For example, upon rendering a document to PDF, Aspose.Cells for Python via .NET populates the **PDF Producer** field with a value, e.g., 'Aspose.Cells for Python via .NET v23.2'.

Please note that you can change this information in output documents by the [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/) property.

{{% /alert %}}

### **Direct Conversion**

Aspose.Cells for Python via .NET supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) method. The [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) method provides the [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) enumeration member that converts the native Excel files to PDF format.

Follow the steps below to directly convert the Excel spreadsheets to PDF format:

1. Instantiate an object of the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class by calling its empty constructor.  
2. You may open/load an existing template file or skip this step if you are creating the workbook from scratch.  
3. Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells for Python via .NET's APIs.  
4. When the spreadsheet code is complete, call the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) method to save the spreadsheet.

The file format should be PDF, so select *PDF* (a pre‑defined value) from the [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) enumeration to generate the final PDF document.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Advanced Conversion**

You may also opt to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) class gives you control over the print, font, security and compression settings for the output PDF. The most important property is [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) which enables you to save the Excel files to PDF/A‑compliant PDF files.

#### **Saving Workbook to PDF/A Compliant Files**

The code snippet below demonstrates how to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) class to save Excel files to PDF/A‑compliant PDF format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Please note, the [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) property was added with the release of Aspose.Cells for Python via .NET for .NET 5.3.0.

{{% /alert %}}

#### **Set the PDF Creation Time**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) class, you can get or set the PDF creation time. The following code demonstrates the use of [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) property to set the creation time of the PDF file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Set ContentCopyForAccessibility Option**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) class, you can get or set the PDF [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) option to control content access in the converted PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Export Custom Properties to PDF**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) class, you can export the custom properties in the source workbook to the PDF. The [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on **File** and then **Properties** as shown in the following image. Template file `sourceWithCustProps.xlsx` can be downloaded [here](sourceWithCustProps.xlsx) for testing, and the output PDF file `outSourceWithCustProps.pdf` is available [here](outSourceWithCustProps.pdf) for analysis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Conversion Attributes**

We work to enhance the conversion features with each new release. Aspose.Cells' Excel to PDF conversion still has a couple of limitations. MapChart is not supported when converting to PDF format. Also, some drawing objects are not supported well.

The table below lists all features that are fully or partially supported when exporting to PDF using Aspose.Cells for Python via .NET. This table is not final and does not cover all the spreadsheet attributes, but it identifies those features that are not supported or are partially supported for conversion to PDF.

| **Document Element** | **Attribute** | **Supported** | **Notes** |
| :- | :- | :- | :- |
| Alignment |   | Yes |   |
| Background settings |   | Yes |   |
| Border | Color | Yes |   |
| Border | Line style | Yes |   |
| Border | Line width | Yes |   |
| Cell Data |   | Yes |   |
| Comments |   | Yes |   |
| Conditional Formatting |   | Yes |   |
| Document Properties |   | Yes |   |
| Drawing Objects |   | Partially | Shadow and 3‑D effects for drawing objects are not supported well; WordArt and SmartArt are partially supported. |
| Font | Size | Yes |   |
| Font | Color | Yes |   |
| Font | Style | Yes |   |
| Font | Underline | Yes |   |
| Font | Effects | Yes |   |
| Images |   | Yes |   |
| Hyperlink |   | Yes |   |
| Charts |   | Partially | MapChart is not supported. |
| Merged Cells |   | Yes |   |
| Page Break |   | Yes |   |
| Page Setup | Header/Footer | Yes |   |
| Page Setup | Margins | Yes |   |
| Page Setup | Page Orientation | Yes |   |
| Page Setup | Page Size | Yes |   |
| Page Setup | Print Area | Yes |   |
| Page Setup | Print Titles | Yes |   |
| Page Setup | Scaling | Yes |   |
| Row Height/Column Width |   | Yes |   |
| RTL (Right to Left) Language |   | Yes |   |

{{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call the [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) method just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}

## **Advanced Topics**
- [Add PDF Bookmarks](/cells/python-net/add-pdf-bookmarks/)
- [Add PDF Bookmarks with Named Destinations](/cells/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Avoid Blank Page in Output PDF when there is Nothing to Print](/cells/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Convert XLSX File to PDF Format](/cells/python-net/convert-xlsx-file-to-pdf-format/)
- [Convert Excel file to PDF format compatible with PDFA-1a](/cells/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convert XLS File with Images or Charts to PDF](/cells/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Create PdfBookmarkEntry for Chart Sheet](/cells/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Fit All Worksheet Columns on Single PDF Page](/cells/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignore Errors while Rendering Excel to PDF](/cells/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limit the Number of Pages Generated - Excel to PDF Conversion](/cells/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Print Comments while saving to PDF](/cells/python-net/print-comments-while-saving-to-pdf/)
- [Render Office Add‑Ins while converting Excel to PDF](/cells/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion](/cells/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Render Unicode Supplementary characters in output PDF by Aspose.Cells](/cells/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling Added Images - Excel to PDF Conversion](/cells/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Save Each Worksheet to a Different PDF File](/cells/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Save Excel into PDF with Standard or Minimum Size](/cells/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Save Specified Worksheets to PDF](/cells/python-net/save-specified-worksheets-to-pdf/)
- [Secure PDF Documents](/cells/python-net/secure-pdf-documents/)
- [Specify how to cross string in output PDF and image](/cells/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)

{{< app/cells/assistant language="python-net" >}}

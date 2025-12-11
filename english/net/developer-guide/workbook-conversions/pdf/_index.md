---
title: PDF
type: docs
weight: 220
url: /net/convert-excel-to-pdf/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supports conversion of an Excel workbook into PDF. In this example, we will see the complete conversion of an Excel workbook into PDF.

{{% /alert %}}

## **Converting Excel Workbook to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format, and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{% alert color="primary" %}}

Aspose.Cells for .NET directly writes the information about API and version number in output documents. For example, upon rendering a document to PDF, Aspose.Cells for .NET populates the **PDF Producer** field with a value, e.g., **'Aspose.Cells v23.2'**.

Please note that you can change this information in output documents by the [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/) property.

{{% /alert %}}

### **Direct Conversion**

Aspose.Cells for .NET supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class's [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method. The [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method provides the [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) enumeration member that converts the native Excel files to PDF format.

Follow the steps below to directly convert the Excel spreadsheets to PDF format:

1. Instantiate an object of the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class by calling its empty constructor.  
2. You may open/load an existing template file or skip this step if you are creating the workbook from scratch.  
3. Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.  
4. When the spreadsheet code is complete, call the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class's [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method to save the spreadsheet.

The file format should be PDF, so select *Pdf* (a pre‑defined value) from the [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) enumeration to generate the final PDF document.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Advanced Conversion**

You may also opt to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) class gives you control over the print, font, security, and compression settings for the output PDF.

The most important property is **Compliance**, which enables you to set the PDF standards compliance level. Currently, you can save to PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A‑1a, PDF/A‑1b, PDF/A‑2a, PDF/A‑2b, PDF/A‑2u, PDF/A‑3a, PDF/A‑3b, and PDF/A‑3u formats. Note that with the PDF/A format, an output file size is larger than a regular PDF file size.

#### **Saving Workbook to PDF/A Compliant Files**

The code snippet below demonstrates how to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) class to save Excel files to PDF/A‑compliant PDF format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Please note, the [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) property was added with the release of Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Set the PDF Creation Time**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) class, you can get or set the PDF creation time. The following code demonstrates the use of [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) property to set the creation time of the PDF file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Set ContentCopyForAccessibility Option**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) class, you can get or set the PDF **AccessibilityExtractContent** option to control content access in the converted PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Export Custom Properties to PDF**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) class, you can export the custom properties in the source workbook to the PDF. The **PdfCustomPropertiesExport** enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on **File** and then **Properties** as shown in the following image. The template file `sourceWithCustProps.xlsx` can be downloaded [here](sourceWithCustProps.xlsx) for testing, and the output PDF file `outSourceWithCustProps.pdf` is available [here](outSourceWithCustProps.pdf) for analysis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Conversion Attributes**

We work to enhance the conversion features with each new release. Aspose.Cells' Excel‑to‑PDF conversion still has a couple of limitations. **MapChart** is not supported when converting to PDF format. Also, some drawing objects are not supported well.

The table below lists features that are fully or partially supported when exporting to PDF using Aspose.Cells. This table is not final and does not cover all spreadsheet attributes, but it identifies those features that are not supported or only partially supported for conversion to PDF.

| **Document Element** | **Attribute** | **Supported** | **Notes** |
| :- | :- | :- | :- |
| Alignment |  | Yes |  |
| Background settings |  | Yes |  |
| Border | Color | Yes |  |
| Border | Line style | Yes |  |
| Border | Line width | Yes |  |
| Cell Data |  | Yes |  |
| Comments |  | Yes |  |
| Conditional Formatting |  | Yes |  |
| Document Properties |  | Yes |  |
| Drawing Objects |  | Partially | Shadow and 3‑D effects for drawing objects are not supported well; WordArt and SmartArt are partially supported. |
| Font | Size | Yes |  |
| Font | Color | Yes |  |
| Font | Style | Yes |  |
| Font | Underline | Yes |  |
| Font | Effects | Yes |  |
| Images |  | Yes |  |
| Hyperlink |  | Yes |  |
| Charts |  | Partially | MapChart is not supported. |
| Merged Cells |  | Yes |  |
| Page Break |  | Yes |  |
| Page Setup | Header/Footer | Yes |  |
| Page Setup | Margins | Yes |  |
| Page Setup | Page Orientation | Yes |  |
| Page Setup | Page Size | Yes |  |
| Page Setup | Print Area | Yes |  |
| Page Setup | Print Titles | Yes |  |
| Page Setup | Scaling | Yes |  |
| Row Height/Column Width |  | Yes |  |
| RTL (Right to Left) Language |  | Yes |  |

{{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}

## **Advanced Topics**
- [Add PDF Bookmarks](/cells/net/add-pdf-bookmarks/)
- [Add PDF Bookmarks with Named Destinations](/cells/net/add-pdf-bookmarks-with-named-destinations/)
- [Avoid Blank Page in Output PDF when there is Nothing to Print](/cells/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Change the Font on just the specific Unicode characters while saving to PDF](/cells/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Control loading of External Resources in MS Excel Workbook while rendering to PDF](/cells/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Convert XLSX File to PDF Format](/cells/net/convert-xlsx-file-to-pdf-format/)
- [Convert Excel file to PDF format compatible with PDFA-1a](/cells/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convert XLS File with Images or Charts to PDF](/cells/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Create PdfBookmarkEntry for Chart Sheet](/cells/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Fit All Worksheet Columns on Single PDF Page](/cells/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class](/cells/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Get Warnings for Font Substitution while Rendering Excel File](/cells/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignore Errors while Rendering Excel to PDF](/cells/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limit the Number of Pages Generated - Excel to PDF Conversion](/cells/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Print Comments while saving to PDF](/cells/net/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins while converting Excel to PDF](/cells/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion](/cells/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Render Unicode Supplementary characters in output PDF by Aspose.Cells](/cells/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling Added Images - Excel to PDF Conversion](/cells/net/resampling-added-images-excel-to-pdf-conversion/)
- [Save Each Worksheet to a Different PDF File](/cells/net/save-each-worksheet-to-a-different-pdf-file/)
- [Save Excel into PDF with Standard or Minimum Size](/cells/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Save Specified Worksheets to PDF](/cells/net/save-specified-worksheets-to-pdf/)
- [Secure PDF Documents](/cells/net/secure-pdf-documents/)
- [Specify how to cross string in output PDF and image](/cells/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}

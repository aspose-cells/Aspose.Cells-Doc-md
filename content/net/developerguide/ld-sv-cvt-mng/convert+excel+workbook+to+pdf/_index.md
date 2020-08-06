---
title : "Convert Excel Workbook to PDF" 
description : "" 
weight : 12066 
toc : false
type: docs
url: /net/developerguide/ld-sv-cvt-mng/convert+excel+workbook+to+pdf/
---

# Aspose.Cells for .NET : Convert Excel Workbook to PDF


Aspose.Cells supports conversion of Excel Workbook into PDF. In this example, we will see the complete conversion of an Excel Workbook into PDF.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Excel Workbook to PDF](#converting-excel-workbook-to-pdf)
    *   1.1 [Direct Conversion](#direct-conversion)
    *   1.2 [Advanced Conversion](#advanced-conversion)
        *   1.2.1 [Saving Workbook to PDF/A Complied Files](#saving-workbook-to-pdf/a-complied-files)
        *   1.2.2 [Set the PDF Creation Time](#set-the-pdf-creation-time)
        *   1.2.3 [Set ContentCopyForAccessibility option](#set-contentcopyforaccessibility-option)
        *   1.2.4 [Export Custom properties to PDF](#export-custom-properties-to-pdf)
    *   1.3 [Conversion Attributes](#conversion-attributes)
{{< /panel >}}
 

## Converting Excel Workbook to PDF

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

Aspose.Cells for .NET directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for .NET populates **Application** field with value 'Aspose.Cells' and **PDF Producer** field with value, e.g 'Aspose.Cells v17.9'.

Please note that you cannot instruct Aspose.Cells for .NET to change or remove this information from output Documents.

### Direct Conversion

Aspose.Cells for .NET supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [Save](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/save/index) method. The [Save](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/save/index) method provides the [SaveFormat.Pdf](https://apireference.aspose.com/net/cells/aspose.cells/saveformat) enumeration member that converts the native Excel files to PDF format.

Follow the below steps to directly convert the Excel spreadsheets to PDF format:

1.  Instantiate an object of the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class by calling its empty constructor.
2.  You may open/load an existing template file or skip this step if you are creating the workbook from scratch.
3.  Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.
4.  When the spreadsheet code is complete, call the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [Save](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/save/index) method to save the spreadsheet.

The file format should be PDF so select *Pdf *(a pre-defined value) from the [SaveFormat](https://apireference.aspose.com/net/cells/aspose.cells/saveformat) enumeration to generate the final PDF document.

### Advanced Conversion

You may also opt to use the [PdfSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [PdfSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions) class gives you control over the print, font, security and compression settings for the output PDF. The most important property is [Compliance](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/compliance) which enables you to save the Excel files to PDF/A compliant PDF files.

#### Saving Workbook to PDF/A Complied Files

The below-provided code snippet demonstrates how to use the [PdfSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions) class to save Excel files to PDF/A compliant PDF format.

Please note, the [Compliance](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/compliance) property was added with the release of Aspose.Cells for .NET 5.3.0.

#### Set the PDF Creation Time

With the [PdfSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions) class, you can get or set the PDF creation time. The following code demonstrates the use of [PdfSaveOptions.CreatedTime](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/createdtime) property to set the creation time of the PDF file.

#### Set ContentCopyForAccessibility option

With the [PdfSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions) class, you can get or set the PDF [AccessibilityExtractContent](https://apireference.aspose.com/net/cells/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) option to control the content access in the converted PDF.

#### Export Custom properties to PDF

With the [PdfSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions) class, you can export the custom properties in the source workbook to the PDF. [PdfCustomPropertiesExport](https://apireference.aspose.com/net/cells/aspose.cells.rendering/pdfcustompropertiesexport) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on File and then properties option as shown in the following image. Template file "sourceWithCustProps.xlsx"  can be downloaded [here](https://docs2.aspose.com/cells/net/attachments/5013526/72417282.xlsx) for testing and output PDF file "outSourceWithCustProps" is available [here](https://docs2.aspose.com/cells/net/attachments/5013526/72417283.pdf) for analysis.

![image](72417284.png)

### Conversion Attributes

We work to enhance the conversion features with each new release. Aspose.Cell's Excel to PDF conversion still has a couple of limitations. Some spreadsheet formatting might be lost when converting to PDF format. Also, some drawing objects are not yet supported.

The table that follows lists all features that are fully or partially supported when exporting to PDF using Aspose.Cells. This table is not final and does not cover all the spreadsheet attributes but it does identify those features that are not supported or partially supported for conversion to PDF.

{{< table style="table-striped" >}}
|Document Element|Attribute|Supported|Notes|
|:----|:----|:----|:----|
|Alignment| |Yes| |
|Background settings| |Yes| |
|Border|Color|Yes| |
|Border|Line style|Yes| |
|Border|Line width|Yes| |
|Cell Data| |Yes| |
|Comments| |No| |
|Conditional Formatting| |Yes| |
|Document Properties| |Yes| |
|Drawing Objects| |Partially|Supported Objects: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Font|Size|Yes| |
|Font|Color|Yes| |
|Font|Style|Yes| |
|Font|Underline|Yes| |
|Font|Effects|Partially|Only strike through effect is supported|
|Images| |Yes| |
|Hyperlink| |Yes| |
|Charts| |Partially| |
|Merged Cells| |Yes| |
|Page Break| |Yes| |
|Page Setup|Header/Footer|Yes| |
|Page Setup|Margins|Yes| |
|Page Setup|Page Orientation|Yes| |
|Page Setup|Page Size|Yes| |
|Page Setup|Print Area|Yes| |
|Page Setup|Print Titles|Yes| |
|Page Setup|Scaling|Yes| |
|Row Height/Column Width| |Yes| |
|RTL (Right to Left) Language| |Yes| |
{{< /table >}}

If your spreadsheet contains formulas, it is best to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.


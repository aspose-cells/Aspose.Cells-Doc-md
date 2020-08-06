---
title: Convert Excel to PDF
type: docs
weight: 50
url: /pythonjava/convert-excel-to-pdf/
---

## **Convert Excel to PDF**
PDF documents are widely used as a standard format of exchanging documents between organizations, government sectors, and individuals. Software developers are often asked to devise a way to easily convert Microsoft Excel files into PDF documents. Aspose.Cells for Python via Java API provides the ability to convert Excel files to PDF documents (including PDF/A). Aspose.Cell's converts spreadsheets to PDF with a high degree of accuracy and fidelity.
### **Direct Conversion**
To save an Excel file directly to PDF, you may use the [Workbook.save](https://apireference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20com.aspose.cells.SaveOptions\)) method and pass [SaveFormat.PDF](https://apireference.aspose.com/cells/python/asposecells.api/saveformat#PDF) as the second parameter.

The following code snippet demonstrates the use of [SaveFormat.PDF](https://apireference.aspose.com/cells/python/asposecells.api/saveformat#PDF) and the [Workbook.save](https://apireference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20com.aspose.cells.SaveOptions\)) method to convert Excel to PDF format.

{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}
### **Advanced Conversion**
To have more control over the conversion to PDF, the API provides the [PdfSaveOptions](https://apireference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) class. The [PdfSaveOptions](https://apireference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) class can be used to set different attributes for the conversion. Setting different properties of the [PdfSaveOptions](https://apireference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) class will give you control over the Print, Font, Security, and Compression settings for the resultant PDF file. The most notable property is the [Compliance](https://apireference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance) that enables you to save the Excel files to PDF/A compliant PDF files.

{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}} 

if your spreadsheet contains formulas, call the [Workbook.calculateFormula](https://apireference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula\(\)) method just before rendering the spreadsheet to PDF. This ensures that the formula dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}

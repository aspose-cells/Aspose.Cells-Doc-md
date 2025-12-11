---
title: Convert Excel to PDF
type: docs
weight: 50
url: /python-java/convert-excel-to-pdf/
description: How to convert Excel to PDF with Python. This article demonstrates converting Excel files to PDF using Python and an easy-to-use Aspose.Cells for Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Convert Excel to PDF**

PDF documents are widely used as a standard format of exchanging documents between organizations, government sectors, and individuals. Software developers are often asked to devise a way to easily convert Microsoft Excel files into PDF documents. Aspose.Cells for Python via Java API provides the ability to convert Excel files to PDF documents (including PDF/A). Aspose.Cells converts spreadsheets to PDF with a high degree of accuracy and fidelity.

### **Direct Conversion**

To save an Excel file directly to PDF, you may use the [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) method and pass [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) as the second parameter.

The following code snippet demonstrates the use of [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) and the [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) method to convert Excel to PDF format.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Advanced Conversion**

To have more control over the conversion to PDF, the API provides the [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) class. The [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) class can be used to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) class will give you control over the print, font, security, and compression settings for the resultant PDF file. The most notable property is the [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance) that enables you to save the Excel files to PDF/A‑compliant PDF files.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

If your spreadsheet contains formulas, call the [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) method just before rendering the spreadsheet to PDF. This ensures that the formula‑dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}

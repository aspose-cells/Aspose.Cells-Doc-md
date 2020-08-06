---
title: Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion
type: docs
weight: 40
url: /java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

When working with large Microsoft Excel files (for example a workbook that has many sheets, each with 50 columns and 300 or more rows of data), you might want the PDF output to show one page per worksheet, regardless of the size of the worksheet. This would mean that each page is likely to have a radically different page size. This can be achieved by using Aspose.Cells for Java.

{{% /alert %}} 

Please see the following sample code that converts an Excel file with multiple worksheets to PDF.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}} 

If the [PdfSaveOptions.OnePagePerSheet](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) option is set to **true**, all the sheet content is rendered to one PDF page. The paper size set by [PageSetup](https://apireference.aspose.com/java/cells/com.aspose.cells/PageSetup) is invalid, but the other settings set with [PageSetup](https://apireference.aspose.com/java/cells/com.aspose.cells/PageSetup) still take effect.

{{% /alert %}} {{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call the [Workbook.calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula\(\)) method just before rendering the spreadsheet to PDF. This ensures that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}

---
title: Fit All Worksheet Columns on Single PDF Page
type: docs
weight: 70
url: /java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}} 

Sometimes you want to generate a PDF file that fits all a worksheet's columns onto a single page. The [PdfSaveOptions.setAllColumnsInOnePagePerSheet](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) property provides this feature in a very easy-to-use manner. Complex calculations such as the height and width of the output PDF page are handled internally and are based on the data in the worksheet.

{{% /alert %}} 
#### **Fit Worksheet Columns on Single PDF Page**
[PdfSaveOptions.setAllColumnsInOnePagePerSheet](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) ensures that all columns of a worksheet are rendered to a single PDF page, although rows may expand to several pages depending upon the data in worksheet.

{{% alert color="primary" %}} 

When a given worksheet has many columns, the rendered PDF file may show the contents at a very small size. It is still readable when scaled up in a viewing application such as Acrobat Reader.

{{% /alert %}} 

The sample code below shows how to use the [PdfSaveOptions.setAllColumnsInOnePagePerSheet](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) property to render a large worksheet of 100 columns.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [Workbook.calculateFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula\(\)) method just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
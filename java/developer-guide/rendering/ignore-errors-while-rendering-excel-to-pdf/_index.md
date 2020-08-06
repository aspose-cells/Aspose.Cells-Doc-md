---
title: Ignore Errors while Rendering Excel to PDF
type: docs
weight: 70
url: /java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Possible Usage Scenarios**
Sometimes when you convert your Excel file to PDF, errors or exceptions occur and the conversion process terminates. You can ignore all such errors during the conversion process using the [PdfSaveOptions.IgnoreError](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#IgnoreError) property. This way, the conversion process will complete smoothly without throwing any error or exception but the loss of data may occur. Therefore, please use this property only if the loss of data is not critical for you.
## **Ignore Errors while Rendering Excel to PDF**
The following code loads the [sample Excel file](attachments/54690159/55541813.xlsx) but the sample Excel file is erroneous and throws an error during the [conversion to PDF](attachments/54690159/55541814.pdf) in 17.11 but since we are using [PdfSaveOptions.IgnoreError](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#IgnoreError) property, it does not throw an error. However, one rounded red arrow-like shape as shown in this screenshot is lost.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}

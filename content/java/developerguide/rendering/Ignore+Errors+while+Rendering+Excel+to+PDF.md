+++
title = "Ignore Errors while Rendering Excel to PDF" 
description = "" 
weight = 12079 
+++

Aspose.Cells for Java : Ignore Errors while Rendering Excel to PDF  

# Aspose.Cells for Java : Ignore Errors while Rendering Excel to PDF


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#IgnoreErrorswhileRenderingExceltoPDF-PossibleUsageScenarios)
*   2 [Ignore Errors while Rendering Excel to PDF](#IgnoreErrorswhileRenderingExceltoPDF-IgnoreErrorswhileRenderingExceltoPDF)
*   3 [Sample Code](#IgnoreErrorswhileRenderingExceltoPDF-SampleCode)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes when you convert your Excel file to PDF, errors or exceptions occur and the conversion process terminates. You can ignore all such errors during the conversion process using the [PdfSaveOptions.IgnoreError](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#IgnoreError) property. This way, the conversion process will complete smoothly without throwing any error or exception but the loss of data may occur. Therefore, please use this property only if the loss of data is not critical for you.

## Ignore Errors while Rendering Excel to PDF

The following code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/54690159/55541813.xlsx) but the sample Excel file is erroneous and throws an error during the [conversion to PDF](https://docs2.aspose.com/cells/java/attachments/54690159/55541814.pdf) in 17.11 but since we are using [PdfSaveOptions.IgnoreError](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#IgnoreError) property, it does not throw an error. However, one rounded red arrow-like shape as shown in this screenshot is lost.

![](https://docs2.aspose.com/cells/java/attachments/54690159/55541815.png)

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [PdfSaveOptions.IgnoreError-True-Ignores-the-Errors-while-Excel2Pdf-Conversion.png](https://docs2.aspose.com/cells/java/attachments/54690159/55541815.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputErrorExcel2Pdf.pdf](https://docs2.aspose.com/cells/java/attachments/54690159/55541814.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleErrorExcel2Pdf.xlsx](https://docs2.aspose.com/cells/java/attachments/54690159/60489731.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleErrorExcel2Pdf.xlsx](https://docs2.aspose.com/cells/java/attachments/54690159/55541813.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  


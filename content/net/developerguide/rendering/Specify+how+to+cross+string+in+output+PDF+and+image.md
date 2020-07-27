+++
title = "Specify how to cross string in output PDF and image" 
description = "" 
weight = 12099 
+++

Aspose.Cells for .NET : Specify how to cross string in output PDF and image  

# Aspose.Cells for .NET : Specify how to cross string in output PDF and image


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#SpecifyhowtocrossstringinoutputPDFandimage-PossibleUsageScenarios)
*   2 [Specify how to cross string in output PDF/Image using TextCrossType](#SpecifyhowtocrossstringinoutputPDFandimage-SpecifyhowtocrossstringinoutputPDF/ImageusingTextCrossType)
{{< /panel >}}
 

## Possible Usage Scenarios

When a cell contains text or string but it is larger than the width of the cell, then the string overflows if the next cell in the next column is null or empty. When you save your Excel file into PDF/Image, you can control this overflow by specifying the cross type using the [TextCrossType](https://apireference.aspose.com/net/cells/aspose.cells/textcrosstype) enumeration. It has the following values

*   **TextCrossType.Default**

Display text like MS Excel which depends on the next cell. If the next cell is null, the string will cross or it will be truncated.

*   **TextCrossType.CrossKeep**

Display the string like MS Excel exporting PDF/Image

*   **TextCrossType.CrossOverride**

Display all the text by crossing other cells and override the text of crossed cells

*   **TextCrossType.StrictInCell**

Only display the string within the width of the cell.

## Specify how to cross string in output PDF/Image using TextCrossType

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [TextCrossType](https://apireference.aspose.com/net/cells/aspose.cells/textcrosstype). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](https://docs2.aspose.com/cells/net/attachments/81690955/81920905.xlsx)

[outputCrossType.pdf](https://docs2.aspose.com/cells/net/attachments/81690955/81920903.pdf)

[outputCrossType.png](https://docs2.aspose.com/cells/net/attachments/81690955/81920904.png)

Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output-17.12.0.pdf](https://docs2.aspose.com/cells/net/attachments/81690955/81920900.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output-17.11.0.pdf](https://docs2.aspose.com/cells/net/attachments/81690955/81920901.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleRenderOfficeAdd-Ins.xlsx](https://docs2.aspose.com/cells/net/attachments/81690955/81920902.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputCrossType.pdf](https://docs2.aspose.com/cells/net/attachments/81690955/81920903.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputCrossType.png](https://docs2.aspose.com/cells/net/attachments/81690955/81920904.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleCrossType.xlsx](https://docs2.aspose.com/cells/net/attachments/81690955/81920905.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  


---
title : "Get Warnings for Font Substitution while Rendering Excel File" 
description : "" 
weight : 20378 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/get+warnings+for+font+substitution+while+rendering+excel+file/
---

# Aspose.Cells for .NET : Get Warnings for Font Substitution while Rendering Excel File


Sometimes, when rendering a Microsoft Excel file to PDF, Aspose.Cells substitutes fonts. Aspose.Cells provides a feature that lets developers know what particular font has been substituted by firing a warning. This is a useful feature that can help you identify why an Aspose.Cells rendered PDF looks different from the original Microsoft Excel file so you can take appropriate actions. For example, installing the missing fonts so that rendering results look the same.

To get warnings for font substitution when rendering Excel files to PDF, implement the `IWarningCallback` interface and set the `PdfSaveOptions.WarningCallback` property with your implemented interface.

The screenshot below shows a source Excel file that we will use in the following code. It has some text in the cells A6 and A7 in fonts that are not rendered fine by Microsoft Excel.

{{< table style="table-striped" >}}
|Not all fonts are rendered correctly|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017493/5112613.png)|
{{< /table >}}

Aspose.Cells will substitute the fonts in the cells A6 and A7 with suitable fonts as shown below.

{{< table style="table-striped" >}}
|Substituted fonts|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017493/5112610.png)|
{{< /table >}}

## Download Source File and Output PDF

You can download the source Excel file and the output PDF from the following links

*   [source.xlsx](https://docs2.aspose.com/cells/net/attachments/5017493/5112611.xlsx)
*   [output.pdf](https://docs2.aspose.com/cells/net/attachments/5017493/5112616.pdf)

## Code

The following code implements the `IWarningCallback` and set the `PdfSaveOptions.WarningCallback` property with the implemented interface. Now, whenever any font will be substituted in any cell, Aspose.Cells will fire a warning inside the `WarningCallback.Warning()` method.

## Output

After converting the source Excel file to PDF, the warnings are output to the debug console like this:

{{< code lang="cs" >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /code >}}

If your spreadsheet contains formulas, it is best to call `Workbook.CalculateFormula` method just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [fonts-substitution-warnings-1.png](https://docs2.aspose.com/cells/net/attachments/5017493/5112613.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [fonts-substitution-warnings-2.png](https://docs2.aspose.com/cells/net/attachments/5017493/5112610.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [source.xlsx](https://docs2.aspose.com/cells/net/attachments/5017493/5112611.xlsx) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output.pdf](https://docs2.aspose.com/cells/net/attachments/5017493/5112616.pdf) (image/png)  


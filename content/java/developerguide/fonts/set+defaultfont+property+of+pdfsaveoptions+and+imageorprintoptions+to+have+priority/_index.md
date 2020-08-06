---
title : "Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority" 
description : "" 
weight : 12070 
toc : false
type: docs
url: /java/developerguide/fonts/set+defaultfont+property+of+pdfsaveoptions+and+imageorprintoptions+to+have+priority/
---

# Aspose.Cells for Java : Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Set DefaultFont property of PdfSaveOptions/ImageOrPrintOptions](#set-defaultfont-property-of-pdfsaveoptions/imageorprintoptions)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

While setting the **DefaultFont** property of [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions) and [ImageOrPrintOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImageOrPrintOptions), you might expect that saving to PDF or image would set that **DefaultFont** to all the text in the workbook that has a missing (not installed) font.

Generally, when saving to PDF or image, Aspose.Cells will first try to set Workbook's default font (i.e., [Workbook.DefaultStyle.Font](https://apireference.aspose.com/java/cells/com.aspose.cells/style#Font)). If workbook's default font still cannot show/render text properly, then Aspose.Cells will try to render with font mentioned against **DefaultFont** attribute in [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImageOrPrintOptions).

To cope with your expectation, we have a Boolean property named "**CheckWorkbookDefaultFont**" in [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImageOrPrintOptions). You can set it to false to disable trying workbook's default font or let the **DefaultFont** setting in [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImageOrPrintOptions) to have priority

## Set DefaultFont property of PdfSaveOptions/ImageOrPrintOptions

The following sample code opens an Excel file. The A1 cell (in the first worksheet) has a text set to "Christmas Time Font text". The font name is "Christmas Time Personal Use" that is not installed on the machine. We set **DefaultFont** attribute of [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImageOrPrintOptions) to "Times New Roman". We also set **CheckWorkbookDefaultFont **Boolean property to "**false**" which ensures that the text of A1 cell is rendered with "Times New Roman" font and should not use the default font of the workbook ("Calibri" in this case). The code renders the first worksheet to PNG and TIFF image formats. It finally renders to the PDF file format. 

The default value of ***CheckWorkbookDefaultFont*** attribute is **true**.

This is the screenshot of the [template file](https://docs2.aspose.com/cells/java/attachments/48136510/49446914.xlsx) used in the example code.

![image](48496707.png)

This is the output PNG image after setting the [ImageOrPrintOptions.DefaultFont](https://apireference.aspose.com/java/cells/com.aspose.cells/imageorprintoptions#DefaultFont) property to "Times New Roman`"`.

![image](48496708.png)

See the output [TIFF](https://docs.aspose.com/download/attachments/48136475/out1_imageTIFF.tiff?version=1&modificationDate=1500578450497&api=v2) image after setting the [ImageOrPrintOptions.DefaultFont](https://apireference.aspose.com/java/cells/com.aspose.cells/imageorprintoptions#DefaultFont) property to "Times New Roman`".`

See the output [P](https://docs.aspose.com/download/attachments/48136475/out1_imageTIFF.tiff?version=1&modificationDate=1500578450497&api=v2)[DF](https://docs.aspose.com/download/attachments/48136475/out1_pdf.pdf?version=1&modificationDate=1500578496704&api=v2) file after setting the [PdfSaveOptions.DefaultFont](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#DefaultFont) property to "Times New Roman`".`

## Sample Code


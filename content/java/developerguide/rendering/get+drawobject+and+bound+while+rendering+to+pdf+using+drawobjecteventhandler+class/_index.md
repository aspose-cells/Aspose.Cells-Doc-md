---
title : "Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class" 
description : "" 
weight : 12078 
toc : false
type: docs
url: /java/developerguide/rendering/get+drawobject+and+bound+while+rendering+to+pdf+using+drawobjecteventhandler+class/
---

# Aspose.Cells for Java : Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class](#get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells provides an abstract class [DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObjectEventHandler) which has a [draw()](https://apireference.aspose.com/java/cells/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) method. The user can implement [DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObjectEventHandler) and utilize the [draw()](https://apireference.aspose.com/java/cells/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) method to get the [DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject) and **Bound **while rendering Excel to PDF or Image. Here is a brief description of the parameters of the [draw()](https://apireference.aspose.com/java/cells/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) method.

*   `drawObject`

[DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject) will be initialized and returned when rendering

*   `x`

Left of [DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject)

*   `y`

Top of [DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject)

*   `width`

Width of [DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject)

*   `height`

Height of [DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject)

If you are rendering Excel file to PDF, then you can utilize [DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObjectEventHandler) class with [PdfSaveOptions.DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Similarly, if you are rendering Excel file to Image, you can utilize [DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObjectEventHandler) class with [ImageOrPrintOptions.DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class

Please see the following sample code. It loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/64454899/64716843.xlsx) and saves it as [output PDF](https://docs2.aspose.com/cells/java/attachments/64454899/64716842.pdf). While rendering to PDF, it utilizes [PdfSaveOptions.DrawObjectEventHandler](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) property and captures the [DrawObject](https://apireference.aspose.com/java/cells/com.aspose.cells/DrawObject) and **Bound** of existing cells and objects e.g. images etc. If the drawObject type is Cell, it prints its Bound and StringValue. And if the drawObject type is Image, it prints its Bound and Shape Name. Please see the console output of the sample code given below for more help.

## Sample Code

## Console Output

\[X\]: 153.60349 \[Y\]: 82.94118 \[Width\]: 103.203476 \[Height\]: 14.470589 \[Cell Value\]: This is sample text.----------------------\[X\]: 267.28854 \[Y\]: 153.12354 \[Width\]: 161.25542 \[Height\]: 128.78824 \[Shape Name\]: Sun----------------------


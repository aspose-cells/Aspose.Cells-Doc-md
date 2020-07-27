+++
title = "Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class" 
description = "" 
weight = 12094 
+++

Aspose.Cells for .NET : Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class  

# Aspose.Cells for .NET : Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#GetDrawObjectandBoundwhilerenderingtoPdfusingDrawObjectEventHandlerclass-PossibleUsageScenarios)
*   2 [Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class](#GetDrawObjectandBoundwhilerenderingtoPdfusingDrawObjectEventHandlerclass-GetDrawObjectandBoundwhilerenderingtoPdfusingDrawObjectEventHandlerclass)
*   3 [Sample Code](#GetDrawObjectandBoundwhilerenderingtoPdfusingDrawObjectEventHandlerclass-SampleCode)
*   4 [Console Output](#GetDrawObjectandBoundwhilerenderingtoPdfusingDrawObjectEventHandlerclass-ConsoleOutput)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells provides an abstract class [DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler) which has a [Draw()](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler/methods/draw) method. The user can implement [DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler) and utilize the [Draw()](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler/methods/draw) method to get the [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject) and Bound while rendering Excel to PDF or Image. Here is a brief description of the parameters of the [Draw()](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler/methods/draw) method.

*   `drawObject`

[DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject) will be initialized and returned when rendering

*   `x`

Left of [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject)

*   `y`

Top of [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject)

*   `width`

Width of [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject)

*   `height`

Height of [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject)

If you are rendering Excel file to PDF, then you can utilize [DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler) class with [PdfSaveOptions.DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). Similarly, if you are rendering Excel file to Image, you can utilize [DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobjecteventhandler) class with [ImageOrPrintOptions.DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class

Please see the following sample code. It loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/64454877/64716821.xlsx) and saves it as [output PDF](https://docs2.aspose.com/cells/net/attachments/64454877/64716822.pdf). While rendering to PDF, it utilizes [PdfSaveOptions.DrawObjectEventHandler](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) property and captures the [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject) and Bound of existing cells and objects e.g. images etc. If the [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject) type is Cell, it prints its Bound and StringValue. And if the [DrawObject](https://apireference.aspose.com/net/cells/aspose.cells.rendering/drawobject) type is Image, it prints its Bound and Shape Name. Please see the console output of the sample code given below for more help.

## Sample Code

## Console Output

\[X\]: 153.6035 \[Y\]: 82.94118 \[Width\]: 103.2035 \[Height\]: 14.47059 \[Cell Value\]: This is sample text.----------------------\[X\]: 267.6917 \[Y\]: 153.4853 \[Width\]: 160.4491 \[Height\]: 128.0647 \[Shape Name\]: Sun----------------------

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx](https://docs2.aspose.com/cells/net/attachments/64454877/64716821.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf](https://docs2.aspose.com/cells/net/attachments/64454877/64716822.pdf) (application/pdf)  


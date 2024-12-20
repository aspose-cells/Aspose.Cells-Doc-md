---
title: Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class
type: docs
weight: 70
url: /net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Possible Usage Scenarios**

Aspose.Cells provides an abstract class [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) which has a [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) method. The user can implement [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) and utilize the [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) method to get the [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) and Bound while rendering Excel to PDF or Image. Here is a brief description of the parameters of the [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) method.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) will be initialized and returned when rendering

- x: Left of [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Top of [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- width: Width of [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- height: Height of [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

If you are rendering Excel file to PDF, then you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) class with [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). Similarly, if you are rendering Excel file to Image, you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) class with [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class**

Please see the following sample code. It loads the [sample Excel file](64716821.xlsx) and saves it as [output PDF](64716822.pdf). While rendering to PDF, it utilizes [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) property and captures the [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) and Bound of existing cells and objects e.g. images etc. If the [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type is Cell, it prints its Bound and StringValue. And if the [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type is Image, it prints its Bound and Shape Name. Please see the console output of the sample code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Console Output**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
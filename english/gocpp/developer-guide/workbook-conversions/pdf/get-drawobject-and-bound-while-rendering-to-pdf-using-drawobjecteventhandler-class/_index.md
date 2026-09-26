---
title: Get DrawObject and Bound while rendering to PDF with Golang via C++ using DrawObjectEventHandler class
linktitle: Get DrawObject and Bound while rendering to PDF
type: docs
weight: 70
url: /go-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Learn how to use the DrawObjectEventHandler class in C++ to capture DrawObject and Bound while rendering Excel files to PDF or images.
---

## **Possible Usage Scenarios**

Aspose.Cells provides an abstract class [**DrawObjectEventHandler**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/) which has a [**Draw()**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/draw/) method. The user can implement [**DrawObjectEventHandler**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/) and utilize the [**Draw()**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/draw/) method to get the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/) and its bounds while rendering Excel to PDF or an image. Here is a brief description of the parameters of the [**Draw()**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/draw/) method.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/) will be initialized and returned when rendering
- x: left coordinate of the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/)
- y: top coordinate of the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/)
- width: width of the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/)
- height: height of the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/)

If you are rendering an Excel file to PDF, then you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/) class with [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/deletepaginatedsaveoptions/). Similarly, if you are rendering an Excel file to an image, you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/) class with [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/go-cpp/drawobjecteventhandler/).

## **Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class**

Please see the following sample code. It loads the [sample Excel file](64716821.xlsx) and saves it as [output PDF](64716822.pdf). While rendering to PDF, it utilizes [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/deletepaginatedsaveoptions/) property and captures the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/) and its bounds of existing cells and objects, e.g., images, etc. If the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/) type is *Cell*, it prints its bounds and string value. If the [**DrawObject**](https://reference.aspose.com/cells/go-cpp/drawobject/) type is *Image*, it prints its bounds and shape name. Please see the console output of the sample code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetDrawobjectAndBoundWhileRenderingToPdfUsingDrawobjecteventhandlerClass.go" >}}

## **Console Output**

{{< highlight go >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="go" >}}

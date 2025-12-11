---
title: Converting Worksheet to Image using ImageOrPrint Options
type: docs
weight: 90
url: /python-net/converting-worksheet-to-image-using-imageorprint-options/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This document is designed to provide a detailed understanding of how to convert a worksheet to an image file and apply different image and print options for the image, options like resolution, TIFF compression, image format and page quality.

{{% /alert %}}

## **Saving Worksheets to Images - Different Approaches**

Sometimes, you might require presenting your worksheets as a pictorial representation. You need to present the worksheet images in your applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply, you want a worksheet rendered as an image so that you can use it elsewhere. Aspose.Cells for Python via .NET supports converting worksheets in Excel files to images. Also, Aspose.Cells for Python via .NET supports setting different options like image format, resolution (both vertical and horizontal), image quality, and other image and print options.

You might try Office Automation, but Office automation has its own drawbacks. There are several reasons and issues involved: for example, security, stability, scalability and speed, price, and features. In short, there are many reasons, with the top one being that Microsoft themselves strongly recommends against Office automation from software solutions.

This article shows how to create a console application in Visual Studio .NET, perform the conversion of a worksheet to image using different image and print options with a few simple lines of code using Aspose.Cells for Python via .NET API.

You need to import the [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) namespace to your program/project. It has several valuable classes, for example, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) etc.

The [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) class represents a worksheet to render images for. It has an overloaded [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return a System.Drawing.Bitmap object, and you can save an image file to disk/stream. There are several image formats supported, e.g., BMP, PNG, GIF, JPEG, TIFF, EMF, and so on.

## **Using Aspose.Cells to Convert Worksheet to Image using ImageOrPrint options**

### **Creating a template workbook in Microsoft Excel**

I created a new workbook in MS Excel and added some data to the first worksheet. Now, I will convert the template file’s worksheet “Sheet1” to an image file “SheetImage.tiff” and apply different image options such as horizontal and vertical resolutions, TIFF compression, etc.

### **Convert Worksheet to an Image file**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}

## **Image conversion using WorkbookRender**

A TIFF image can contain more than one frame. You can save the whole workbook to a single TIFF image with multiple frames or pages:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

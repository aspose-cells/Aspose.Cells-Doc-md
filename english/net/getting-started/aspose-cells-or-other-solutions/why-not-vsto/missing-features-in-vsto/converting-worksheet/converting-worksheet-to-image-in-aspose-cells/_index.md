---
title: Converting Worksheet to Image in Aspose.Cells  
type: docs  
weight: 20  
url: /net/converting-worksheet-to-image-in-aspose-cells/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

This document is designed to provide developers with a detailed understanding of how to convert a worksheet to an image file and a worksheet with multiple pages to an image file per page.  

Sometimes, you might need to present worksheets as images, for example to use them in applications or web pages. You might need to insert the images into a Word document, a **PDF** file, a PowerPoint presentation, or use them in some other scenario. Simply, you want to render the worksheet as an image. Aspose.Cells supports converting worksheets in Microsoft Excel files to images. Also, **Aspose.Cells** supports converting a workbook to multiple image files, one per page.

You might use Office automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example security, stability, scalability, speed, cost, and features. In short, there are many reasons, but the main one is that Microsoft itself strongly recommends against Office automation.

This article shows how to create a console application in Visual Studio .NET, convert a worksheet to an image, and convert a worksheet into one image for each page with a few simple lines of code using the Aspose.Cells API. You need to import the **Aspose.Cells.Rendering** namespace to your program/project. It has several valuable classes, e.g., **SheetRender**, **ImageOrPrintOptions**, **WorkbookRender**, etc. **Aspose.Cells.Rendering.SheetRender** class represents a worksheet to render images for the worksheet; it has an overloaded **ToImage** method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return a **System.Drawing.Bitmap** object, and you can save an image file to disk or a stream. Several image formats are supported, e.g., *.bmp*, *.png*, *.gif*, *.jpg*, *.jpeg*, *.tiff*, *.emf*, etc.

```csharp
//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");
```

## **Download Sample Code**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)

{{< app/cells/assistant language="csharp" >}}

---
title: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells can now render worksheet to graphic context. Graphic context can be anything like image file, screen or printer etc. Please use one of the following two methods to render worksheet to graphic context.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://apireference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://apireference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

The following code illustrates how to use Aspose.Cells to render worksheet to graphic context. Once you will execute a code, it will print the entire worksheet and fill the leftover empty space with blue color in graphics context and save the image as **OutputImage_out_.png** file. You can use any source excel file to try this code. Please also read the comments inside the code for better understanding.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}

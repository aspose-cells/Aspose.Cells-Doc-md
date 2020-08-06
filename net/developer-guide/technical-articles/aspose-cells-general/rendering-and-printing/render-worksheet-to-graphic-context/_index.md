---
title: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}} 

Aspose.Cells can now render worksheet to graphic context. Graphic context can be anything like image file, screen or printer etc. Please use one of the following two methods to render worksheet to graphic context.

- SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
- SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

{{% /alert %}} 
# **Render Worksheet to Graphic Context**
The following code illustrates how to use Aspose.Cells to render worksheet to graphic context. Once you will execute a code, it will print the entire worksheet and fill the leftover empty space with blue color in graphics context and save the image as **OutputImage_out_.png** file. You can use any source excel file to try this code. Please also read the comments inside the code for better understanding.



{{< gist "aspose-cells" "c326c6c668fc372e30569fa9e0f6bf4b" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}





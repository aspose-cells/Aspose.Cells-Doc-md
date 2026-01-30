---
title: Render Worksheet to Graphic Context with Go
linktitle: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /gocpp/render-worksheet-to-graphic-context/
description: Learn how to render a worksheet to a graphic context using Aspose.Cells for Go.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}  

Aspose.Cells can now render a worksheet to a graphic context. The graphic context can be anything such as an image file, a screen, or a printer. Please use one of the following two methods to render a worksheet to a graphic context.  

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/gocpp/aspose.cells.rendering/sheetrender/toimage/)  
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/gocpp/aspose.cells.rendering/sheetrender/toimage/)  

{{% /alert %}}  

The following code illustrates how to use Aspose.Cells to render a worksheet to a graphic context. Once you execute the code, it will render the entire worksheet, fill the remaining empty space with a blue color in the graphics context, and save the image as the **OutputImage_out.png** file. You can use any source Excel file to try this code. Please also read the comments inside the code for better understanding.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderWorksheetToGraphicContext.go" >}}  

{{< app/cells/assistant language="go" >}}
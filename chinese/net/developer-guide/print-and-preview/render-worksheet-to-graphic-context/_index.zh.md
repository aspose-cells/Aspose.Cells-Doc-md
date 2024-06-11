---
title: 将工作表呈现到图形上下文
type: docs
weight: 300
url: /zh/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells现在可以将工作表呈现到图形上下文。图形上下文可以是图像文件、屏幕或打印机等。请使用以下两种方法之一将工作表呈现到图形上下文。

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

以下代码示例说明了如何使用Aspose.Cells将工作表呈现到图形上下文。一旦执行代码，它将在图形上下文中打印整个工作表，并用蓝色填充剩余的空白空间，并将图像保存为**OutputImage_out_.png**文件。您可以使用任何源Excel文件来尝试这段代码。此外，请阅读代码内部的注释以更好地理解。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}

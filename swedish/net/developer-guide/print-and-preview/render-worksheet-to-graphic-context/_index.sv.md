---
title: Återge arbetsblad till grafisk kontext
type: docs
weight: 300
url: /sv/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells kan nu rendera kalkylblad till grafisk kontext. Grafiskt sammanhang kan vara vad som helst som bildfil, skärm eller skrivare etc. Använd en av följande två metoder för att rendera kalkylblad till grafiskt sammanhang.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float höjd)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 Följande kod illustrerar hur man använder Aspose.Cells för att rendera kalkylblad till grafisk kontext. När du har kört en kod kommer den att skriva ut hela kalkylbladet och fylla det överblivna tomma utrymmet med blå färg i grafiksammanhang och spara bilden som**OutputImage_out_.png** fil. Du kan använda valfri källexcel-fil för att prova den här koden. Läs även kommentarerna i koden för bättre förståelse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}

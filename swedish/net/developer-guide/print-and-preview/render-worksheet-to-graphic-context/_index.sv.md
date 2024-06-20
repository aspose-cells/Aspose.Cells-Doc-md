---
title: Rendera arbetsblad till grafiskt sammanhang
type: docs
weight: 300
url: /sv/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells kan nu rendera arbetsblad till grafiskt sammanhang. Grafiskt sammanhang kan vara vad som helst som bildfil, skärm eller skrivare osv. Använd en av de följande två metoderna för att rendera arbetsblad till grafiskt sammanhang.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

Följande kod illustrerar hur man använder Aspose.Cells för att rendera arbetsblad till grafiskt sammanhang. När du kör koden kommer den att skriva ut hela arbetsbladet och fylla den överblivna tomma platsen med blå färg i grafiskt sammanhang och spara bilden som **OutputImage_out_.png**-fil. Du kan använda vilken käll-Excel-fil som helst för att prova denna kod. Läs också kommentarerna i koden för bättre förståelse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}

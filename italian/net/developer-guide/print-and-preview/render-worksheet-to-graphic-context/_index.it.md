---
title: Rappresentare il foglio di calcolo nel contesto grafico
type: docs
weight: 300
url: /it/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells ora può rappresentare il foglio di calcolo nel contesto grafico. Il contesto grafico può essere qualsiasi cosa, come un file immagine, schermo o stampante, ecc. Si prega di utilizzare uno dei seguenti due metodi per rappresentare il foglio di calcolo nel contesto grafico.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

Il codice seguente illustra come utilizzare Aspose.Cells per rappresentare il foglio di calcolo nel contesto grafico. Una volta eseguito il codice, stamperà l'intero foglio di calcolo e riempirà lo spazio vuoto rimanente con il colore blu nel contesto grafico e salverà l'immagine come file **OutputImage_out_.png**. È possibile utilizzare qualsiasi file excel di origine per provare questo codice. Si prega di leggere anche i commenti all'interno del codice per una migliore comprensione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
{{< app/cells/assistant language="csharp" >}}

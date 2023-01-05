---
title: Renderizza il foglio di lavoro nel contesto grafico
type: docs
weight: 300
url: /it/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells ora può eseguire il rendering del foglio di lavoro nel contesto grafico. Il contesto grafico può essere qualsiasi cosa come file di immagine, schermo o stampante, ecc. Utilizzare uno dei due metodi seguenti per eseguire il rendering del foglio di lavoro nel contesto grafico.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 Il codice seguente illustra come utilizzare Aspose.Cells per eseguire il rendering del foglio di lavoro nel contesto grafico. Una volta eseguito un codice, stamperà l'intero foglio di lavoro e riempirà lo spazio vuoto rimanente con il colore blu nel contesto grafico e salverà l'immagine come**OutputImage_out_.png** file. Puoi utilizzare qualsiasi file Excel di origine per provare questo codice. Si prega di leggere anche i commenti all'interno del codice per una migliore comprensione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}

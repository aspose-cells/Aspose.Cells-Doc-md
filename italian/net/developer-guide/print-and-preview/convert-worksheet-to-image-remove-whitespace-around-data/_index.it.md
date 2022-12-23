---
title: "Converti foglio di lavoro in immagine: rimuovi gli spazi bianchi intorno ai dati"
type: docs
weight: 40
url: /it/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

volte, è necessario presentare immagini del foglio di lavoro in applicazioni o pagine Web. Ad esempio, potrebbe essere necessario inserire immagini in un documento Word, un file PDF, una presentazione PowerPoint o qualche altro documento. Fondamentalmente, vuoi rendere un foglio di lavoro come un'immagine in modo che possa essere incollato in altre applicazioni. Aspose.Cells consente di convertire i fogli di lavoro Excel Microsoft in immagini.

{{% /alert %}}

## **Rimuovi gli spazi bianchi attorno ai dati**

 Il[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API converte un foglio di lavoro in un file immagine con qualsiasi attributo specificato, ad esempio formato immagine, fogli impaginati, ecc. Sono supportati diversi formati immagine, tra cui BMP, GIF, JPG, TIFF e EMF.

 Quando si utilizza la funzione da foglio a immagine, l'immagine di output presenta uno spazio bianco, ovvero un bordo, attorno ad essa per impostazione predefinita. Puoi rimuoverlo impostando i margini di impostazione della pagina superiore, inferiore, sinistro e destro per il foglio di lavoro di origine su 0 e specifica[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)attributi di conseguenza.

Il seguente frammento di codice rimuove lo spazio vuoto attorno ai dati nell'immagine di output.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}


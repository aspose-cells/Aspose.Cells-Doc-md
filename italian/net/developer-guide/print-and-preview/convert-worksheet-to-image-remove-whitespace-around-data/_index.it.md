---
title: Converti foglio elettronico in immagine  Rimuovi spazi vuoti intorno ai dati
type: docs
weight: 40
url: /it/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

A volte è necessario presentare immagini del foglio elettronico in applicazioni o pagine web. Ad esempio, potresti aver bisogno di inserire immagini in un documento di Word, un file PDF, una presentazione PowerPoint o qualche altro documento. Fondamentalmente, desideri renderizzare un foglio elettronico come un'immagine in modo che possa essere incollato in altre applicazioni. Aspose.Cells ti consente di convertire i fogli di lavoro di Microsoft Excel in immagini.

{{% /alert %}}

## **Rimuovi spazi vuoti intorno ai dati**

L'API [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) converte un foglio elettronico in un file immagine con eventuali attributi specificati, ad esempio formato immagine, fogli paginati, ecc. Sono supportati diversi formati di immagine, come BMP, GIF, JPG, TIFF e EMF.

Quando si utilizza la funzione foglio-in-immagine, l'immagine di output ha spazi vuoti, cioè un bordo, attorno ad essa per impostazione predefinita. È possibile rimuovere questo impostando i margini di impaginazione superiore, inferiore, sinistro e destro del foglio di lavoro di origine a 0 e specificando [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) attributi di conseguenza.

Il seguente frammento di codice rimuove gli spazi vuoti intorno ai dati nell'immagine di output.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}

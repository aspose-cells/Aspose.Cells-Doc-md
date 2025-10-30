---
title: Converti foglio elettronico in immagine  Rimuovi spazi vuoti intorno ai dati
type: docs
weight: 40
url: /it/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

A volte, è necessario presentare le immagini di un foglio di lavoro in applicazioni o pagine web. Ad esempio, potresti dover inserire immagini in un documento Word, in un file PDF, in una presentazione PowerPoint o in altri documenti. In sostanza, vuoi rendere un foglio di lavoro come immagine, in modo che possa essere incollato in altre applicazioni. Aspose.Cells per Python via .NET ti consente di convertire i fogli di calcolo di Microsoft Excel in immagini.

{{% /alert %}}

## **Rimuovi spazi vuoti intorno ai dati**

L'API [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) converte un foglio elettronico in un file immagine con eventuali attributi specificati, ad esempio formato immagine, fogli paginati, ecc. Sono supportati diversi formati di immagine, come BMP, GIF, JPG, TIFF e EMF.

Quando si utilizza la funzione foglio-in-immagine, l'immagine di output ha spazi vuoti, cioè un bordo, attorno ad essa per impostazione predefinita. È possibile rimuovere questo impostando i margini di impaginazione superiore, inferiore, sinistro e destro del foglio di lavoro di origine a 0 e specificando [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) attributi di conseguenza.

Il seguente frammento di codice rimuove gli spazi vuoti intorno ai dati nell'immagine di output.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

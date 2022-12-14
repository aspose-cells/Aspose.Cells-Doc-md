---
title: Rimuovi gli spazi bianchi dai dati prima del rendering nell'immagine
type: docs
weight: 270
url: /it/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

A volte, è necessario presentare immagini del foglio di lavoro in applicazioni o pagine Web. Ad esempio, potrebbe essere necessario inserire un'immagine in un documento Word, un file PDF, una presentazione PowerPoint o qualche altro documento. Fondamentalmente, vuoi rendere un foglio di lavoro come un'immagine in modo che possa essere incollato in altre applicazioni. Aspose.Cells API consente di convertire i fogli di lavoro Excel Microsoft in immagini.

{{% /alert %}}

 Il[**FoglioRendering**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)class è in grado di convertire un foglio di lavoro in un file immagine con qualsiasi attributo specificato, ad esempio formato immagine, fogli impaginati, ecc. Sono supportati diversi formati immagine, inclusi BMP, GIF, JPG, TIFF ed EMF.

 Quando si utilizza la funzione da foglio a immagine, l'immagine di output presenta uno spazio bianco/vuoto, ovvero un bordo, attorno ad essa per impostazione predefinita. Puoi rimuoverlo. Impostare i margini di impostazione della pagina superiore, sinistro, inferiore e destro per il foglio di lavoro di origine su 0 e specificare[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)attributi di conseguenza.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}

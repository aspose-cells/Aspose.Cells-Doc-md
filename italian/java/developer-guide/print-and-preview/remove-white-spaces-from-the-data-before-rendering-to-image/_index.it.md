---
title: Rimuovere gli spazi bianchi dai dati prima del rendering dell immagine
type: docs
weight: 270
url: /it/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

A volte è necessario presentare immagini di fogli di lavoro in applicazioni o pagine web. Ad esempio, potresti aver bisogno di inserire immagini in un documento Word, un file PDF, una presentazione PowerPoint o in un altro documento. Fondamentalmente, desideri rendere un foglio di calcolo come un'immagine in modo che possa essere incollato in altre applicazioni. Le API di Aspose.Cells consentono di convertire fogli di lavoro di Microsoft Excel in immagini.

{{% /alert %}}

La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) è in grado di convertire un foglio di lavoro in un file immagine con attributi specificati, ad esempio formato immagine, fogli paginati, ecc. Sono supportati vari formati di immagine, tra cui BMP, GIF, JPG, TIFF e EMF.

Quando si utilizza la funzione di foglio a immagine, l'immagine di output presenta spazi bianchi/vuoti, cioè un bordo, attorno ad essa per impostazione predefinita. È possibile rimuoverlo. Imposta i margini di configurazione pagina superiore, sinistra, inferiore e destra del foglio di lavoro di origine su 0 e specifica gli attributi [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) di conseguenza.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}

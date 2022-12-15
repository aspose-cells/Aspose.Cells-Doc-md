---
title: Immagine
type: docs
weight: 300
url: /it/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in diversi formati.

{{% /alert %}}

## Conversione della cartella di lavoro in TIFF

 Un file Excel può contenere più fogli con più pagine.[Workbook Render](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) ti consente di convertire Excel in TIFF con più pagine. Inoltre, puoi controllare più opzioni per TIFF, come[Compressione](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Profondità di colore](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Risoluzione([Risoluzione orizzontale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Risoluzione verticale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 Il seguente frammento di codice mostra come convertire Excel in TIFF con più pagine. Il[file Excel di origine](workbook-to-tiff-with-mulitiple-pages.xlsx) e[immagine TIFF generata](workbook-to-tiff-with-mulitiple-pages.tiff) sono allegati per il vostro riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Conversione del foglio di lavoro in immagine**

I fogli di lavoro contengono i dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

In qualità di sviluppatore, potresti dover presentare i fogli di lavoro come immagini. Ad esempio, potrebbe essere necessario utilizzare un'immagine di un foglio di lavoro in un'applicazione o in una pagina Web. Potresti voler inserire un'immagine in un documento Microsoft Word, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, vuoi un foglio di lavoro reso come immagine in modo da poterlo usare da qualche altra parte.

Aspose.Cells supporta la conversione di fogli di lavoro Excel in immagini. Per utilizzare questa funzione, è necessario importare il file**[Aspose.Cells.Rendering](https://reference.aspose.com/cells/net/aspose.cells.rendering)** spazio dei nomi al tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRendering](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, e altri.

 Il**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** class rappresenta un foglio di lavoro da visualizzare come immagini. Ha un metodo sovraccarico,**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**, che può convertire un foglio di lavoro in file immagine con diversi attributi o opzioni. Restituisce un oggetto System.Drawing.Bitmap ed è possibile salvare un file immagine su disco o stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Al momento, l'API per la conversione dei fogli di lavoro in immagini non supporta i grafici a bolle 3D.

{{% /alert %}}

## **Conversione del foglio di lavoro in SVG**

SVG è l'acronimo di Scalable Vector Graphics. SVG è una specifica basata sugli standard XML per la grafica vettoriale bidimensionale. È uno standard aperto che è stato sviluppato dal World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for .NET è stato in grado di convertire i fogli di lavoro in immagini SVG dalla versione 7.1.0. Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Argomenti avanzati**
- [Converti un grafico Excel in immagine](/cells/it/net/convert-an-excel-chart-to-image/)
- [Conversione del grafico in immagine in formato SVG](/cells/it/net/converting-chart-to-image-in-svg-format/)
- [Esporta il grafico in SVG con l'attributo viewBox](/cells/it/net/export-chart-to-svg-with-viewbox-attribute/)
- [Tieni traccia dell'avanzamento della conversione di Excel in TIFF](/cells/it/net/track-conversion-progress-of-excel-to-tiff/)

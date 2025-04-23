---
title: Immagine
type: docs
weight: 300
url: /it/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cells ti consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in formati diversi.

{{% /alert %}}

## Conversione del Workbook in TIFF

Un file Excel può contenere più fogli con pagine multiple. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) ti consente di convertire Excel in TIFF con pagine multiple. Inoltre, è possibile controllare molte opzioni per il TIFF, come [Compressione](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Profondità del colore](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Risoluzione ([Risoluzione orizzontale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Risoluzione verticale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

Il seguente snippet di codice mostra come convertire Excel in TIFF con pagine multiple. Il [file Excel di origine](workbook-to-tiff-with-mulitiple-pages.xlsx) e l'[immagine TIFF generata](workbook-to-tiff-with-mulitiple-pages.tiff) sono allegati per il tuo riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Conversione del foglio di lavoro in immagine**

I fogli di lavoro contengono dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti aver bisogno di presentare i fogli di lavoro come immagini. Ad esempio, potresti aver bisogno di utilizzare un'immagine di un foglio di lavoro in un'applicazione o una pagina web. Potresti voler inserire un'immagine in un documento di Microsoft Word, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, desideri un foglio di lavoro reso come immagine in modo che tu possa usarlo altrove.

Aspose.Cells supporta la conversione di fogli di calcolo Excel in immagini. Per utilizzare questa funzionalità, è necessario importare lo spazio dei nomi [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) nel tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), e altri.

La classe [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) rappresenta un foglio di lavoro da renderizzare come immagini. Ha un metodo sovraccaricato, [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), che può convertire un foglio di lavoro in file immagine con attributi o opzioni differenti. Restituisce un oggetto System.Drawing.Bitmap e puoi salvare un file immagine su disco o flusso. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Attualmente, l'API per la conversione dei fogli di lavoro in immagini non supporta i grafici a bolle 3D.

{{% /alert %}}

## **Conversione del foglio di lavoro in SVG**

SVG sta per Scalable Vector Graphics. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for .NET è stato in grado di convertire i fogli di lavoro in immagine SVG dalla versione 7.1.0. Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine SVG da un file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Argomenti avanzati**
- [Converti un Grafico Excel in Immagine](/cells/it/net/convert-an-excel-chart-to-image/)
- [Conversione del grafico in Immagine in formato SVG](/cells/it/net/converting-chart-to-image-in-svg-format/)
- [Esportare il grafico in SVG con attributo viewBox](/cells/it/net/export-chart-to-svg-with-viewbox-attribute/)
- [Monitora il progresso della conversione di Excel in TIFF](/cells/it/net/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="csharp" >}}

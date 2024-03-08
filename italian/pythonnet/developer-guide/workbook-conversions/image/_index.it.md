---
title: Image
type: docs
weight: 300
url: /it/python-net/convert-excel-to-image/
description: Convertire il grafico in Image utilizzando Aspose.Cells for Python via .NET API.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in diversi formati.

{{% /alert %}}

##  Conversione della cartella di lavoro in TIFF

 Un file Excel può contenere più fogli con più pagine.[WorkbookRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) ti consente di convertire Excel in TIFF con più pagine. Inoltre, puoi controllare più opzioni per TIFF, ad esempio[Compressione](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Profondità di colore](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Risoluzione([Risoluzione orizzontale](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Risoluzione verticale](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 Il seguente frammento di codice mostra come convertire Excel in TIFF con più pagine. IL[file Excel di origine](workbook-to-tiff-with-mulitiple-pages.xlsx) E[immagine generata TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) sono allegati per riferimento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **Conversione del foglio di lavoro in Image**

I fogli di lavoro contengono i dati che desideri analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti dover presentare i fogli di lavoro come immagini. Ad esempio, potrebbe essere necessario utilizzare l'immagine di un foglio di lavoro in un'applicazione o in una pagina Web. Potresti voler inserire un'immagine in un documento Word Microsoft, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, vuoi che un foglio di lavoro venga visualizzato come immagine in modo da poterlo utilizzare altrove.

Aspose.Cells for Python via .NET supporta la conversione di fogli di lavoro Excel in immagini. Per utilizzare questa funzionalità è necessario importare il file**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**spazio dei nomi al tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio *[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[OpzioniImmagineOrStampa](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[WorkbookRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**, e altri.

 IL**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**La classe rappresenta un foglio di lavoro da visualizzare come immagini. Ha un metodo sovraccaricato, *[immaginare](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**, che può convertire un foglio di lavoro in file immagine con diversi attributi o opzioni. Restituisce un oggetto System.Drawing.Bitmap ed è possibile salvare un file immagine su disco o in streaming. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Al momento, lo API per la conversione dei fogli di lavoro in immagini non supporta i grafici a bolle 3D.

{{% /alert %}}

##  **Conversione del foglio di lavoro in SVG**

SVG sta per Scalable Vector Graphics. SVG è una specifica basata sugli standard XML per la grafica vettoriale bidimensionale. È uno standard aperto sviluppato dal World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for Python via .NET è stato in grado di convertire i fogli di lavoro nell'immagine SVG dalla versione 7.1.0. Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **Argomenti avanzati**
- [Converti un grafico Excel in Image](/cells/it/python-net/convert-an-excel-chart-to-image/)
- [Conversione del grafico in Image nel formato SVG](/cells/it/python-net/converting-chart-to-image-in-svg-format/)
- [Esporta grafico a SVG con attributo viewBox](/cells/it/python-net/export-chart-to-svg-with-viewbox-attribute/)

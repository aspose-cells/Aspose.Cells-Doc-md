---
title: Immagine
type: docs
weight: 300
url: /it/python-net/convert-excel-to-image/
description: Converti Grafico in Immagine utilizzando l API Aspose.Cells for Python via .NET.
keywords: Python Converti Grafico in Immagine, Esporta Grafico in Immagine in Python via NET, Salva Grafico in Immagine in Python.
---


{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ti consente di esportare un foglio di lavoro dal workbook e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in diversi formati.

{{% /alert %}}

## Conversione del Workbook in TIFF

Un file Excel può contenere fogli multiple con pagine multiple. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) ti consente di convertire Excel in TIFF con pagine multiple. Inoltre, puoi controllare diverse opzioni per il TIFF, come [Compressione](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Profondità del colore](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Risoluzione ([Risoluzione orizzontale](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Risoluzione verticale](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

Il seguente snippet di codice mostra come convertire Excel in TIFF con pagine multiple. Il [file Excel di origine](workbook-to-tiff-with-mulitiple-pages.xlsx) e l'[immagine TIFF generata](workbook-to-tiff-with-mulitiple-pages.tiff) sono allegati per il tuo riferimento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **Conversione del foglio di lavoro in immagine**

I fogli di lavoro contengono dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti aver bisogno di presentare i fogli di lavoro come immagini. Ad esempio, potresti aver bisogno di utilizzare un'immagine di un foglio di lavoro in un'applicazione o una pagina web. Potresti voler inserire un'immagine in un documento di Microsoft Word, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, desideri un foglio di lavoro reso come immagine in modo che tu possa usarlo altrove.

Aspose.Cells for Python via .NET supporta la conversione dei fogli di lavoro Excel in immagini. Per utilizzare questa funzionalità, devi importare lo spazio dei nomi [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) nel tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/), e altri.

La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) rappresenta un foglio di lavoro da renderizzare come immagini. Ha un metodo sovraccaricato, [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), che può convertire un foglio di lavoro in file immagine con attributi o opzioni differenti. Restituisce un oggetto System.Drawing.Bitmap e puoi salvare un file immagine su disco o flusso. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Attualmente, l'API per la conversione dei fogli di lavoro in immagini non supporta i grafici a bolle 3D.

{{% /alert %}}

## **Conversione del foglio di lavoro in SVG**

SVG sta per Scalable Vector Graphics. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for Python via .NET è stato in grado di convertire i fogli di lavoro in immagine SVG dalla versione 7.1.0. Il seguente snippet di codice mostra come convertire un foglio di lavoro in un file immagine SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Argomenti avanzati**
- [Converti un Grafico Excel in Immagine](/cells/it/python-net/convert-an-excel-chart-to-image/)
- [Conversione del grafico in Immagine in formato SVG](/cells/it/python-net/converting-chart-to-image-in-svg-format/)
- [Esportare il grafico in SVG con attributo viewBox](/cells/it/python-net/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="python-net" >}}

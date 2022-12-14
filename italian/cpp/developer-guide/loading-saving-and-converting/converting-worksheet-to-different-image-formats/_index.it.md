---
title: Conversione del foglio di lavoro in diversi formati di immagine
type: docs
weight: 90
url: /it/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells consente di esportare un foglio di lavoro da una cartella di lavoro e convertirlo in diversi formati di immagine. Questo articolo spiega come convertire un foglio di lavoro in diversi formati di immagine.

{{% /alert %}} 
## **Conversione del foglio di lavoro in immagine**
I fogli di lavoro contengono i dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

In qualità di sviluppatore, potresti dover presentare i fogli di lavoro come immagini. Ad esempio, potrebbe essere necessario utilizzare un'immagine di un foglio di lavoro in un'applicazione o in una pagina Web. Potresti voler inserire un'immagine in un documento Word Microsoft, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, vuoi un foglio di lavoro reso come immagine in modo da poterlo usare da qualche altra parte.

Aspose.Cells supporta la conversione di fogli di lavoro Excel in immagini. Per utilizzare questa funzione, è necessario importare il file[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.rendering)spazio dei nomi al tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio,[ISheetRender](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render), [IImageOrPrintOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_image_or_print_options)e altri.

La classe `Aspose.Cells.Rendering.ISheetRender` rappresenta un foglio di lavoro di cui eseguire il rendering come immagini. Ha un metodo sovraccarico,[Immaginare](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render#ae508827a76d0c353ab0890024ec363c5), che può convertire un foglio di lavoro in file immagine con diversi attributi o opzioni. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine.
### **Formato PNG**
 Si prega di vedere il seguente codice di esempio, its[esempio di file Excel](67338402.xlsx) , e il[emettere immagini PNG](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG.cpp" >}}
### **Formato TIFF**
 Si prega di vedere il seguente codice di esempio, its[esempio di file Excel](67338402.xlsx) , e il[emette un'immagine TIFF](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF.cpp" >}}
## **Conversione del foglio di lavoro in SVG**
SVG è l'acronimo di Scalable Vector Graphics. SVG è una specifica basata sugli standard XML per la grafica vettoriale bidimensionale. È uno standard aperto che è stato sviluppato dal World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells per C++ è stato in grado di convertire i fogli di lavoro in immagini SVG dalla versione 18.5.0.

Per utilizzare questa funzione, importa lo spazio dei nomi `Aspose.Cells.Rendering` nel tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio `ISheetRender`, `IImageOrPrintOptions` e altre.

La classe `Aspose.Cells.Rendering.IImageOrPrintOptions` specifica che il foglio di lavoro verrà salvato in formato SVG. Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine SVG

 Si prega di vedere il seguente codice di esempio, its[esempio di file Excel](67338402.xlsx) , e il[emettere immagini SVG](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG.cpp" >}}

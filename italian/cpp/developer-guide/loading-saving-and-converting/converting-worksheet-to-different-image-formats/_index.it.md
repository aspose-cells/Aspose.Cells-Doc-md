---
title: Conversione di fogli di lavoro in diversi formati di immagine
type: docs
weight: 90
url: /it/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells ti consente di esportare un foglio di lavoro da una cartella di lavoro e convertirlo in diversi formati di immagine. Questo articolo spiega come convertire un foglio di lavoro in diversi formati di immagine.

{{% /alert %}} 
##  **Conversione di un foglio di lavoro in immagine**
I fogli di lavoro contengono i dati che desideri analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti dover presentare i fogli di lavoro come immagini. Ad esempio, potrebbe essere necessario utilizzare l'immagine di un foglio di lavoro in un'applicazione o in una pagina Web. Potresti voler inserire un'immagine in un documento Word Microsoft, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, vuoi che un foglio di lavoro venga visualizzato come immagine in modo da poterlo utilizzare altrove.

Aspose.Cells supporta la conversione di fogli di lavoro Excel in immagini. Per utilizzare questa funzionalità è necessario importare il file[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)spazio dei nomi al tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio,[SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [OpzioniImmagineOrStampa](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)e altri.

La classe `Aspose.Cells.Rendering.ISheetRender` rappresenta un foglio di lavoro da visualizzare come immagini. Ha un metodo sovraccarico,[Immaginare](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), che può convertire un foglio di lavoro in file immagine con attributi o opzioni diversi. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine.
###  **PNG Formato**
 Si prega di consultare il seguente codice di esempio, its[file Excel di esempio](67338402.xlsx) , e il[uscita PNG Immagini](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}
<!--
### **TIFF Format**
Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}
-->
##  **Conversione del foglio di lavoro in SVG**
SVG sta per Scalable Vector Graphics. SVG è una specifica basata sugli standard XML per la grafica vettoriale bidimensionale. È uno standard aperto sviluppato dal World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for C++ è stato in grado di convertire i fogli di lavoro nell'immagine SVG dalla versione 18.5.0.

Per utilizzare questa funzionalità, importa lo spazio dei nomi `Aspose.Cells.Rendering` nel tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio `ISheetRender`, `IImageOrPrintOptions` e altre.

La classe `Aspose.Cells.Rendering.IImageOrPrintOptions` specifica che il foglio di lavoro verrà salvato nel formato SVG. Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine SVG

 Si prega di consultare il seguente codice di esempio, its[file Excel di esempio](67338402.xlsx) , e il[uscita SVG Immagini](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}

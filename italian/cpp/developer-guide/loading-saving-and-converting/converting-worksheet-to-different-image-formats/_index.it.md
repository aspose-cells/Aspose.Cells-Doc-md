---
title: Conversione del foglio di lavoro in diversi formati di immagine
type: docs
weight: 90
url: /it/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells consente di esportare un foglio di lavoro da un libro e convertirlo in diversi formati di immagine. Questo articolo spiega come convertire un foglio di lavoro in diversi formati di immagine.

{{% /alert %}} 
## **Conversione del foglio di lavoro in immagine**
I fogli di lavoro contengono dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti aver bisogno di presentare i fogli di lavoro come immagini. Ad esempio, potresti aver bisogno di utilizzare un'immagine di un foglio di lavoro in un'applicazione o una pagina web. Potresti voler inserire un'immagine in un documento di Microsoft Word, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, desideri un foglio di lavoro reso come immagine in modo che tu possa usarlo altrove.

Aspose.Cells supporta la conversione dei fogli di lavoro di Excel in immagini. Per utilizzare questa funzione, è necessario importare il namespace [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) nel proprio programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) e altre.

La classe `Aspose.Cells.Rendering.ISheetRender` rappresenta un foglio di lavoro da rendere come immagini. Ha un metodo sovraccaricato, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), che può convertire un foglio di lavoro in file immagine con diversi attributi o opzioni. Sono supportati diversi formati di immagine, ad esempio, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine.
### **Formato PNG**
Si prega di consultare il seguente codice di esempio, il [file di Excel di esempio](67338402.xlsx), e le [immagini PNG di output](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **Formato TIFF**
Si prega di consultare il seguente codice di esempio, il [file di Excel di esempio](67338402.xlsx), e l'[immagine TIFF di output](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **Conversione del foglio di lavoro in SVG**
SVG sta per Scalable Vector Graphics. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for C++ è stato in grado di convertire i fogli di lavoro in immagini SVG dalla versione 18.5.0 in poi.

Per utilizzare questa funzionalità, importare lo spazio dei nomi `Aspose.Cells.Rendering` nel proprio programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio, `ISheetRender`, `IImageOrPrintOptions`, e altre.

La classe `Aspose.Cells.Rendering.IImageOrPrintOptions` specifica che il foglio di lavoro sarà salvato nel formato SVG. Il seguente snippet di codice mostra come convertire un foglio di lavoro in un file immagine SVG di Excel

Si prega di vedere il seguente codice di esempio, il [file di Excel di esempio](67338402.xlsx), e le [immagini SVG di output](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}

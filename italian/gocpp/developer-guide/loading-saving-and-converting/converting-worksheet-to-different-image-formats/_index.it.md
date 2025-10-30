---
title: Conversione del foglio di lavoro in diversi formati di immagine
type: docs
weight: 90
url: /it/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells consente di esportare un foglio di lavoro da un libro e convertirlo in diversi formati di immagine. Questo articolo spiega come convertire un foglio di lavoro in diversi formati di immagine.

{{% /alert %}}

## **Conversione del foglio di lavoro in immagine**

I fogli di lavoro contengono dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti aver bisogno di presentare i fogli di lavoro come immagini. Ad esempio, potresti aver bisogno di usare un’immagine di un foglio di lavoro in un’applicazione o pagina web. Potresti voler inserire un’immagine in un documento Microsoft Word, un file PDF, una presentazione PowerPoint o altri tipi di documenti. In breve, desideri che un foglio di lavoro venga rappresentato come immagine in modo da poterlo utilizzare altrove.

Aspose.Cells supporta la conversione di fogli di lavoro Excel in immagini. Per utilizzare questa funzionalità, devi importare lo spazio dei nomi [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) nel tuo programma o progetto. Esso contiene varie classi utili per rendering e stampa, ad esempio, [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) e altre.

La classe `Aspose.Cells.Rendering.ISheetRender` rappresenta un foglio di lavoro da rendere come immagini. Ha un metodo sovraccaricato, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), che può convertire un foglio di lavoro in uno o più file immagine con attributi o opzioni diversi. Sono supportati vari formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF e EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine.

### **convertire Excel/foglio di calcolo in PNG con GoLang**

Si prega di consultare il seguente codice di esempio, il [file di Excel di esempio](67338402.xlsx), e le [immagini PNG di output](67338401.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **convertire Excel/foglio di calcolo in TIFF con GoLang**

Si prega di consultare il seguente codice di esempio, il [file di Excel di esempio](67338402.xlsx), e l'[immagine TIFF di output](67338419.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **convertire Excel/foglio di calcolo in SVG con GoLang**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG sta per Scalable Vector Graphics. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for Go via C++ è stato in grado di convertire i fogli di lavoro in immagini SVG dalla versione 24.12.0.

Per utilizzare questa funzionalità, importare lo spazio dei nomi `Aspose.Cells.Rendering` nel proprio programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio, `ISheetRender`, `IImageOrPrintOptions`, e altre.

La classe `Aspose.Cells.Rendering.IImageOrPrintOptions` specifica che il foglio di lavoro sarà salvato nel formato SVG. Il seguente snippet di codice mostra come convertire un foglio di lavoro in un file immagine SVG di Excel

Si prega di vedere il seguente codice di esempio, il [file di Excel di esempio](67338402.xlsx), e le [immagini SVG di output](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}

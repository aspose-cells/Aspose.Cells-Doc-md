---
title: Anteprima di stampa della cartella di lavoro e del foglio di lavoro
type: docs
weight: 130
url: /it/java/workbook-and-worksheet-print-preview/
---
## **Scenario di utilizzo**

Potrebbero esserci casi in cui i file Excel con milioni di pagine devono essere convertiti in PDF o immagini. L'elaborazione di tali file richiederà molto tempo e risorse. In questi casi, la funzione Anteprima di stampa della cartella di lavoro e del foglio di lavoro potrebbe rivelarsi utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e quindi decidere se il file deve essere convertito o meno. Questo articolo si concentra sull'utilizzo di[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)e[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classi per scoprire il numero totale di pagine.

## **Anteprima di stampa della cartella di lavoro e del foglio di lavoro**

Aspose.Cells fornisce la funzione di anteprima di stampa. Per questo, lo API fornisce[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)e[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classi. Per creare l'anteprima di stampa dell'intera cartella di lavoro, creare un'istanza di[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)classe passando[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)e[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)oggetti al costruttore. Il[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)la classe fornisce un[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)metodo che restituisce il numero di pagine nell'anteprima generata. Simile a[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)classe, il[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)class viene utilizzata per generare un'anteprima di stampa per un foglio di lavoro specifico. Per creare l'anteprima di stampa di un foglio di lavoro, creare un'istanza di[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classe passando[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)e[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)oggetti al costruttore. Il[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)class fornisce anche un[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)metodo che restituisce il numero di pagine nell'anteprima generata.

Il seguente frammento di codice illustra l'uso di entrambi[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)e[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)classi utilizzando il[file excel di esempio](Book1.xlsx).

### **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Di seguito è riportato l'output generato dall'esecuzione del codice precedente.

### **Uscita console**

Numero di pagine della cartella di lavoro: 1</br>
Numero di pagine del foglio di lavoro: 1

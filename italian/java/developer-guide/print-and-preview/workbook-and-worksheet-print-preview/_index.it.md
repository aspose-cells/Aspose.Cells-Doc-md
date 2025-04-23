---
title: Anteprima di stampa di Workbook e Foglio di lavoro
type: docs
weight: 130
url: /it/java/workbook-and-worksheet-print-preview/
---

## **Scenario di Utilizzo**

Potrebbero esserci casi in cui è necessario convertire file Excel con milioni di pagine in PDF o immagini. Elaborare tali file consumerebbe molto tempo e risorse. In casi del genere, la funzionalità Anteprima di stampa di Workbook e Foglio di lavoro potrebbe risultare utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e quindi decidere se convertire o meno il file. Questo articolo si concentra sull'utilizzo delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)per scoprire il numero totale di pagine.

## **Anteprima di stampa di Workbook e Foglio di lavoro**

Aspose.Cells fornisce la funzione anteprima di stampa. A questo scopo, l'API fornisce le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview). Per creare l'anteprima di stampa dell'intero cartella di lavoro, crea un'istanza della classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) passando gli oggetti di [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) al costruttore. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) fornisce un metodo [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount) che restituisce il numero di pagine nell'anteprima generata. Similmente alla classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) è utilizzata per generare un'anteprima di stampa per un foglio di lavoro specifico. Per creare l'anteprima di stampa di un foglio di lavoro, crea un'istanza della classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) passando gli oggetti di [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) al costruttore. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) fornisce anche un metodo [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount) che restituisce il numero di pagine nell'anteprima generata.

Il seguente frammento di codice dimostra l'uso delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) utilizzando il file excel di esempio (Book1.xlsx).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Quello che segue è l'output generato eseguendo il codice sopra.

### **Output della console**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

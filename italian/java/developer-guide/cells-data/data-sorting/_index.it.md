---
title: Ordinamento dei dati
type: docs
weight: 90
url: /it/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

L'ordinamento dei dati è una delle tante utili funzionalità di Microsoft Excel. Consente agli utenti di ordinare i dati per renderli più facili da esaminare.

Aspose.Cells consente di ordinare i dati del foglio di lavoro in modo alfabetico o numerico. Funziona allo stesso modo di Microsoft Excel per ordinare i dati.

{{% /alert %}}

## **Ordinare i dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1. Seleziona **Dati** dal menu **Ordina**.
   Viene visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco - definito come un gruppo contiguo di dati in cui i dati sono visualizzati in colonne.

**La finestra di dialogo Ordina in Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **Ordinare i dati con Aspose.Cells**

Aspose.Cells fornisce la classe [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) utilizzata per ordinare i dati in ordine crescente o decrescente. La classe ha alcuni membri importanti, ad esempio, metodi come [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) e [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). Questi membri vengono utilizzati per definire le chiavi di ordinamento e specificare l'ordine di ordinamento delle chiavi.

È necessario definire le chiavi e impostare l'ordine di ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il metodo [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

Il metodo [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) accetta i seguenti parametri:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), le celle del foglio di lavoro.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), l'intervallo di celle. Definire l'area delle celle prima di applicare l'ordinamento dei dati.

Questo esempio mostra come ordinare i dati utilizzando l'API Aspose.Cells. L'esempio utilizza un file di modello "Book1.xls" e ordina i dati per l'intervallo dati (A1:B14) nel primo foglio di lavoro:

Questo esempio utilizza il file di modello "Book1.xls" creato in Microsoft Excel.

**Modello di file Excel completo di dati**

![todo:image_alt_text](data-sorting_2.png)

Dopo aver eseguito il codice sottostante, i dati vengono ordinati correttamente come puoi vedere dal file di output Excel.

**File Excel di output dopo l'ordinamento dei dati**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

Per ordinare *da sinistra a destra*, utilizza l'attributo [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight).

{{% /alert %}}

## **Ordinamento dati con il colore di sfondo**

Excel fornisce la funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzionalità è fornita utilizzando Aspose.Cells utilizzando [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) dove [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) può essere utilizzato in [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato nella [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), funzione vengono posizionate in cima o in fondo in base all'impostazione dell'Ordine di ordinamento e l'ordine delle restanti celle non viene affatto modificato.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Argomenti avanzati**
- [Ordina dati nella colonna con elenco di ordinamenti personalizzati](/cells/it/java/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/java/specifying-sort-warning-while-sorting-data/)


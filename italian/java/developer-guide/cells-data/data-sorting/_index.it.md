---
title: Ordinamento dei dati
type: docs
weight: 90
url: /it/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

L'ordinamento dei dati è una delle tante funzioni utili di Microsoft Excel. Consente agli utenti di ordinare i dati per semplificare la scansione.

Aspose.Cells consente di ordinare i dati del foglio di lavoro in ordine alfabetico o numerico. Funziona allo stesso modo di Microsoft Excel per ordinare i dati.

{{% /alert %}}

## **Ordinamento dei dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1.  Selezionare**Dati** dal**Ordinare** menù.
 Viene visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco, definito come un gruppo contiguo di dati in cui i dati vengono visualizzati in colonne.

**La finestra di dialogo Ordina in Microsoft Excel**

![cose da fare:immagine_alt_testo](data-sorting_1.png)

## **Ordinamento dati con Aspose.Cells**

 Aspose.Cells fornisce il[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) classe utilizzata per ordinare i dati in ordine crescente o decrescente. La classe ha alcuni membri importanti, ad esempio metodi come[**impostaChiave1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**impostaChiave2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) e[**setOrdine1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrdine2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Questi membri vengono utilizzati per definire le chiavi ordinate e specificare l'ordinamento delle chiavi.

 È necessario definire le chiavi e impostare l'ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il[**ordinare**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

 Il[**ordinare**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) accetta i seguenti parametri:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), le celle del foglio di lavoro.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), l'intervallo di celle. Definire l'area della cella prima di applicare l'ordinamento dei dati.

Questo esempio mostra come ordinare i dati utilizzando Aspose.Cells API. L'esempio utilizza un file modello "Book1.xls" e ordina i dati per l'intervallo di dati (A1:B14) nel primo foglio di lavoro:

Questo esempio utilizza il file modello "Book1.xls" creato in Microsoft Excel.

**Modello di file Excel completo di dati**

![cose da fare:immagine_alt_testo](data-sorting_2.png)

Dopo aver eseguito il codice seguente, i dati vengono ordinati in modo appropriato, come puoi vedere dal file Excel di output.

**File Excel di output dopo l'ordinamento dei dati**

![cose da fare:immagine_alt_testo](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Ordinare*Da sinistra a destra* , utilizzare il[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) attributo.

{{% /alert %}}

## **Ordinamento dei dati con il colore di sfondo**

 Excel fornisce la funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzione è fornita utilizzando Aspose.Cells utilizzando[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) dove[**OrdinaSuTipo.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) può essere utilizzato in[**aggiungichiave()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato nel file[**aggiungichiave()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), la funzione viene posizionata in alto o in basso in base all'impostazione SortOrder e l'ordine del resto delle celle non viene modificato affatto.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzione:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Argomenti avanzati**
- [Ordina i dati nella colonna con l'elenco di ordinamento personalizzato](/cells/it/java/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/java/specifying-sort-warning-while-sorting-data/)


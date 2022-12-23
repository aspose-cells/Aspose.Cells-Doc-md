---
title: Ordinamento dei dati
type: docs
weight: 130
url: /it/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

L'ordinamento dei dati è una delle tante funzioni utili di Microsoft Excel. Consente agli utenti di ordinare i dati per semplificare la scansione. Aspose.Cells consente agli sviluppatori di ordinare i dati del foglio di lavoro in ordine alfabetico o numerico che funziona allo stesso modo di Microsoft Excel per ordinare i dati.

{{% /alert %}}

## **Ordinamento dei dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1.  Selezionare**Dati** dal**Ordinare** menù. Verrà visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco, definito come un gruppo contiguo di dati in cui i dati vengono visualizzati in colonne.

## **Ordinamento dati con Aspose.Cells**

 Aspose.Cells fornisce il[**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)classe utilizzata per ordinare i dati in ordine crescente o decrescente. La classe ha alcuni membri importanti, ad esempio proprietà come Key1 ... Key3 e Order1 ... Order3. Questi membri vengono utilizzati per definire le chiavi ordinate e specificare l'ordinamento delle chiavi.

 È necessario definire le chiavi e impostare l'ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il[**Ordinare**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)metodo utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

 Il[**Ordinare**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)metodo accetta i seguenti parametri:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), le celle per il foglio di lavoro sottostante.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), l'intervallo di celle. Definire l'area della cella prima di applicare l'ordinamento dei dati.

Questo esempio utilizza il file modello "Book1.xls" creato in Microsoft Excel. Dopo aver eseguito il codice seguente, i dati vengono ordinati in modo appropriato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Se vuoi ordinare*Da sinistra a destra* , Usa il[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) attributo.

{{% /alert %}}

### **Ordinamento dei dati con il colore di sfondo**

 Excel fornisce funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzionalità viene fornita utilizzando Aspose.Cells utilizzando DataSorter where[**OrdinaSuTipo**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor può essere utilizzato in[**Aggiungichiave()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato nel file[**Aggiungichiave()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), la funzione viene posizionata in alto o in basso in base all'impostazione SortOrder e l'ordine del resto delle celle non viene modificato affatto.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzione:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Argomenti avanzati**
- [Ordina i dati nella colonna con l'elenco di ordinamento personalizzato](/cells/it/net/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/net/specifying-sort-warning-while-sorting-data/)

---
title: Ordinamento dei dati
type: docs
weight: 130
url: /it/nodejs-cpp/sort-data-of-excel/
description: Impara come ordinare i dati utilizzando l API Aspose.Cells for Node.js via C++.
keywords: Ordina i dati in ordine ascendente o discendente, ordina i dati in base al colore di sfondo.
---

{{% alert color="primary" %}}

L'ordinamento dei dati è una delle molte utili funzioni di Microsoft Excel. Consente agli utenti di ordinare i dati per facilitarne la scansione. Aspose.Cells for Node.js via C++ permette agli sviluppatori di ordinare i dati del foglio di lavoro alfabeticamente o numericamente, funzionando allo stesso modo in cui Excel ordina i dati.

{{% /alert %}}

## **Ordinare i dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1. Seleziona **Dati** dal menu **Ordina**. Verrà visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco - definito come un gruppo contiguo di dati in cui i dati sono visualizzati in colonne.

## **Ordinare i dati con Aspose.Cells**

Aspose.Cells for Node.js via C++ fornisce la classe [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) usata per ordinare i dati in ordine crescente o decrescente. La classe ha alcuni membri importanti, ad esempio, proprietà come Key1 ... Key3 e Order1 ... Order3. Questi membri vengono usati per definire le chiavi ordinate e specificare l'ordine di ordinamento delle chiavi.

È necessario definire le chiavi e impostare l'ordine di ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il metodo [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

Il metodo [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) accetta i seguenti parametri:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), le celle per il foglio di lavoro sottostante.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), l'intervallo di celle. Definire l'area delle celle prima di applicare l'ordinamento dei dati.

Questo esempio utilizza il file di modello "Book1.xls" creato in Microsoft Excel. Dopo l'esecuzione del codice seguente, i dati vengono ordinati in modo appropriato.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

Se si desidera ordinare *DaSinistraADestra*, utilizzare l'attributo [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-).

{{% /alert %}}

### **Ordinamento dati con il colore di sfondo**

Excel fornisce funzioni per ordinare i dati basandosi sul colore di sfondo. La stessa funzione è disponibile anche tramite Aspose.Cells for Node.js via C++ usando DataSorter, dove [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor può essere usato in [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato in [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-), funzione, vengono posizionate in alto o in basso secondo l'impostazione SortOrder e l'ordine delle restanti celle non viene modificato.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Argomenti avanzati**
- [Ordina dati nella colonna con elenco di ordinamenti personalizzati](/cells/it/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="nodejs-cpp" >}}

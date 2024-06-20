---
title: Ordina i dati in una colonna con un elenco di ordinamento personalizzato
type: docs
weight: 210
url: /it/java/sort-data-in-column-with-custom-sort-list/
---

## **Possibili Scenari di Utilizzo**

Puoi ordinare i dati nella colonna utilizzando un elenco personalizzato. Ciò può essere fatto utilizzando il metodo [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)). Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non contengono virgole al loro interno. Se contengono virgole come "USA, US", "Cina, CN" ecc., allora è necessario utilizzare il metodo [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)). Qui, l'ultimo parametro non è una Stringa ma un Array di Stringhe.

## **Ordina dati nella colonna con elenco di ordinamenti personalizzati**

Il seguente codice di esempio spiega come utilizzare il metodo DataSorter.AddKey(int key, SortOrder order, String[] customList) per ordinare i dati con un elenco di ordinamento personalizzato. Consultare il [file Excel di esempio](50528359.xlsx) utilizzato in questo codice e il [file Excel di output](50528358.xlsx) generato da esso. La schermata seguente mostra l'effetto del codice sul file Excel di esempio in esecuzione.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}

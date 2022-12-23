---
title: Ordina i dati nella colonna con l'elenco di ordinamento personalizzato
type: docs
weight: 210
url: /it/java/sort-data-in-column-with-custom-sort-list/
---
## **Possibili scenari di utilizzo**

Puoi ordinare i dati nella colonna utilizzando un elenco personalizzato. Questo può essere fatto usando[DataSorter.AddKey(chiave int, ordine SortOrder, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) metodo. Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non contengono virgole. Se hanno virgole come "USA, US", "China, CN" ecc., devi usarle[DataSorter.AddKey(chiave int, ordine SortOrder, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) metodo. Qui, l'ultimo parametro non è String ma un array di stringhe.

## **Ordina i dati nella colonna con l'elenco di ordinamento personalizzato**

Il codice di esempio seguente spiega come usare il metodo DataSorter.AddKey(int key, SortOrder order, String[]customList) per ordinare i dati con un elenco di ordinamento personalizzato. Si prega di consultare il[esempio di file Excel](50528359.xlsx)utilizzato in questo codice e[file Excel di output](50528358.xlsx)generato da esso. Lo screenshot seguente mostra l'effetto del codice sul file Excel di esempio durante l'esecuzione.

![cose da fare:immagine_alt_testo](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}

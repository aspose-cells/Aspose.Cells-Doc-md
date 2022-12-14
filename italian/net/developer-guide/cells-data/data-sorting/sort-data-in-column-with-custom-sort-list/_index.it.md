---
title: Ordina i dati nella colonna con l'elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/net/sort-data-in-column-with-custom-sort-list/
---
## **Possibili scenari di utilizzo**

 Puoi ordinare i dati nella colonna utilizzando un elenco personalizzato. Questo può essere fatto usando[**DataSorter.AddKey(chiave int, ordine SortOrder, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)metodo. Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non contengono virgole. Se hanno virgole come "USA,US", "China,CN" ecc., devi usare [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Qui, l'ultimo parametro non è String ma un array di stringhe.

## **Ordina i dati nella colonna con l'elenco di ordinamento personalizzato**

Il seguente codice di esempio spiega come utilizzare [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) metodo per ordinare i dati con un elenco di ordinamento personalizzato. Consulta il [file Excel di esempio](50528327.xlsx) utilizzato in questo codice e il [file Excel di output](50528328.xlsx) da esso generato. Lo screenshot seguente mostra l'effetto del codice sul file Excel di esempio durante l'esecuzione.

![cose da fare:immagine_alt_testo](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}

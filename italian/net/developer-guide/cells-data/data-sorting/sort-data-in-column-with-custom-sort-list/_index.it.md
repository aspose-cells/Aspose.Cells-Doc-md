---
title: Ordina i dati nella colonna con l'elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/net/sort-data-in-column-with-custom-sort-list/
description: Scopri come ordinare i dati nella colonna utilizzando un elenco personalizzato utilizzando Aspose.Cells for .NET API.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Possibili scenari di utilizzo**

 È possibile ordinare i dati nella colonna utilizzando un elenco personalizzato. Questo può essere fatto utilizzando[**DataSorter.AddKey(chiave int, ordine SortOrder, stringa customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)metodo. Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non contengono virgole al loro interno. Se contengono virgole come "USA,US", "China,CN" ecc., è necessario utilizzare il [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) metodo. Qui, l'ultimo parametro non è String ma un Array of Strings.

##  **Ordina i dati nella colonna con l'elenco di ordinamento personalizzato**

Il seguente codice di esempio spiega come utilizzare il [**Metodo DataSorter.AddKey (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) metodo per ordinare i dati con un elenco di ordinamento personalizzato. Si prega di consultare il[file Excel di esempio](50528327.xlsx) utilizzato in questo codice e[file Excel di output](50528328.xlsx) da esso generato. La schermata seguente mostra l'effetto del codice sul file Excel di esempio durante l'esecuzione.

![cose da fare:immagine_alt_testo](sort-data-in-column-with-custom-sort-list_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}

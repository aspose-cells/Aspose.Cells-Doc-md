---
title: Ordina i dati in una colonna con un elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/net/sort-data-in-column-with-custom-sort-list/
description: Scopri come ordinare i dati nella colonna utilizzando un elenco personalizzato utilizzando l API Aspose.Cells for .NET.
keywords: Ordina i dati nella colonna con un elenco di ordinamento personalizzato, Ordina i dati per elenco personalizzato.
---

## **Possibili Scenari di Utilizzo**

Puoi ordinare i dati nella colonna utilizzando un elenco personalizzato. Questo può essere fatto utilizzando il metodo [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2). Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non hanno virgole al loro interno. Se hanno virgole come "USA,US", "Cina,CN" ecc., allora è necessario utilizzare il metodo [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Qui, l'ultimo parametro non è String ma un Array di Stringhe.

## **Ordina dati nella colonna con elenco di ordinamenti personalizzati**

Il codice di esempio seguente spiega come utilizzare il metodo [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) per ordinare i dati con un elenco di ordinamento personalizzato. Si prega di consultare il [file di esempio Excel](50528327.xlsx) utilizzato in questo codice e il [file Excel di output](50528328.xlsx) generato da esso. La seguente schermata mostra l'effetto del codice sul file di esempio Excel all'esecuzione.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}

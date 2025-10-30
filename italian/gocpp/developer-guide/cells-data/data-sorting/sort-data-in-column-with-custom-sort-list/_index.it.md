---
title: Ordina i dati nella colonna con elenco di ordinamento personalizzato con Golang tramite C++
linktitle: Ordina i dati in una colonna con un elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Scopri come ordinare i dati nella colonna usando un elenco personalizzato con l API Aspose.Cells for C++.
keywords: Ordina i dati nella colonna con un elenco di ordinamento personalizzato, Ordina i dati per elenco personalizzato.
---

## **Possibili Scenari di Utilizzo**

Puoi ordinare i dati nella colonna usando un elenco personalizzato. Questo può essere fatto usando il metodo [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non contengono virgole. Se contengono virgole come "USA,US", "Cina,CN" ecc., allora devi usare il metodo [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Qui, l'ultimo parametro non è una String ma un Array di Stringhe.

## **Ordina dati nella colonna con elenco di ordinamenti personalizzati**

Il seguente esempio di codice spiega come utilizzare il metodo [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) per ordinare i dati con un elenco di ordinamento personalizzato. Si prega di vedere il [file Excel di esempio](50528327.xlsx) usato in questo codice e il [file Excel di output](50528328.xlsx) generato da esso. La seguente schermata mostra l'effetto del codice sul file Excel di esempio all'esecuzione.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}

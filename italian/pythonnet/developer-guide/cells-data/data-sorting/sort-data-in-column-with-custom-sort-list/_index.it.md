---
title: Ordina i dati in una colonna con un elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/python-net/sort-data-in-column-with-custom-sort-list/
description: Scopri come ordinare i dati nella colonna utilizzando un elenco personalizzato utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Ordina i dati in colonna con elenco di ordinamento personalizzato Python, Ordina i dati per elenco personalizzato Python.
---

## **Possibili Scenari di Utilizzo**

È possibile ordinare i dati nella colonna utilizzando un elenco personalizzato. Questo può essere fatto utilizzando il metodo [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non hanno virgole all'interno. Se hanno virgole come "USA,US", "Cina,CN" ecc., allora è necessario utilizzare il metodo [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Qui, l'ultimo parametro non è una Stringa ma un Array di Stringhe.

## **Ordina dati nella colonna con elenco di ordinamenti personalizzati**

Il seguente codice di esempio spiega come utilizzare il metodo [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) per ordinare i dati con un elenco di ordinamento personalizzato. Si prega di vedere il [file Excel di esempio](50528327.xlsx) utilizzato in questo codice e il [file Excel di output](50528328.xlsx) generato da esso. La seguente schermata mostra l'effetto del codice sul file Excel di esempio all'esecuzione.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}

---
title: Ordina i dati in una colonna con un elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Impara come ordinare i dati in una colonna usando una lista personalizzata tramite l’API Aspose.Cells for Node.js via C++.
keywords: Ordina i dati nella colonna con un elenco di ordinamento personalizzato, Ordina i dati per elenco personalizzato.
---

## **Possibili Scenari di Utilizzo**

Puoi ordinare i dati in una colonna usando una lista personalizzata. Questo può essere fatto usando il metodo [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-). Tuttavia, questo metodo funziona solo se gli elementi nella lista personalizzata non contengono virgole al suo interno. Se hanno virgole come "USA,US", "Cina,CN" ecc., allora devi usare il metodo [**DataSorter.addKey(numero, ordinamento, string[]**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-). Qui, l'ultimo parametro non è una String ma un Array di String.

## **Ordina dati nella colonna con elenco di ordinamenti personalizzati**

Il seguente esempio di codice spiega come usare il metodo [**DataSorter.addKey(numero, ordinamento, string[]**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) per ordinare i dati con una lista di ordinamento personalizzata. Vedi il [file Excel di esempio](50528327.xlsx) usato in questo codice e il [file Excel di output](50528328.xlsx) generato. La schermata seguente mostra l'effetto del codice sul file Excel di esempio durante l'esecuzione.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

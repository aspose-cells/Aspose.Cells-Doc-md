---
title: Propagare la formula in un entità tabella o elenco automaticamente durante l inserimento dei dati in nuove righe
linktitle: Imposta la formula tabella
type: docs
weight: 260
url: /it/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Possibili Scenari di Utilizzo**
A volte si desidera che una formula nella propria tabella o oggetto elenco si propaghi automaticamente alle nuove righe durante l'inserimento di nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere lo stesso risultato con Aspose.Cells, utilizzare la proprietà [ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula).
## **Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe**
Il seguente codice di esempio crea un'entità tabella o un oggetto elenco in modo che la formula nella colonna B si propaghi automaticamente alle nuove righe quando si inseriscono nuovi dati. Si prega di controllare il [file Excel di output](5115469.xlsx) generato con questo codice. Se si inserisce un numero in cella A3, si vedrà che la formula nella cella B2 si propaga automaticamente alla cella B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}

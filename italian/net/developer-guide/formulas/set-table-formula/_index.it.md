---
title: Propaga automaticamente la formula nella tabella o nell'oggetto elenco durante l'inserimento dei dati in nuove righe
linktitle: Imposta la formula della tabella
type: docs
weight: 260
url: /it/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Possibili scenari di utilizzo**
 A volte, si desidera che una formula nella tabella o nell'oggetto elenco si propaghi automaticamente a nuove righe durante l'inserimento di nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere la stessa cosa con Aspose.Cells, si prega di utilizzare[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)proprietà.
## **Propaga automaticamente la formula nella tabella o nell'oggetto elenco durante l'inserimento dei dati in nuove righe**
Il seguente codice di esempio crea una tabella o un oggetto elenco in modo tale che la formula nella colonna B si propaghi automaticamente alle nuove righe quando si immettono nuovi dati. Si prega di controllare[file excel di output](5115469.xlsx) generato con questo codice. Se inserisci un numero qualsiasi nella cella A3, vedrai che la formula nella cella B2 si propaga automaticamente alla cella B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}

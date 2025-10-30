---
title: Propagare la formula in un entità tabella o elenco automaticamente durante l inserimento dei dati in nuove righe
linktitle: Imposta la formula tabella
type: docs
weight: 260
url: /it/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Possibili Scenari di Utilizzo**
A volte, si desidera che una formula nel proprio Tavolo o Oggetto Lista venga automaticamente propagata alle nuove righe durante l'inserimento di nuovi dati. Questo è il funzionamento predefinito di Microsoft Excel. Per ottenere lo stesso con Aspose.Cells for Python via .NET, si prega di usare la proprietà [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula).

## **Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe**
Il seguente codice di esempio crea un'entità tabella o un oggetto elenco in modo che la formula nella colonna B si propaghi automaticamente alle nuove righe quando si inseriscono nuovi dati. Si prega di controllare il [file Excel di output](5115469.xlsx) generato con questo codice. Se si inserisce un numero in cella A3, si vedrà che la formula nella cella B2 si propaga automaticamente alla cella B3.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

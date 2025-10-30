---
title: Elimina la tabella pivot da un foglio di lavoro con Golang tramite C++
linktitle: Elimina Pivot Table
type: docs
weight: 60
url: /it/go-cpp/delete-pivot-table-from-a-worksheet/
description: Codice C++ per rimuovere PivotTable dai Fogli di Lavoro Excel usando Aspose.Cells.
keywords: c++ rimuovi pivot table dal foglio di lavoro, c++ rimuovi pivot table da excel, come eliminare pivot table con c++, elimina pivot table con c++, elimina pivot table da excel con c++, c++ cancella pivot table, c++ rimuovi pivot table, rimuovi pivot table, elimina pivot table, come eliminare pivot table
---

{{% alert color="primary" %}}

Aspose.Cells fornisce una funzionalità per eliminare o rimuovere la tabella pivot da un foglio di lavoro. Puoi eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di utilizzare il metodo [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e il metodo [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) per eliminare l'oggetto tabella pivot utilizzando la sua posizione all'interno della collezione delle tabelle pivot.

{{% /alert %}}

Il seguente esempio di codice elimina due pivot table dal foglio di lavoro. Per primo elimina la pivot table usando il metodo [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) e poi utilizza il metodo [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}

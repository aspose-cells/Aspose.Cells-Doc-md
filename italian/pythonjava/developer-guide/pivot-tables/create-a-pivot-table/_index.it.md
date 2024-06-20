---
title: Crea una tabella pivot
type: docs
weight: 10
url: /it/python-java/create-a-pivot-table/
---

## **Crea una tabella pivot**
Aspose.Cells per Python via Java fornisce la funzione per creare tabelle pivot. Per creare una tabella pivot utilizzando Aspose.Cells, segui i passaggi seguenti:

1. Aggiungi alcuni dati alle celle del foglio di lavoro utilizzando la proprietà [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value) dell'oggetto [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell). Questi dati saranno utilizzati come origine dati per la tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) dell'oggetto [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) incapsulato nell'oggetto [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet).
1. Accedi all'oggetto [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) dalla [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) passando l'indice del [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable).
1. Utilizza uno qualsiasi degli oggetti tabella pivot (spiegati sopra) incapsulati nell'oggetto [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) per gestire la tabella pivot.

Il seguente frammento di codice dimostra la creazione di una tabella pivot con l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}

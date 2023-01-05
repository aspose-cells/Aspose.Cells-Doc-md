---
title: Crea una tabella pivot
type: docs
weight: 10
url: /it/python-java/create-a-pivot-table/
---
## **Crea una tabella pivot**
Aspose.Cells for Python via Java fornisce la funzione per creare tabelle pivot. Per creare una tabella pivot utilizzando Aspose.Cells, procedi nel seguente modo:

1. Aggiungi alcuni dati alle celle del foglio di lavoro utilizzando il file[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)dell'oggetto[valore impostato](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)proprietà. Questi dati verranno utilizzati come origine dati per la tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo[Raccolta di tabelle pivot](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[Inserisci](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)metodo, incapsulato nel file[Foglio di lavoro](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)oggetto.
1. Accedi al[Tabella pivot](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)oggetto dal[Raccolta di tabelle pivot](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)passando il[Tabella pivot](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)indice.
1. Utilizzare uno qualsiasi degli oggetti tabella pivot (spiegati sopra) incapsulati nel file[Raccolta di tabelle pivot](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)oggetto per gestire la tabella pivot.

Il seguente frammento di codice illustra la creazione di una tabella pivot con Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}

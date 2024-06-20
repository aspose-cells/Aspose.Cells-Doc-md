---
title: Elimina la tabella pivot da un foglio di lavoro
type: docs
weight: 60
url: /it/net/delete-pivot-table-from-a-worksheet/
description: Codice C# per rimuovere le tabelle pivot dai fogli di calcolo di Excel
keywords: c# rimuovere tabella pivot dal foglio di lavoro, c# rimuovere tabella pivot da excel, come eliminare la tabella pivot con c#, eliminare la tabella pivot con c#, eliminare la tabella pivot da excel con c#, c# eliminare tabella pivot, c# rimuovere tabella pivot, rimuovere tabella pivot, eliminare tabella pivot, come eliminare la tabella pivot
---

{{% alert color="primary" %}}

Aspose.Cells fornisce una funzionalità per eliminare o rimuovere la tabella pivot da un foglio di lavoro. Puoi eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di utilizzare il metodo [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e il metodo [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) per eliminare l'oggetto tabella pivot utilizzando la sua posizione all'interno della collezione delle tabelle pivot.

{{% /alert %}}

Il codice di esempio seguente elimina due tabelle pivot dal foglio di lavoro. Prima rimuove la tabella pivot utilizzando il metodo [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) e poi rimuove la tabella pivot utilizzando il metodo [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}

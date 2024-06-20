---
title: Elimina la tabella pivot da un foglio di lavoro
type: docs
weight: 60
url: /it/python-net/delete-pivot-table-from-a-worksheet/
description: Codice Python via .NET per rimuovere la tabella pivot dai fogli di lavoro di Excel
keywords: Aspose.Cells for Python Excel, libreria Excel Python, Python via .NET rimuovi tabella pivot dal foglio di lavoro, Python via .NET rimuovi tabella pivot da Excel, come eliminare la tabella pivot con Python via .NET, elimina tabella pivot con Python via .NET, elimina tabella pivot da Excel con Python via .NET, Python via .NET elimina tabella pivot, Python via .NET rimuovi tabella pivot, rimuovi tabella pivot, elimina tabella pivot, come eliminare la tabella pivot
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fornisce una funzione per eliminare o rimuovere la tabella pivot da un foglio di lavoro. È possibile eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di utilizzare il metodo [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e il metodo [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) per eliminare l'oggetto tabella pivot utilizzando la sua posizione all'interno della raccolta tabella pivot.

{{% /alert %}}

## **Come eliminare la tabella pivot dal foglio di lavoro utilizzando Aspose.Cells per la libreria Excel Python**

Il codice di esempio seguente elimina due tabelle pivot dal foglio di lavoro. Prima rimuove la tabella pivot utilizzando il metodo [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) e poi rimuove la tabella pivot utilizzando il metodo [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}

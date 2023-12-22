---
title: Elimina tabella pivot da un foglio di lavoro
type: docs
weight: 60
url: /it/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET codice per rimuovere tabella pivot per fogli di lavoro Excel
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET fornisce una funzionalità per eliminare o rimuovere la tabella pivot da un foglio di lavoro. È possibile eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di utilizzare il[**Foglio di lavoro.pivot_tables.remove(tabella_pivot)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) metodo per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)metodo per eliminare l'oggetto della tabella pivot utilizzando la sua posizione all'interno della raccolta di tabelle pivot.

{{% /alert %}}

 Il codice di esempio seguente elimina due tabelle pivot dal foglio di lavoro. Innanzitutto rimuove la tabella pivot utilizzando[**Foglio di lavoro.pivot_tables.remove(tabella_pivot)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) metodo e quindi rimuove la tabella pivot utilizzando[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) metodo

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}

---
title: Elimina la tabella pivot da un foglio di lavoro
type: docs
weight: 60
url: /it/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Codice Aspose.Cells for Node.js via C++ per rimuovere le tabelle pivot da fogli di lavoro Excel
keywords: Excel Aspose.Cells for Node.js via C++, libreria Excel Node.js, rimuovere la tabella pivot dal foglio di lavoro, eliminare la tabella pivot da Excel, come eliminare la tabella pivot con Aspose.Cells for Node.js via C++, eliminare la tabella pivot, eliminare la tabella pivot da Excel, rimuovere la tabella pivot, Aspose.Cells for Node.js via C++ rimuove la tabella pivot, rimuovere la tabella pivot, eliminare la tabella pivot, come eliminare la tabella pivot
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ offre una funzione per eliminare o rimuovere la tabella pivot da un foglio di lavoro. È possibile eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la sua posizione. Si prega di usare il metodo [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e il metodo [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) per eliminarlo usando la sua posizione all'interno della collezione di tabelle pivot.

{{% /alert %}}

## **Come eliminare la tabella pivot dal foglio di lavoro usando Aspose.Cells for Node.js via C++**

Il codice di esempio seguente elimina due tabelle pivot dal foglio di lavoro. Prima rimuove la tabella pivot utilizzando il metodo [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) e poi rimuove la tabella pivot utilizzando il metodo [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}

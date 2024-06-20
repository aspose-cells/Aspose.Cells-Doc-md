---
title: Elimina la tabella pivot da un foglio di lavoro
type: docs
weight: 50
url: /it/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce una funzione per eliminare o rimuovere una tabella pivot da un foglio di lavoro. È possibile eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Utilizzare il metodo [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e il metodo [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) per eliminare un oggetto tabella pivot utilizzando la sua posizione all'interno della collezione delle tabelle pivot.

{{% /alert %}}

## **Esempio**

Il seguente esempio di codice elimina due tabelle pivot dal foglio di lavoro. Prima rimuove la tabella pivot utilizzando il metodo [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) e poi rimuove la tabella pivot utilizzando il metodo [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int))

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}

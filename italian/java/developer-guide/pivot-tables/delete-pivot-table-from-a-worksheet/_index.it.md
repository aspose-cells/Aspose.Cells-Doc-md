---
title: Elimina tabella pivot da un foglio di lavoro
type: docs
weight: 50
url: /it/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce una funzione per eliminare o rimuovere una tabella pivot da un foglio di lavoro. È possibile eliminare la tabella pivot utilizzando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di utilizzare il[**Foglio di lavoro.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) ) per eliminare la tabella pivot utilizzando l'oggetto tabella pivot e[**Foglio di lavoro.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)per eliminare un oggetto tabella pivot utilizzando la sua posizione all'interno della raccolta di tabelle pivot.

{{% /alert %}}

## **Esempio**

 Il codice di esempio seguente elimina due tabelle pivot dal foglio di lavoro. Innanzitutto, rimuove la tabella pivot utilizzando[**Foglio di lavoro.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) metodo e quindi rimuove la tabella pivot utilizzando[**Foglio di lavoro.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) metodo

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}

---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale
type: docs
weight: 50
url: /it/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Possibili Scenari di Utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come fonte dati, quindi è chiamata tabella pivot figlio o tabella pivot nidificata. È possibile trovare le tabelle pivot figlie di una tabella pivot principale utilizzando il metodo [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--).

## **Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale**

Il codice di esempio seguente carica il [file Excel di esempio](61767766.xlsx) che contiene tre tabelle pivot. Le ultime due tabelle pivot sono i figli della tabella pivot di cui sopra come mostrato in questa schermata. Il codice trova le tabelle pivot figlie utilizzando il metodo [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) e quindi le aggiorna una per volta.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}

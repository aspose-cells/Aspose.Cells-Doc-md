---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale
type: docs
weight: 60
url: /it/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Possibili Scenari di Utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come fonte dati, quindi è chiamata tabella pivot figlio o tabella pivot nidificata. È possibile trovare le tabelle pivot figlie di una tabella pivot principale utilizzando il metodo [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren).

## **Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale**

Il codice di esempio seguente carica il [file di Excel di esempio](61767747.xlsx) che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono i figli della tabella pivot soprastante come mostrato in questa schermata. Il codice trova le tabelle pivot figlie utilizzando il metodo [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) e poi le aggiorna una per volta.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
{{< app/cells/assistant language="csharp" >}}

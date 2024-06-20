---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale
type: docs
weight: 60
url: /it/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Come trovare e aggiornare le tabelle pivot nidificate o figlie della tabella pivot principale con Aspose.Cells per Python via .NET.
keywords: Aspose.Cells for Python Excel, libreria Excel Python, Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale utilizzando Aspose.Cells per la libreria Excel Python.
---

## **Possibili Scenari di Utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come fonte dati, quindi è chiamata tabella pivot figlio o tabella pivot nidificata. È possibile trovare le tabelle pivot figlie di una tabella pivot principale utilizzando il metodo [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#).

## **Come trovare e aggiornare le tabelle pivot nidificate o figlie della tabella pivot principale**

Il codice di esempio seguente carica il [file di Excel di esempio](61767747.xlsx) che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono i figli della tabella pivot soprastante come mostrato in questa schermata. Il codice trova le tabelle pivot figlie utilizzando il metodo [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) e poi le aggiorna una per volta.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}

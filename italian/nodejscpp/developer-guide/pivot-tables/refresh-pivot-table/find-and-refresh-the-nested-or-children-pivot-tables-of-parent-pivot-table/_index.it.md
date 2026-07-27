---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale
type: docs
weight: 60
url: /it/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Come trovare e aggiornare le tabelle pivot annidate o figlie della tabella pivot genitore con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells per Node.js Excel, libreria Excel Node.js, Trovare e aggiornare le tabelle pivot annidate o figlie della tabella pivot genitore utilizzando la libreria Aspose.Cells per Node.js Excel.
---

## **Possibili Scenari di Utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come fonte dati, quindi è chiamata tabella pivot figlio o tabella pivot nidificata. È possibile trovare le tabelle pivot figlie di una tabella pivot principale utilizzando il metodo [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--).

## **Come trovare e aggiornare le tabelle pivot nidificate o figlie della tabella pivot principale**

Il codice di esempio seguente carica il [file di Excel di esempio](61767747.xlsx) che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono i figli della tabella pivot soprastante come mostrato in questa schermata. Il codice trova le tabelle pivot figlie utilizzando il metodo [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) e poi le aggiorna una per volta.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

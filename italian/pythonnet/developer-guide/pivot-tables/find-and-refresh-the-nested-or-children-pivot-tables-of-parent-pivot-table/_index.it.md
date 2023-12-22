---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre
type: docs
weight: 60
url: /it/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Come trovare e aggiornare le tabelle pivot nidificate o figlie della tabella pivot padre con Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Possibili scenari di utilizzo**

volte, una tabella pivot utilizza un'altra tabella pivot come origine dati, quindi viene chiamata tabella pivot figlio o tabella pivot nidificata. Puoi trovare le tabelle pivot figlie di una tabella pivot padre utilizzando il file[**Tabella pivot.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)metodo.

##  **Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre**

 Il codice di esempio seguente carica il file[file Excel di esempio](61767747.xlsx) che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono le figlie della tabella pivot precedente, come mostrato in questo screenshot. Il codice trova la tabella pivot figlio utilizzando il file[**Tabella pivot.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)metodo e quindi aggiornarli uno per uno.

![cose da fare:immagine_alt_testo](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}

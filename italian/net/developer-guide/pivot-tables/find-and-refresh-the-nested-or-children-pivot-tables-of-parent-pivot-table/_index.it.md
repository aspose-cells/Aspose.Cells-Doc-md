---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre
type: docs
weight: 60
url: /it/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Possibili scenari di utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come origine dati, quindi viene chiamata tabella pivot figlio o tabella pivot nidificata. Puoi trovare le tabelle pivot figlie di una tabella pivot genitore utilizzando il file[**Tabella pivot.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)metodo.

## **Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre**

 Il codice di esempio seguente carica il file[esempio di file Excel](61767747.xlsx) che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono i figli della tabella pivot precedente, come mostrato in questo screenshot. Il codice trova la tabella pivot dei bambini utilizzando il file[**Tabella pivot.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)metodo e poi li aggiorna uno per uno.

![cose da fare:immagine_alt_testo](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}

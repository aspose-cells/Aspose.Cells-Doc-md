---
title: Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre
type: docs
weight: 50
url: /it/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Possibili scenari di utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come origine dati, quindi viene chiamata tabella pivot figlio o tabella pivot nidificata. Puoi trovare le tabelle pivot figlie di una tabella pivot genitore utilizzando il file[**Tabella pivot.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) metodo.

## **Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre**

Il codice di esempio seguente carica il file[esempio di file Excel](61767766.xlsx)che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono i figli della tabella pivot precedente, come mostrato in questo screenshot. Il codice trova la tabella pivot dei bambini utilizzando il file[**Tabella pivot.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) e quindi li aggiorna uno per uno.

![cose da fare:immagine_alt_testo](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}

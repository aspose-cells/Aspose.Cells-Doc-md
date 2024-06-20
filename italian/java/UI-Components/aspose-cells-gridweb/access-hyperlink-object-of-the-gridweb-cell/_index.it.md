---
title: Accesso all oggetto Iperlink dell elemento GridWeb Cell
type: docs
weight: 60
url: /it/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **Possibili Scenari di Utilizzo**
È possibile verificare se una cella contiene un collegamento ipertestuale o meno utilizzando i seguenti due metodi. Questi metodi restituiranno null se la cella non contiene un collegamento ipertestuale e, se contiene un collegamento ipertestuale, restituiranno l'oggetto GridHyperlink.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **Aprire il collegamento ipertestuale in una nuova o esistente finestra**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **Accesso all'oggetto Iperlink dell'elemento GridWeb Cell**
Il seguente codice di esempio accede all'iperlink della cella A1. Se la cella A1 contiene un collegamento ipertestuale, restituirà l'oggetto GridHyperlink, altrimenti restituirà null.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

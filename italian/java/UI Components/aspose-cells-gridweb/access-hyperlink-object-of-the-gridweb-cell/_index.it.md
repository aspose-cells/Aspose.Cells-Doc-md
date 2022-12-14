---
title: Accesso all'oggetto Hyperlink del GridWeb Cell
type: docs
weight: 60
url: /it/java/access-hyperlink-object-of-the-gridweb-cell/
---
## **Possibili scenari di utilizzo**
Puoi verificare se la cella contiene un collegamento ipertestuale o meno utilizzando i seguenti due metodi. Questi metodi restituiranno null se la cella non contiene un collegamento ipertestuale e se contiene un collegamento ipertestuale, restituirà l'oggetto GridHyperlink.

- GridHyperlinkCollection.getHyperlink(cella GridCell)
- GridHyperlinkCollection.getHyperlink(int riga,int colonna)
## **Apri collegamento ipertestuale in una finestra nuova o esistente**
 Se il tuo file excel contiene un collegamento ipertestuale che si collega ad alcuni URL come<http://wwww.aspose.com/> e lo carichi in GridWeb, i collegamenti ipertestuali verranno visualizzati con l'attributo target impostato su_ vuoto. Significa che quando fai clic sul collegamento ipertestuale in una cella di GridWeb, si aprirà in una nuova finestra anziché nella finestra esistente. Inoltre, se desideri aprire il collegamento ipertestuale nella finestra esistente, imposta GridHyperlink.Target su_se stesso.
## **Accesso all'oggetto Hyperlink del GridWeb Cell**
Il seguente codice di esempio accede al collegamento ipertestuale della cella A1. Se la cella A1 contiene un collegamento ipertestuale, restituirà l'oggetto GridHyperlink, altrimenti restituirà null.
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

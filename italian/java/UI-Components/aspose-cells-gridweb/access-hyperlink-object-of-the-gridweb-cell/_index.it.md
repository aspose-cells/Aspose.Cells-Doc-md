---
title: Accedi all'oggetto Collegamento ipertestuale di GridWeb Cell
type: docs
weight: 60
url: /it/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **Possibili scenari di utilizzo**
Puoi verificare se la cella contiene un collegamento ipertestuale o meno utilizzando i due metodi seguenti. Questi metodi restituiranno null se la cella non contiene un collegamento ipertestuale e se contiene un collegamento ipertestuale, restituirà l'oggetto GridHyperlink.

- GridHyperlinkCollection.getHyperlink(cella GridCell)
- GridHyperlinkCollection.getHyperlink(int riga,int colonna)
##  **Apri collegamento ipertestuale in una finestra nuova o esistente**
 Se il tuo file Excel contiene un collegamento ipertestuale che si collega ad alcuni URL come<http://wwww.aspose.com/> e lo carichi in GridWeb, i collegamenti ipertestuali verranno visualizzati con l'attributo target impostato su _blank. Significa che quando fai clic sul collegamento ipertestuale in una cella GridWeb, si aprirà in una nuova finestra invece della finestra esistente. Inoltre, se desideri aprire il collegamento ipertestuale nella finestra esistente, imposta GridHyperlink.Target su _self.
##  **Accedi all'oggetto Collegamento ipertestuale di GridWeb Cell**
Il seguente codice di esempio accede al collegamento ipertestuale della cella A1. Se la cella A1 contiene un collegamento ipertestuale, restituirà l'oggetto GridHyperlink, altrimenti restituirà null.
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

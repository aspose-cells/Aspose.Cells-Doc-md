---
title: Greifen Sie auf das Hyperlink-Objekt des GridWeb Cell zu
type: docs
weight: 60
url: /de/java/access-hyperlink-object-of-the-gridweb-cell/
---
## **Mögliche Nutzungsszenarien**
Sie können mit den folgenden zwei Methoden überprüfen, ob die Zelle einen Hyperlink enthält oder nicht. Diese Methoden geben null zurück, wenn die Zelle keinen Hyperlink enthält, und wenn sie einen Hyperlink enthält, wird das GridHyperlink-Objekt zurückgegeben.

- GridHyperlinkCollection.getHyperlink (GridCell-Zelle)
- GridHyperlinkCollection.getHyperlink(int Zeile,int Spalte)
## **Hyperlink in neuem oder vorhandenem Fenster öffnen**
 Wenn Ihre Excel-Datei einen Hyperlink enthält, der auf eine URL wie z<http://wwww.aspose.com/> und Sie laden es in GridWeb, dann werden die Hyperlinks mit dem auf gesetzten Zielattribut gerendert_ leer. Das bedeutet, wenn Sie auf den Hyperlink in einer GridWeb-Zelle klicken, wird er in einem neuen Fenster anstelle des vorhandenen Fensters geöffnet. Wenn Sie den Hyperlink im vorhandenen Fenster öffnen möchten, setzen Sie bitte das GridHyperlink.Target auf_selbst.
## **Greifen Sie auf das Hyperlink-Objekt des GridWeb Cell zu**
Der folgende Beispielcode greift auf den Hyperlink von Zelle A1 zu. Wenn Zelle A1 einen Hyperlink enthält, wird das GridHyperlink-Objekt zurückgegeben, andernfalls wird null zurückgegeben.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

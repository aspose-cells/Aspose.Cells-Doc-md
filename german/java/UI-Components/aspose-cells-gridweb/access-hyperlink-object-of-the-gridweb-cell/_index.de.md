---
title: Greifen Sie auf das Hyperlink-Objekt des GridWeb Cell zu
type: docs
weight: 60
url: /de/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **Mögliche Nutzungsszenarien**
Mit den folgenden zwei Methoden können Sie überprüfen, ob die Zelle einen Hyperlink enthält oder nicht. Diese Methoden geben null zurück, wenn die Zelle keinen Hyperlink enthält, und wenn sie einen Hyperlink enthält, geben sie das GridHyperlink-Objekt zurück.

- GridHyperlinkCollection.getHyperlink(GridCell-Zelle)
- GridHyperlinkCollection.getHyperlink(int row,int columns)
##  **Öffnen Sie den Hyperlink in einem neuen oder vorhandenen Fenster**
 Wenn Ihre Excel-Datei einen Hyperlink enthält, der auf eine URL wie z<http://wwww.aspose.com/> und Sie laden es in GridWeb, dann werden die Hyperlinks mit dem auf _blank gesetzten Zielattribut gerendert. Das heißt, wenn Sie auf den Hyperlink in einer GridWeb-Zelle klicken, wird diese in einem neuen Fenster statt im vorhandenen Fenster geöffnet. Wenn Sie außerdem den Hyperlink im vorhandenen Fenster öffnen möchten, setzen Sie bitte GridHyperlink.Target auf _self.
##  **Greifen Sie auf das Hyperlink-Objekt des GridWeb Cell zu**
Der folgende Beispielcode greift auf den Hyperlink von Zelle A1 zu. Wenn Zelle A1 einen Hyperlink enthält, wird das GridHyperlink-Objekt zurückgegeben, andernfalls wird Null zurückgegeben.
##  **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

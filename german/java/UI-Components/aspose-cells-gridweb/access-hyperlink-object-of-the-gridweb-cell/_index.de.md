---
title: Hyperlink Objekt der GridWeb Zelle zugreifen
type: docs
weight: 60
url: /de/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **Mögliche Verwendungsszenarien**
Sie können überprüfen, ob eine Zelle einen Hyperlink enthält oder nicht, indem Sie die folgenden beiden Methoden verwenden. Diese Methoden geben null zurück, wenn die Zelle keinen Hyperlink enthält, und wenn sie einen Hyperlink enthält, wird ein GridHyperlink-Objekt zurückgegeben.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **Hyperlink in neuem oder vorhandenem Fenster öffnen**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **Hyperlink-Objekt der GridWeb-Zelle zugreifen**
Der folgende Beispielcode greift auf den Hyperlink der Zelle A1 zu. Wenn die Zelle A1 einen Hyperlink enthält, wird ein GridHyperlink-Objekt zurückgegeben, andernfalls wird null zurückgegeben.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

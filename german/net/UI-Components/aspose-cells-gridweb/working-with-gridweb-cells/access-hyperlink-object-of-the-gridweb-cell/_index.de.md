---
title: Greifen Sie auf das Hyperlink-Objekt des GridWeb Cell zu
type: docs
weight: 100
url: /de/net/access-hyperlink-object-of-the-gridweb-cell/
---
## **Mögliche Nutzungsszenarien**
Sie können mit den folgenden zwei Methoden überprüfen, ob die Zelle einen Hyperlink enthält oder nicht. Diese Methoden geben null zurück, wenn die Zelle keinen Hyperlink enthält, und wenn sie einen Hyperlink enthält, wird das GridHyperlink-Objekt zurückgegeben.

- GridHyperlinkCollection.GetHyperlink(GridCell-Zelle)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Hyperlink in neuem oder vorhandenem Fenster öffnen**
 Wenn Ihre Excel-Datei einen Hyperlink enthält, der auf eine URL wie z<http://wwww.aspose.com/> und Sie laden es in GridWeb, dann werden die Hyperlinks mit dem auf gesetzten Zielattribut gerendert_ leer. Das bedeutet, wenn Sie auf den Hyperlink in einer GridWeb-Zelle klicken, wird er in einem neuen Fenster statt in einem bestehenden Fenster geöffnet. Bitte überprüfen Sie die GridHyperlink.Target-Eigenschaft im folgenden Debug-Fenster. Wenn Sie den Hyperlink im vorhandenen Fenster öffnen möchten, setzen Sie bitte das GridHyperlink.Target auf_selbst.

![todo: Bild_alt_Text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Greifen Sie auf das Hyperlink-Objekt des GridWeb Cell zu**
Der folgende Beispielcode greift auf den Hyperlink von Zelle A1 zu. Wenn Zelle A1 einen Hyperlink enthält, wird das GridHyperlink-Objekt zurückgegeben, andernfalls wird null zurückgegeben.
### **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

---
title: Hyperlink Objekt der GridWeb Zelle zugreifen
type: docs
weight: 100
url: /de/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb, Hyperlink
description: Dieser Artikel stellt vor, wie man mit Hyperlinks in GridWeb arbeitet.
---

## **Mögliche Verwendungsszenarien**
Sie können überprüfen, ob eine Zelle einen Hyperlink enthält oder nicht, indem Sie die folgenden beiden Methoden verwenden. Diese Methoden geben null zurück, wenn die Zelle keinen Hyperlink enthält, und wenn sie einen Hyperlink enthält, wird ein GridHyperlink-Objekt zurückgegeben.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Hyperlink in neuem oder vorhandenem Fenster öffnen**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Hyperlink-Objekt der GridWeb-Zelle zugreifen**
Der folgende Beispielcode greift auf den Hyperlink der Zelle A1 zu. Wenn die Zelle A1 einen Hyperlink enthält, wird ein GridHyperlink-Objekt zurückgegeben, andernfalls wird null zurückgegeben.
### **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

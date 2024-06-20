---
title: Доступ к объекту гиперссылки в ячейке GridWeb
type: docs
weight: 100
url: /ru/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb, гиперссылка
description: Эта статья рассказывает о работе с гиперссылками в GridWeb.
---

## **Возможные сценарии использования**
Вы можете проверить, содержит ли ячейка гиперссылку, используя следующие два метода. Эти методы вернут null, если ячейка не содержит гиперссылки, и если она содержит гиперссылку, то вернут объект GridHyperlink.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Открыть гиперссылку в новом или существующем окне**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Доступ к объекту гиперссылки в ячейке GridWeb**
В следующем примере кода осуществляется доступ к гиперссылке ячейки A1. Если ячейка A1 содержит гиперссылку, то будет возвращен объект GridHyperlink, в противном случае будет возвращено значение null.
### **Образец кода**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

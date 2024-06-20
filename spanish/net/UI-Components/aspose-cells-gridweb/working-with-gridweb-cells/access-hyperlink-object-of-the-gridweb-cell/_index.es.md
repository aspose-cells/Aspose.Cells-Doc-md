---
title: Acceder al objeto Hipervínculo de la celda GridWeb
type: docs
weight: 100
url: /es/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb,hipervínculo
description: Este artículo presenta cómo trabajar con hipervínculos en GridWeb.
---

## **Escenarios de uso posibles**
Puede verificar si la celda contiene un hipervínculo o no utilizando los siguientes dos métodos. Estos métodos devolverán nulo si la celda no contiene un hipervínculo, y si contiene un hipervínculo, devolverá el objeto GridHyperlink.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Abrir hipervínculo en una ventana nueva o existente**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Acceder al objeto Hipervínculo de la celda GridWeb**
El siguiente código de ejemplo accede al hipervínculo de la celda A1. Si la celda A1 contiene un hipervínculo, devolverá el objeto GridHyperlink, de lo contrario, devolverá nulo.
### **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

---
title: Kom åt Hyperlink objektet för GridWeb cell
type: docs
weight: 100
url: /sv/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb, hyperlänk
description: Den här artikeln introducerar hur man arbetar med hyperlänk i GridWeb.
---

## **Möjliga användningsscenario**
Du kan kontrollera om cellen innehåller en hyperlänk eller inte med hjälp av följande två metoder. Dessa metoder kommer att returnera null om cellen inte innehåller en hyperlänk, och om den innehåller en hyperlänk kommer den att returnera GridHyperlink-objekt.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Öppna Hyperlänk i nytt eller befintligt fönster**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Kom åt Hyperlink-objektet för GridWeb-cell**
Följande exempelkod får åtkomst till hyperlänken för cell A1. Om cell A1 innehåller en hyperlänk kommer den att returnera GridHyperlink-objekt, annars kommer den att returnera null.
### **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

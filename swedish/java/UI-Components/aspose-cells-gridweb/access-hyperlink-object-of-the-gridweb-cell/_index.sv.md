---
title: Kom åt Hyperlink objektet för GridWeb cell
type: docs
weight: 60
url: /sv/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **Möjliga användningsscenario**
Du kan kontrollera om cellen innehåller en hyperlänk eller inte med hjälp av följande två metoder. Dessa metoder kommer att returnera null om cellen inte innehåller en hyperlänk, och om den innehåller en hyperlänk kommer den att returnera GridHyperlink-objekt.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **Öppna Hyperlänk i nytt eller befintligt fönster**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **Kom åt Hyperlink-objektet för GridWeb-cell**
Följande exempelkod får åtkomst till hyperlänken för cell A1. Om cell A1 innehåller en hyperlänk kommer den att returnera GridHyperlink-objekt, annars kommer den att returnera null.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

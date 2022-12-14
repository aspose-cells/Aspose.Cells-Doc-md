---
title: Få åtkomst till Hyperlink-objektet i GridWeb Cell
type: docs
weight: 100
url: /sv/net/access-hyperlink-object-of-the-gridweb-cell/
---
## **Möjliga användningsscenarier**
Du kan kontrollera om cellen innehåller hyperlänk eller inte med följande två metoder. Dessa metoder returnerar null om cellen inte innehåller en hyperlänk och om den innehåller en hyperlänk kommer den att returnera GridHyperlink-objekt.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int rad,int kolumn)
## **Öppna hyperlänk i nytt eller befintligt fönster**
 Om din excel-fil innehåller hyperlänk som länkar till någon URL som<http://wwww.aspose.com/> och du laddar den i GridWeb så kommer hyperlänkarna att renderas med target-attributet inställt på_ tom. Det betyder att när du klickar på hyperlänken i en GridWeb-cell kommer den att öppnas i ett nytt fönster istället för det befintliga fönstret. Kontrollera egenskapen GridHyperlink.Target i följande felsökningsfönster. Om du dessutom vill öppna hyperlänken i det befintliga fönstret, ställ in GridHyperlink.Target till_själv.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Få åtkomst till Hyperlink-objektet i GridWeb Cell**
Följande exempelkod ger åtkomst till hyperlänken i cell A1. Om cell A1 innehåller hyperlänk kommer den att returnera GridHyperlink-objekt, annars returnerar den null.
### **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

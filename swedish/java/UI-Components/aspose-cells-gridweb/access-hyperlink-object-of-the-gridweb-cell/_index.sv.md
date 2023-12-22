---
title: Få åtkomst till Hyperlink-objektet i GridWeb Cell
type: docs
weight: 60
url: /sv/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **Möjliga användningsscenarier**
Du kan kontrollera om cellen innehåller hyperlänk eller inte med följande två metoder. Dessa metoder returnerar null om cellen inte innehåller en hyperlänk och om den innehåller en hyperlänk kommer den att returnera GridHyperlink-objekt.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int rad,int kolumn)
##  **Öppna hyperlänk i nytt eller befintligt fönster**
 Om din excel-fil innehåller hyperlänk som länkar till någon URL som<http://wwww.aspose.com/> och du laddar det i GridWeb så kommer hyperlänkarna att renderas med target-attributet satt till _blank. Det betyder att när du klickar på hyperlänken i en GridWeb-cell kommer den att öppnas i ett nytt fönster istället för det befintliga fönstret. Dessutom, om du vill öppna hyperlänken i det befintliga fönstret, ställ in GridHyperlink.Target till _self.
##  **Få åtkomst till Hyperlink-objektet i GridWeb Cell**
Följande exempelkod ger åtkomst till hyperlänken i cell A1. Om cell A1 innehåller hyperlänk kommer den att returnera GridHyperlink-objekt, annars returnerar den null.
##  **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

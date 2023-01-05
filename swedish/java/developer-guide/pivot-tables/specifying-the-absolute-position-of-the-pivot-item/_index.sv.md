---
title: Ange den absoluta positionen för pivotobjektet
type: docs
weight: 40
url: /sv/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Ibland behöver användaren specificera den absoluta positionen för pivotposterna, Aspose.Cells API har exponerat några nya egenskaper och en metod för att uppnå detta användarkrav.

-  Lagt till[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) egenskap som kan användas för att ange positionsindex i alla PivotItems oavsett föräldernod. Lagt till[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) egenskap som kan användas för att ange positionsindex i PivotItems under samma överordnade nod.
-  Lagt till[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)metod för att flytta objektet uppåt eller nedåt baserat på räknevärdet, där antalet är antalet positioner för att flytta PivotItem uppåt eller nedåt. Om räknevärdet är mindre än noll kommer objektet att flyttas uppåt, medan om räknevärdet är större än noll kommer PivotItem att flyttas nedåt, boolesk typ isSameParent parameter som anger om flyttoperationen måste utföras i samma överordnade nod eller inte.
-  Föråldrad den*PivotItem.move(int count)* metod, därför föreslås det att använda den nyligen tillagda metoden[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) istället.

 Observera att det är nödvändigt att ringa till[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) och[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) metoder innan användning[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) fastigheter och[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) metod.

{{% /alert %}}

## Exempelkod

Följande exempelkod skapar en pivottabell och anger sedan pivotobjektens positioner i samma överordnade nod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}

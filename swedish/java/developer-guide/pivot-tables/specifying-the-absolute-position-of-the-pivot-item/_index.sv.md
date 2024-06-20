---
title: Ange den absoluta positionen för Pivot Item
type: docs
weight: 40
url: /sv/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Ibland behöver användaren ange den absoluta positionen för pivotobjekten. Aspose.Cells API har exponerat några nya egenskaper och en metod för att uppfylla detta användarkrav.

- Lagt till egenskapen [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) som kan användas för att ange positionens index för alla PivotItems oavsett föräldernod. Lagt till egenskapen [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) som kan användas för att ange positionens index för PivotItems under samma föräldernod.
- Tillagt [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean))-metod för att flytta objektet uppåt eller nedåt baserat på räkningsvärdet, där räkningen är antalet positioner att flytta PivotItem uppåt eller nedåt. Om räkningsvärdet är mindre än noll flyttas objektet uppåt medan om räkningsvärdet är större än noll kommer PivotItem att flyttas nedåt, Boolean-typen ärSameParent- parameter som anger om flyttoperationen måste utföras i samma föräldernod eller inte.
- Ogiltigförklarade metoden *PivotItem.move(int count)*, därför rekommenderas det att istället använda den nyttillagda metoden [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)).

Observera att det är nödvändigt att anropa metoderna [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) and [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) innan du använder egenskaperna [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) och metoden [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)).

{{% /alert %}}

## Exempelkod

Följande exempelkod skapar en pivot-tabell och anger sedan pivotobjektens positioner i samma föräldernod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}

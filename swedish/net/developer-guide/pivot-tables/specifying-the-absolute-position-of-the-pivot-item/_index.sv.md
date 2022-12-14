---
title: Ange den absoluta positionen för pivotobjektet
type: docs
weight: 50
url: /sv/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Ibland måste användaren specificera den absoluta positionen för pivotposterna, Aspose.Cells API har exponerat få nya egenskaper och en metod för att uppnå användarkrav.

-  Lagt till[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) egenskap som kan användas för att ange positionsindex i alla PivotItems oavsett föräldernod. Lagt till[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) egenskap som kan användas för att ange positionsindex i PivotItems under samma överordnade nod.
-  Lagt till[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)metod för att flytta objektet uppåt eller nedåt baserat på räknevärdet, där count är antalet positioner för att flytta PivotItem uppåt eller nedåt. Om räknevärdet är mindre än noll, kommer objektet att flyttas uppåt, där som om räknevärdet är större än noll, kommer PivotItem att flyttas nedåt, boolesk typ isSameParent parametern anger om flyttoperationen måste utföras i samma överordnade nod eller inte.
-  Föråldrad den*PivotItem.Move(int count)* metod, därför föreslås det att använda den nyligen tillagda metoden[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) istället.

{{% /alert %}}

 Följande exempelkod skapar en pivottabell och anger sedan pivotobjektens positioner i samma överordnade nod. Du kan ladda ner[käll Excel](5112632.xlsx) och[utgång Excel](5112619.xlsx) filer för din referens. Om du öppnar den utgående Excel-filen kommer du att se pivotobjektet "4H12" är på 0:e positionen i överordnat "K11" och "DIF400" är på 3:e positionen. På samma sätt är CA32 i position 1 och AAA3 är i position 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Observera att det är nödvändigt att anropa metoderna PivotTable.RefreshData och PivotTable.CalculateData innan du använder[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) fastigheter och[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) metod.

{{% /alert %}}

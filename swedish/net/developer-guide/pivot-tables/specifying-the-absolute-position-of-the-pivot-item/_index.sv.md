---
title: Specificera den absoluta positionen för pivotposten
type: docs
weight: 50
url: /sv/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Ibland behöver användaren specificera den absoluta positionen för pivotposterna. Aspose.Cells API har exponerat några nya egenskaper och en metod för att uppfylla användarens krav.

- Lagt till egenskapen [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) som kan användas för att ange positionens index för alla PivotItems oavsett föräldernod. Lagt till egenskapen [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) som kan användas för att ange positionens index för PivotItems under samma föräldernod.
- Lagt till metoden [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) för att flytta posten upp eller ner baserat på räkningsvärdet, där räkningsvärdet är antalet positioner att flytta PivotItem upp eller ner. Om räkningsvärdet är mindre än noll kommer posten att flyttas upp, medan om räkningsvärdet är större än noll kommer PivotItem att flyttas ner, Boolean typen isSameParent-parameter specificerar om flytoperationen måste utföras i samma föräldernod eller inte.
- Föråldrad metoden *PivotItem.Move(int count)* därför rekommenderas att använda den nyinsatta metoden [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) istället.

{{% /alert %}}

Följande provkod skapar en pivottabell och sedan specificerar den pivotpostens positioner i samma föräldernod. Du kan ladda ner [käll-Excel](5112632.xlsx)- och [utdata-Excel](5112619.xlsx)-filer för din referens. Om du öppnar utdata-Excel-filen kommer du att se att pivotposten "4H12" är på 0: e position i förälder "K11" och "DIF400" är på 3: e position. På samma sätt är CA32 på position 1 och AAA3 är på position 2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Observera att det är nödvändigt att använda metoderna [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) och [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) i början av applikationen, det vill säga; innan du kallar några andra objekt i Aspose.Cells API.

{{% /alert %}}

---
title: specificering av den absoluta positionen för pivottabeln med Golang via C++
linktitle: Specificera den absoluta positionen för pivotposten
type: docs
weight: 50
url: /sv/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Lär dig hur du anger den absoluta positionen för pivotobjekt i C++ med Aspose.Cells.
---

{{% alert color="primary" %}}

Ibland måste användare ange den absoluta positionen för pivotobjekt. Aspose.Cells API har exponerat några nya egenskaper och en metod för att uppnå detta krav.

- Lagt till egenskapen [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) som kan användas för att ange positionens index för alla PivotItems oavsett föräldernod. Lagt till egenskapen [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) som kan användas för att ange positionens index för PivotItems under samma föräldernod.
- Lagt till [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) metod för att flytta objektet upp eller ned baserat på räknevärdet, där räknevärdet är antalet positioner att flytta PivotItem upp eller ned. Om räknevärdet är mindre än noll flyttas objektet upp, medan om räknevärdet är större än noll flyttas PivotItem ned. den booleska typen `isSameParent`-parametern specificerar om flyttningen ska göras inom samma föräldraenhet eller inte.
- Äldre `PivotItem.Move(int count)`-metoden; därför rekommenderas det att använda den nyare metoden [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) istället.

{{% /alert %}}

Följande exempel på kod skapar en pivottabell och specificerar sedan pivotobjektets positioner inom samma föräldranod. Du kan ladda ner [käll-Excel](5112632.xlsx) och [utdata-Excel](5112619.xlsx) filer för referens. Om du öppnar utdatafilen ser du att pivotobjektet "4H12" är på position 0 inom föräldern "K11" och "DIF400" är på position 3. På samma sätt är CA32 på position 1 och AAA3 på position 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Observera att det är nödvändigt att kalla `PivotTable.RefreshData` och `PivotTable.CalculateData`-metoderna innan du använder [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) egenskaper och [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) metod.

{{% /alert %}}

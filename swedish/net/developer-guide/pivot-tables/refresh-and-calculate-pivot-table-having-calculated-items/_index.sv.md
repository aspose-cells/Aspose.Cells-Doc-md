---
title: Uppdatera och beräkna pivottabellen med beräknade objekt
type: docs
weight: 40
url: /sv/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells stöder nu uppdatering och beräkning av pivottabell med beräknade objekt. Vänligen använd[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) och[**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) som vanligt för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabellen med beräknade objekt**

 Följande exempelkod laddar[source excel-fil](5115238.xlsx)som innehåller en pivottabell med tre beräknade poster såsom "add", "div", "div2". Vi ändrar först värdet på cell D2 till 20 och uppdaterar och beräknar sedan pivottabellen med Aspose.Cells API:er och sparar arbetsboken i formatet PDF. Resultaten i[utgång PDF](5115229.pdf) visar att Aspose.Cells uppdaterade och beräknade pivottabellen efter att ha beräknat objekt framgångsrikt. Du kan verifiera det med Microsoft Excel genom att manuellt sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen via Alt+F5 genvägstangent eller klicka på pivottabellen Uppdatera-knappen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}

---
title: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 40
url: /sv/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells stöder nu uppdatering och beräkning av pivottabell med beräknade poster. Använd vanligtvis [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) och [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Följande kodexempel laddar in [käll-excelfilen](5115238.xlsx) som innehåller en pivottabell med tre beräknade poster såsom "add", "div", "div2". Vi ändrar först värdet i cell D2 till 20 och uppdaterar och beräknar sedan pivottabellen med Aspose.Cells API:er och sparar arbetsboken i PDF-format. Resultaten i [utdata PDF](5115229.pdf) visar att Aspose.Cells har uppdaterat och beräknat pivottabellen med beräknade poster framgångsrikt. Du kan verifiera det med hjälp av Microsoft Excel genom manuellt sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen via genvägen Alt+F5 eller genom att klicka på pivottabellens Uppdatera-knapp.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}

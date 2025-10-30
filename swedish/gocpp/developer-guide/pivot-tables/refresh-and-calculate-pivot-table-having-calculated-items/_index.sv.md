---
title: Uppdatera och beräkna pivottabell med beräknade objekt med Golang via C++
linktitle: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 40
url: /sv/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Uppdatera och beräkna pivottabell med beräknade objekt med Aspose.Cells för Golang via C++
---

{{% alert color="primary" %}}

Aspose.Cells stöder nu uppdatering och beräkning av pivottabell med beräknade poster. Använd vanligtvis [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) och [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Följande exempel laddar [käll-Excel-fil](5115238.xlsx) som innehåller en pivottabell med tre beräknade objekt, såsom "add", "div", "div2". Vi ändrar först värdet i cell D2 till 20 och uppdaterar sedan och beräknar pivottabellen med Aspose.Cells API:er och sparar arbetsboken i PDF-format. Resultatet i [utdata-PDF](5115229.pdf) visar att Aspose.Cells framgångsrikt uppdaterade och beräknade pivottabellen med beräknade objekt. Du kan verifiera detta manuellt i Microsoft Excel genom att sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen via tangentkombinationen Alt+F5 eller genom att klicka på pivottabellens Uppdatera-knapp.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}

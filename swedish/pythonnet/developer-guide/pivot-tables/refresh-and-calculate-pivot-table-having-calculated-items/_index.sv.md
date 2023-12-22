---
title: Uppdatera och beräkna pivottabellen med beräknade objekt
type: docs
weight: 40
url: /sv/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Den här artikeln visar hur du uppdaterar och beräknar pivottabell med beräknade objekt med Aspose.Cells for Python via .NET.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET stöder nu uppdatering och beräkning av pivottabell med beräknade poster. Vänligen använd[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) och[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) som vanligt för att utföra denna funktion.

{{% /alert %}}

##  **Uppdatera och beräkna pivottabellen med beräknade objekt**

 Följande exempelkod laddar[source excel-fil](5115238.xlsx)som innehåller en pivottabell med tre beräknade poster såsom "add", "div", "div2". Vi ändrar först värdet på cell D2 till 20 och uppdaterar och beräknar sedan pivottabellen med Aspose.Cells for Python via .NET API:er och sparar arbetsboken i formatet PDF. Resultaten i[utgång PDF](5115229.pdf) visar att Aspose.Cells for Python via .NET uppdaterade och beräknade pivottabellen efter att ha beräknat objekt framgångsrikt. Du kan verifiera det med Microsoft Excel genom att manuellt sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen med Alt+F5 genvägstangent eller klicka på pivottabellen Uppdatera-knappen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}

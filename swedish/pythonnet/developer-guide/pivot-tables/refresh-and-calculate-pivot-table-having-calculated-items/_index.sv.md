---
title: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 40
url: /sv/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Den här artikeln visar hur du uppdaterar och beräknar en pivottabell med beräknade poster med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Uppdatera och beräkna pivottabell med beräknade poster
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET stöder nu uppdatering och beräkning av pivottabell med beräknade poster. Använd [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) och [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) som vanligt för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Den följande exempelkoden laddar [käll-Excel-filen](5115238.xlsx) som innehåller en pivottabell med tre beräknade poster som "addera", "dela", "dela2". Först ändrar vi värdet i cell D2 till 20 och sedan uppdaterar och beräknar pivottabellen med hjälp av Aspose.Cells för Python via .NET API:er och sparar arbetsboken i PDF-format. Resultatet i [utdata-PDFen](5115229.pdf) visar att Aspose.Cells för Python via .NET har uppdaterat och beräknat pivottabellen med beräknade poster framgångsrikt. Du kan verifiera det genom att manuellt ange värdet 20 i cell D2 och sedan uppdatera pivottabellen via kortkommandot Alt+F5 eller genom att klicka på pivottabellens Uppdatera-knapp.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}

---
title: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 130
url: /sv/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells stödjer nu att uppdatera och beräkna pivottabell med beräknade poster. Använd [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) och [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) som vanligt för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Följande exempelkod laddar in [källfilen i Excel](5473428.xlsx) som innehåller en pivottabell med tre beräknade poster såsom "add", "div", "div2". Vi ändrar först värdet i cell D2 till 20 och uppdaterar och beräknar sedan pivottabellen med Aspose.Cells API:er och sparar arbetsboken i PDF-format. Resultaten i [utdata-PDF:en](5473431.pdf) visar att Aspose.Cells framgångsrikt uppdaterade och beräknade pivottabellen med beräknade poster. Du kan verifiera det med hjälp av Microsoft Excel genom att manuellt ange värdet 20 i cell D2 och sedan uppdatera pivottabellen via genvägsförkortningen Alt+F5 eller genom att klicka på knappen för att uppdatera pivottabellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}

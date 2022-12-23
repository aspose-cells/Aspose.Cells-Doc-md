---
title: Uppdatera och beräkna pivottabellen med beräknade objekt
type: docs
weight: 130
url: /sv/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells stöder nu uppdatering och beräkning av pivottabell med beräknade objekt. Snälla använd[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) och[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) som vanligt för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabellen med beräknade objekt**

 Följande exempelkod laddar[source excel-fil](5473428.xlsx)som innehåller en pivottabell med tre beräknade poster såsom "add", "div", "div2". Vi ändrar först värdet på cell D2 till 20 och uppdaterar och beräknar sedan pivottabellen med Aspose.Cells API:er och sparar arbetsboken i formatet PDF. Resultaten i[utgång PDF](5473431.pdf) visar att Aspose.Cells uppdaterade och beräknade pivottabellen efter att ha beräknat objekt framgångsrikt. Du kan verifiera det med Microsoft Excel genom att manuellt sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen via Alt+F5 genvägstangent eller klicka på pivottabellen Uppdatera-knappen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}

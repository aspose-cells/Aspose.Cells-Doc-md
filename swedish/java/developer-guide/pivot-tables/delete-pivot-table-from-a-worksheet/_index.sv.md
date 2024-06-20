---
title: Ta bort pivottabell från ett arbetsblad
type: docs
weight: 50
url: /sv/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en funktion för att ta bort en pivot-tabell från ett kalkylblad. Du kan ta bort pivot-tabellen med pivot-tabell objektet eller pivot-tabellpositionen. Använd [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) metoden för att ta bort pivot-tabellen med pivot-tabell objektet och [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) metoden för att ta bort en pivot-tabell objekt med dess position i pivot-tabellkollektionen.

{{% /alert %}}

## **Exempel**

Följande kodexempel tar bort två pivot-tabeller från kalkylbladet. Först tar den bort pivot-tabellen med [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) metoden och sedan tar den bort pivot-tabellen med [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) metoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}

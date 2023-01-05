---
title: Ta bort pivottabell från ett kalkylblad
type: docs
weight: 50
url: /sv/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller en funktion för att ta bort eller ta bort en pivottabell från ett kalkylblad. Du kan ta bort pivottabellen med hjälp av pivottabellobjektet eller pivottabellpositionen. Vänligen använd[**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) ) metod för att ta bort pivottabellen med hjälp av pivottabellobjektet och[**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)metod för att ta bort ett pivottabellobjekt med dess position inuti pivottabellsamlingen.

{{% /alert %}}

## **Exempel**

 Följande exempelkod tar bort två pivottabeller från kalkylbladet. Först tar det bort pivottabellen med hjälp av[**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) metod och sedan tar den bort pivottabellen med[**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) metod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}

---
title: Frysa rutor i Apache POI och Aspose.Cells
type: docs
weight: 80
url: /sv/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Frys rutor**
Aspose.Cells tillhandahåller en klass, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)-klassen. Worksheet-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att konfigurera frysrutor, anropa freezePanes-metoden i Worksheet-klassen. FreezePanes-metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frusna kolumner**, antalet synliga kolumner i vänstra fönstret.

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Frysa rutor**
sheet.createFreezePane finns tillgänglig för att uppnå FreezePane-funktionalitet när du använder Apache POI SS - HSSF och XSSF

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

För mer information, besök [Frys rutor](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}

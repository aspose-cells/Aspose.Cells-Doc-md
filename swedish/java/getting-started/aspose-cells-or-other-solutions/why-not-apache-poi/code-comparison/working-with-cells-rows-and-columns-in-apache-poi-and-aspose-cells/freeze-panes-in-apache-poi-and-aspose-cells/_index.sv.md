---
title: Frys rutor i Apache POI och Aspose.Cells
type: docs
weight: 80
url: /sv/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Frys rutor**
Aspose.Cells tillhandahåller en klass,[Arbetsbok](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[Arbetsblad](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)klass. Klassen Worksheet tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att konfigurera frysa rutor, anrop Worksheet-klassens freezePanes-metod. FreezePanes-metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysningen börjar från.
- **Kolumn**, kolumnindex för cellen som frysningen startar från.
- **Frysta rader**, antalet synliga rader i den övre rutan.
- **Frysta kolonner**, antalet synliga kolumner i den vänstra rutan

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Frys rutor**
sheet.createFreezePane är tillgängligt för att uppnå FreezePane-funktionalitet när du använder Apache POI SS - HSSF och XSSF

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

 För mer information, besök[Frys rutor](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}

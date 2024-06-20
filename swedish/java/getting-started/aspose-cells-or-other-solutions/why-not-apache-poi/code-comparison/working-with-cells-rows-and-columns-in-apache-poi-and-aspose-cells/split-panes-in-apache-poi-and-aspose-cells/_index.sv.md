---
title: Dela upp fönsterrutor i Apache POI och Aspose.Cells
type: docs
weight: 70
url: /sv/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Dela fönster**
Aspose.Cells tillhandahåller en klass, Workbook, som representerar en Microsoft Excel-fil. Workbook-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera Excel-filer. För att implementera delade vyer, använd split-metoden i Worksheet-klassen. För att ta bort delade fönster, använd removeSplit-metoden.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Dela upp fönsterrutor**
Funktionaliteten för delade fönsterrutor kan uppnås genom createSplitPane-metoden när du använder Apache POI SS (HSSF & XSSF) API.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

För mer information, besök [Dela upp fönsterrutor](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

---
title: Delade rutor i Apache POI och Aspose.Cells
type: docs
weight: 70
url: /sv/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Delade rutor**
Aspose.Cells tillhandahåller en klass, arbetsbok som representerar en Microsoft Excel-fil. Klassen Workbook tillhandahåller ett brett utbud av egenskaper och metoder för att hantera Excel-filer. För att implementera delade vyer, använd arbetsbladsklassens delade metod. För att ta bort delade rutor, använd metoden removeSplit.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Delade rutor**
Funktionalitet för delade fönster kan uppnås genom att skapa SplitPane-metoden när du använder Apache POI SS (HSSF & XSSF) API

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

 För mer information, besök[Delade rutor](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

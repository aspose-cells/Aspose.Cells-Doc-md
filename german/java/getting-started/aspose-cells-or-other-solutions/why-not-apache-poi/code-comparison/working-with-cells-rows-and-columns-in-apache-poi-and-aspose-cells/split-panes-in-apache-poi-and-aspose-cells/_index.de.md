---
title: Geteilte Fenster in Apache POI und Aspose.Cells
type: docs
weight: 70
url: /de/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Geteilte Scheiben**
Aspose.Cells stellt eine Klasse Workbook bereit, die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Excel-Dateien. Um geteilte Ansichten zu implementieren, verwenden Sie die Split-Methode der Worksheet-Klasse. Um geteilte Bereiche zu entfernen, verwenden Sie die Methode removeSplit.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Geteilte Fenster**
Die Split Panes-Funktionalität kann durch die createSplitPane-Methode erreicht werden, während Apache POI SS (HSSF & XSSF) API verwendet wird

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Geteilte Scheiben](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

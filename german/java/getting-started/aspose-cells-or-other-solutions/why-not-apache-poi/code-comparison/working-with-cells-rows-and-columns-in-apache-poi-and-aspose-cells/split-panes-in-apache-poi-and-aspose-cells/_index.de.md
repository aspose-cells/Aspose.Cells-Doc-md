---
title: Bereiche in Apache POI und Aspose.Cells aufteilen
type: docs
weight: 70
url: /de/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Panes aufteilen**
Aspose.Cells bietet eine Klasse, Workbook, die eine Microsoft Excel-Datei repräsentiert. Die Workbook-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Excel-Dateien. Verwenden Sie die split-Methode der Worksheet-Klasse, um Splitansichten zu implementieren. Verwenden Sie die removeSplit-Methode, um Splitbereiche zu entfernen.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Bereiche aufteilen**
Die Split-Bereiche-Funktionalität kann durch die Methode createSplitPane unter Verwendung der Apache POI SS (HSSF & XSSF) API erreicht werden.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Split-Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

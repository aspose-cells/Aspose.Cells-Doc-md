---
title: Zellen ausblenden und einblenden
type: docs
weight: 30
url: /de/java/hide-and-unhide-cells/
---

## **Aspose.Cells - Zeilen und Spalten ausblenden und einblenden**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert. Die Klasse Worksheet bietet eine Cells-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die Cells-Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Zellen ausblenden/einblenden**
Um eine Zeile oder Spalte zu verstecken, verwendet Apache POI SS die Methode Row.setZeroHeight(boolean).

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Zeilen und Spalten ausblenden und einblenden](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}

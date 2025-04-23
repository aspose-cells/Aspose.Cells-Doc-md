---
title: Druckbereich festlegen
type: docs
weight: 40
url: /de/java/set-print-area/
---

## **Aspose.Cells - Druckbereich festlegen**
Standardmäßig umfasst nur der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen spezifischen Druckbereich des Arbeitsblatts festlegen.

Um einen bestimmten Druckbereich auszuwählen, verwenden Sie die Methode setPrintArea der Klasse [PageSetup](/java/pagesetup). Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Druckbereich festlegen**
Die Methode Workbook.setPrintArea ist verfügbar, um Seiteneigenschaften des Druckbereichs festzulegen.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Einstellen von Druckoptionen](/cells/de/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

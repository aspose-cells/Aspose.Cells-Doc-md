---
title: Zeile und Spalte automatisch anpassen
type: docs
weight: 10
url: /de/java/auto-fit-row-and-column/
description: Erfahren Sie, wie Sie Zeilen und Spalten mithilfe von Aspose.Cells for Java API automatisch anpassen.
keywords: How to Autofit Row and Column in Java, Autofit Row Data in workbook using Java, Java Autofit Column Data. 
---
##  **So passen Sie Zeilen und Spalten automatisch mit Aspose.Cells for Java an**
Der einfachste Ansatz zum automatischen Anpassen der Breite und Höhe einer Zeile ist der Aufruf der Worksheet.autoFitRow-Methode. Die autoFitRow-Methode verwendet einen Zeilenindex (der Zeile, deren Größe geändert werden soll) als Parameter.

**Bitte beachten Sie:**Wenn Sie Zeilen und Spalten in Excel-Tabellen mit Java automatisch anpassen möchten, besuchen Sie bitte[Zeilen und Spalten automatisch anpassen](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
##  **Apache POI SS – HSSF XSSF – Automatische Anpassung von Zeile und Spalte**
Apache POI SS – HSSF und XSSF bietet Sheet.autoSizeColumn zum automatischen Anpassen von Spalten

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
##  **Laden Sie Running Code herunter**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
##  **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)

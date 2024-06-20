---
title: Öffentliche API Änderungen in Aspose.Cells 8.4.2
type: docs
weight: 160
url: /de/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen der Aspose.Cells-API von Version 8.4.1 auf 8.4.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-2/), sondern auch eine Beschreibung von Änderungen im Verhalten im Hintergrund von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Verbessertes Diagrammerstellungsmechanismus**
Die Klasse com.aspose.cells.charts.Chart hat die Methode setChartDataRange freigelegt, um die Aufgabe der Diagrammerstellung zu erleichtern. Die Methode setChartDataRange akzeptiert zwei Parameter, wobei der erste Parameter vom Typ string den Zellbereich angibt, aus dem die Datenreihen geplottet werden sollen. Der zweite Parameter ist vom Typ Boolean und gibt die Plot-Ausrichtung an, d.h. ob die Datenreihen des Diagramms aus einem Bereich von Zellenwerten zeilen- oder spaltenweise geplottet werden sollen.

Der folgende Codeausschnitt zeigt, wie Sie mit wenigen Zeilen Code ein Säulendiagramm erstellen können, wobei angenommen wird, dass die Diagrammseriendaten auf demselben Arbeitsblatt von Zelle A1 bis D4 vorhanden sind.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Hinzugefügter VbaModuleCollection.add-Methode**
Aspose.Cells for Java 8.4.2 hat die VbaModuleCollection.add-Methode freigelegt, um ein neues VBA-Modul zur Instanz des Arbeitsmappens hinzuzufügen. Die VbaModuleCollection.add-Methode akzeptiert einen parameter vom Typ Worksheet, um ein arbeitsblattspezifisches Modul hinzuzufügen.

Der folgende Codeausschnitt zeigt, wie die VbaModuleCollection.add-Methode verwendet wird.

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Überladene Methode Cells.copyColumns hinzugefügt**
Aspose.Cells for Java 8.4.2 hat eine überladene Version der Cells.copyColumns-Methode freigelegt, um die Quellspalten auf das Ziel zu wiederholen. Die neu freigegebene Methode akzeptiert insgesamt 5 Parameter, wobei die ersten 4 Parameter wie bei der üblichen Cells.copyColumns-Methode sind. Der letzte Parameter vom Typ int gibt jedoch an, wie viele Zielspalten auf denen die Quellspalten wiederholt werden sollen.

Der folgende Codeausschnitt zeigt, wie die neu freigegebene Cells.copyColumns-Methode verwendet wird.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Enumeration Felder PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS hinzugefügt**
Mit der Version 8.4.2 hat die Aspose.Cells-API 2 neue Enumerationsfelder für PasteType hinzugefügt.

- PasteType.DEFAULT: Funktioniert ähnlich wie die "Alle"-Funktionalität von Excel zum Einfügen von Zellenbereichen.
- PasteType.ALL_EXCEPT_BORDERS: Funktioniert ähnlich wie die Funktionalität "Alle außer Rahmen" von Excel zum Einfügen von Zellenbereichen.

Der folgende Beispielcode zeigt die Verwendung des PasteType.DEFAULT-Feldes.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Ab der Version Aspose.Cells for Java 8.4.2 verhält sich das Enumerationsfeld PasteType.ALL anders als die Funktionalität "Alle" von Excel zum Einfügen von Zellenbereichen. Jetzt kopiert auch das PasteType.ALL die Spaltenbreiten auf den Zielenbereich im Gegensatz zur "Alle"-Funktionalität von Excel. Um das Verhalten"Alle" von Excel zu imitieren, verwenden Sie bitte den PasteType.DEFAULT.

{{% /alert %}}

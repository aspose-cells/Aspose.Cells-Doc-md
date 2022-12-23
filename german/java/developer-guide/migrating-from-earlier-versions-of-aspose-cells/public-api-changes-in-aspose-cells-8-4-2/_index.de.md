---
title: Öffentlich API Änderungen in Aspose.Cells 8.4.2
type: docs
weight: 160
url: /de/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.4.1 zu 8.4.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-2/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Verbesserter Diagrammerstellungsmechanismus**
Die Klasse com.aspose.cells.charts.Chart hat die Methode setChartDataRange verfügbar gemacht, um die Aufgabe der Diagrammerstellung zu vereinfachen. Die setChartDataRange-Methode akzeptiert zwei Parameter, wobei der erste Parameter vom Typ string ist, der den Zellbereich angibt, aus dem die Datenreihe gezeichnet werden soll. Der zweite Parameter ist vom Typ Boolean, der die Plotausrichtung angibt, d. h.; ob die Diagrammdatenreihen aus einem Bereich von Zellenwerten nach Zeile oder nach Spalten gezeichnet werden sollen.

Das folgende Code-Snippet zeigt, wie ein Säulendiagramm mit wenigen Codezeilen erstellt wird, vorausgesetzt, dass die Diagrammseriendaten des Diagramms auf demselben Arbeitsblatt von Zelle A1 bis D4 vorhanden sind.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Methode VbaModuleCollection.add Hinzugefügt**
Aspose.Cells for Java 8.4.2 hat die Methode VbaModuleCollection.add verfügbar gemacht, um der Instanz von Workbook ein neues VBA-Modul hinzuzufügen. Die Methode VbaModuleCollection.add akzeptiert einen Parameter vom Typ Arbeitsblatt, um ein arbeitsblattspezifisches Modul hinzuzufügen.

Der folgende Codeausschnitt zeigt, wie die VbaModuleCollection.add-Methode verwendet wird.

**Java**

{{< highlight "csharp" >}}

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

### **Überladene Methode Cells.copyColumns Hinzugefügt**
Aspose.Cells for Java 8.4.2 hat eine überladene Version der Methode Cells.copyColumns bereitgestellt, um die Quellspalten auf dem Ziel zu wiederholen. Die neu verfügbar gemachte Methode akzeptiert insgesamt 5 Parameter, wobei die ersten 4 Parameter dieselben sind wie bei der allgemeinen Methode Cells.copyColumns. Der letzte Parameter vom Typ int gibt jedoch die Anzahl der Zielspalten an, auf denen die Quellspalten wiederholt werden müssen.

Der folgende Codeausschnitt zeigt, wie die neu verfügbar gemachte Cells.copyColumns-Methode verwendet wird.

**Java**

{{< highlight "csharp" >}}

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

### **Aufzählungsfelder PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS Hinzugefügt**
Mit der Veröffentlichung von v8.4.2 hat die Aspose.Cells API 2 neue Aufzählungsfelder für PasteType hinzugefügt, wie unten beschrieben.

- PasteType.DEFAULT: Funktioniert ähnlich wie die „Alle“-Funktion von Excel zum Einfügen von Zellbereichen.
- PasteType.ALL_AUSSER_RÄNDER: Funktioniert ähnlich wie die Excel-Funktion „Alle außer Ränder“ zum Einfügen von Zellbereichen.

Der folgende Beispielcode demonstriert die Verwendung des PasteType.DEFAULT-Felds.

**Java**

{{< highlight "csharp" >}}

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

Ab der Version Aspose.Cells for Java 8.4.2 verhält sich das Enumerationsfeld PasteType.ALL anders als die „All“-Funktion von Excel zum Einfügen von Zellbereichen. Jetzt kopiert PasteType.ALL auch die Spaltenbreiten in den Zielbereich, im Gegensatz zu Excels „All“-Funktionalität. Um das „All“-Verhalten von Excel nachzuahmen, verwenden Sie bitte PasteType.DEFAULT.

{{% /alert %}}

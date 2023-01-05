---
title: Öffentlich API Änderungen in Aspose.Cells 8.4.2
type: docs
weight: 150
url: /de/net/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.4.1 zu 8.4.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-2/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Verbesserter Diagrammerstellungsmechanismus**
Die Klasse Aspose.Cells.Charts.Chart hat die SetChartDataRange-Methode verfügbar gemacht, um die Aufgabe der Diagrammerstellung zu vereinfachen. Die SetChartDataRange-Methode akzeptiert zwei Parameter, wobei der erste Parameter vom Typ Zeichenfolge ist, der den Zellbereich angibt, aus dem die Datenreihe gezeichnet werden soll. Der zweite Parameter ist vom Typ Boolean, der die Plotausrichtung angibt, d. h.; ob die Diagrammdatenreihen aus einem Bereich von Zellenwerten nach Zeile oder nach Spalten gezeichnet werden sollen.

Das folgende Code-Snippet zeigt, wie ein Säulendiagramm mit wenigen Codezeilen erstellt wird, vorausgesetzt, dass die Diagrammseriendaten des Diagramms auf demselben Arbeitsblatt von Zelle A1 bis D4 vorhanden sind.

**C#**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Methode VbaModuleCollection.Add Hinzugefügt**
Aspose.Cells for .NET 8.4.2 hat die Methode VbaModuleCollection.Add verfügbar gemacht, um der Instanz von Workbook ein neues VBA-Modul hinzuzufügen. Die Methode VbaModuleCollection.Add akzeptiert einen Parameter vom Typ Arbeitsblatt, um ein arbeitsblattspezifisches Modul hinzuzufügen.

Der folgende Codeausschnitt zeigt, wie die VbaModuleCollection.Add-Methode verwendet wird.

**C#**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Überladene Methode Cells.CopyColumns Hinzugefügt**
Aspose.Cells for .NET 8.4.2 hat eine überladene Version der Methode Cells.CopyColumns bereitgestellt, um die Quellspalten auf dem Ziel zu wiederholen. Die neu verfügbar gemachte Methode akzeptiert insgesamt 5 Parameter, wobei die ersten 4 Parameter die gleichen sind wie bei der allgemeinen Cells.CopyColumns-Methode. Der letzte Parameter vom Typ int gibt jedoch die Anzahl der Zielspalten an, auf denen die Quellspalten wiederholt werden müssen.

Der folgende Codeausschnitt zeigt, wie die neu verfügbar gemachte Cells.CopyColumns-Methode verwendet wird.

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Aufzählungsfelder PasteType.Default & PasteType.DefaultExceptBorders Hinzugefügt**
Mit der Veröffentlichung von v8.4.2 hat die Aspose.Cells API 2 neue Aufzählungsfelder für PasteType hinzugefügt, wie unten beschrieben.

- PasteType.Default: Funktioniert ähnlich wie die „Alle“-Funktion von Excel zum Einfügen von Zellbereichen.
- PasteType.DefaultExceptBorders: Funktioniert ähnlich wie die Excel-Funktion „Alle außer Rahmen“ zum Einfügen von Zellbereichen.

Der folgende Beispielcode demonstriert die Verwendung des PasteType.Default-Felds.

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Ab der Version Aspose.Cells for .NET 8.4.2 verhält sich das Enumerationsfeld PasteType.All anders als die „All“-Funktion von Excel zum Einfügen von Zellbereichen. Jetzt kopiert PasteType.All auch die Spaltenbreiten in den Zielbereich, im Gegensatz zu Excels „All“-Funktionalität. Um das „All“-Verhalten von Excel nachzuahmen, verwenden Sie bitte PasteType.Default.

{{% /alert %}}
